# ============================================================
#  verify-project.ps1
#  Health check for this repo on ANY computer.
#  Read-only: it changes nothing, it only reports.
#
#  Usage:
#    powershell -ExecutionPolicy Bypass -File .\tools\verify-project.ps1
# ============================================================

$ErrorActionPreference = "Continue"

if ([string]::IsNullOrEmpty($PSScriptRoot)) {
    $PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
}
$repoRoot = Split-Path -Parent $PSScriptRoot

$passCount = 0
$failCount = 0
$warnCount = 0
$results   = New-Object System.Collections.ArrayList

function Add-Result {
    param(
        [string]$Status,
        [string]$Item,
        [string]$Detail
    )
    [void]$results.Add([PSCustomObject]@{
        Status = $Status
        Item   = $Item
        Detail = $Detail
    })
    if ($Status -eq "PASS") { $script:passCount++ }
    elseif ($Status -eq "FAIL") { $script:failCount++ }
    else { $script:warnCount++ }
}

Write-Host ""
Write-Host "=================================================="
Write-Host " BDD Customer Intelligence  --  Project Health Check"
Write-Host "=================================================="
Write-Host ""
Write-Host (" Repo root : " + $repoRoot)
Write-Host (" Computer  : " + $env:COMPUTERNAME)
Write-Host (" User      : " + $env:USERNAME)
Write-Host (" Time      : " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss"))
Write-Host ""

# ---------- 1. git ----------
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
if ($gitCmd) {
    $gitVer = (& git --version) 2>$null
    Add-Result "PASS" "git installed" $gitVer
} else {
    Add-Result "FAIL" "git installed" "git not found in PATH - install from https://git-scm.com/download/win"
}

# ---------- 2. git identity ----------
$gName  = (& git config --global user.name) 2>$null
$gEmail = (& git config --global user.email) 2>$null
if ([string]::IsNullOrWhiteSpace($gName) -or [string]::IsNullOrWhiteSpace($gEmail)) {
    Add-Result "WARN" "git identity" "not configured - run: git config --global user.name / user.email"
} else {
    Add-Result "PASS" "git identity" ($gName + " <" + $gEmail + ">")
}

# ---------- 3. is this a git repo ----------
if (Test-Path (Join-Path $repoRoot ".git")) {
    $branch = (& git -C $repoRoot rev-parse --abbrev-ref HEAD) 2>$null
    $head   = (& git -C $repoRoot rev-parse --short HEAD) 2>$null
    Add-Result "PASS" "git repository" ("branch=" + $branch + "  head=" + $head)
    $remote = (& git -C $repoRoot remote get-url origin) 2>$null
    if ([string]::IsNullOrWhiteSpace($remote)) {
        Add-Result "WARN" "git remote" "no 'origin' remote yet - not pushed to GitHub"
    } else {
        Add-Result "PASS" "git remote" $remote
    }
} else {
    Add-Result "FAIL" "git repository" ".git folder missing - run git init"
}

# ---------- 4. skill source in repo ----------
$skillRepo = Join-Path $repoRoot "skill\bdd-inquiry-analyzer"
if (Test-Path $skillRepo) {
    $n = @(Get-ChildItem $skillRepo -Recurse -File).Count
    Add-Result "PASS" "skill (in repo)" ($n.ToString() + " files")
} else {
    Add-Result "FAIL" "skill (in repo)" "missing folder: skill\bdd-inquiry-analyzer"
}

# ---------- 5. skill deployed locally + md5 match ----------
$skillLocal = Join-Path $env:USERPROFILE ".workbuddy\skills\bdd-inquiry-analyzer"
if (-not (Test-Path $skillLocal)) {
    Add-Result "FAIL" "skill (local)" "not deployed - run: tools\restore-skill.ps1"
} else {
    $nLocal = @(Get-ChildItem $skillLocal -Recurse -File).Count
    $mismatch = 0
    if (Test-Path $skillRepo) {
        $a = @{}
        foreach ($f in (Get-ChildItem $skillRepo -Recurse -File)) {
            $rel = $f.FullName.Substring($skillRepo.Length).TrimStart("\")
            $a[$rel] = (Get-FileHash $f.FullName -Algorithm MD5).Hash
        }
        $b = @{}
        foreach ($f in (Get-ChildItem $skillLocal -Recurse -File)) {
            $rel = $f.FullName.Substring($skillLocal.Length).TrimStart("\")
            $b[$rel] = (Get-FileHash $f.FullName -Algorithm MD5).Hash
        }
        foreach ($k in $a.Keys) {
            if (-not $b.ContainsKey($k)) { $mismatch++ }
            elseif ($b[$k] -ne $a[$k]) { $mismatch++ }
        }
        foreach ($k in $b.Keys) {
            if (-not $a.ContainsKey($k)) { $mismatch++ }
        }
    }
    if ($mismatch -eq 0) {
        Add-Result "PASS" "skill (local)" ($nLocal.ToString() + " files, identical to repo")
    } else {
        Add-Result "WARN" "skill (local)" ($mismatch.ToString() + " file(s) differ from repo - run tools\sync-skill.ps1")
    }
}

# ---------- 6. python ----------
$pyCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pyCmd) {
    $pyVer = (& python --version) 2>$null
    Add-Result "PASS" "python" $pyVer
} else {
    Add-Result "WARN" "python" "not in PATH - only needed to re-render PDFs manually"
}

# ---------- 7. browser for PDF rendering ----------
$chromePaths = @(
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    (Join-Path $env:LOCALAPPDATA "Google\Chrome\Application\chrome.exe"),
    "C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
)
$foundBrowser = $null
foreach ($p in $chromePaths) {
    if (Test-Path $p) { $foundBrowser = $p; break }
}
if ($foundBrowser) {
    Add-Result "PASS" "browser (for PDF)" $foundBrowser
} else {
    Add-Result "FAIL" "browser (for PDF)" "no Chrome / Edge found - install one to render PDFs"
}

# ---------- 8. workbuddy home ----------
$wbHome = Join-Path $env:USERPROFILE ".workbuddy"
if (Test-Path $wbHome) {
    Add-Result "PASS" "WorkBuddy home" $wbHome
} else {
    Add-Result "WARN" "WorkBuddy home" "not found - install WorkBuddy first"
}

# ---------- 9. deliverables count ----------
$cards = @(Get-ChildItem $repoRoot -Filter "*_BDD_Intelligence_*.md" -File)
$pdfs  = @(Get-ChildItem $repoRoot -Filter "*.pdf" -File)
Add-Result "PASS" "intelligence cards" ($cards.Count.ToString() + " .md files")
Add-Result "PASS" "PDF deliverables" ($pdfs.Count.ToString() + " .pdf files")

# ---------- 10. archive ----------
$arch = Join-Path $repoRoot "_bdd-skill-archive"
if (Test-Path $arch) {
    $dirs = @(Get-ChildItem $arch -Directory)
    Add-Result "PASS" "version archive" ($dirs.Count.ToString() + " version folders")
} else {
    Add-Result "WARN" "version archive" "missing _bdd-skill-archive"
}

# ---------------- report ----------------
Write-Host "--------------------------------------------------"
Write-Host " CHECK RESULTS"
Write-Host "--------------------------------------------------"
foreach ($r in $results) {
    $color = "Gray"
    if ($r.Status -eq "PASS") { $color = "Green" }
    elseif ($r.Status -eq "FAIL") { $color = "Red" }
    elseif ($r.Status -eq "WARN") { $color = "Yellow" }
    Write-Host (" [" + $r.Status + "] " + $r.Item) -ForegroundColor $color
    Write-Host ("        " + $r.Detail)
}
Write-Host ""
Write-Host "--------------------------------------------------"
Write-Host (" TOTAL : PASS=" + $passCount + "  WARN=" + $warnCount + "  FAIL=" + $failCount)
Write-Host "--------------------------------------------------"
Write-Host ""

if ($failCount -eq 0) {
    Write-Host " RESULT: PASS - this machine is ready." -ForegroundColor Green
    Write-Host ""
    if ($warnCount -gt 0) {
        Write-Host " (WARN items are non-blocking, but worth fixing.)" -ForegroundColor Yellow
        Write-Host ""
    }
    exit 0
} else {
    Write-Host (" RESULT: FAIL - " + $failCount + " blocking problem(s) above.") -ForegroundColor Red
    Write-Host ""
    exit 1
}
