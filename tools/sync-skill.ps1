# ============================================================
#  sync-skill.ps1
#  Copy the LOCAL WorkBuddy skill BACK INTO this repo,
#  so that improvements made on this machine get committed
#  and can be pushed to GitHub.
#
#  Direction:  %USERPROFILE%\.workbuddy\skills\bdd-inquiry-analyzer
#                    -->  <repo>\skill\bdd-inquiry-analyzer
#
#  When to run:
#    - After you (or the AI) refined the skill on this machine
#    - Right before "git add / git commit / git push"
#
#  Usage:
#    powershell -ExecutionPolicy Bypass -File .\tools\sync-skill.ps1
# ============================================================

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrEmpty($PSScriptRoot)) {
    $PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$src      = Join-Path $env:USERPROFILE ".workbuddy\skills\bdd-inquiry-analyzer"
$dest     = Join-Path $repoRoot "skill\bdd-inquiry-analyzer"

Write-Host ""
Write-Host "=================================================="
Write-Host " BDD Skill  --  Sync local  ->  repo"
Write-Host "=================================================="
Write-Host ""

# ---------------- [1/4] check source ----------------
Write-Host "[1/4] Checking local skill ..."
if (-not (Test-Path $src)) {
    Write-Host "      FAIL  local skill not found:" -ForegroundColor Red
    Write-Host ("            " + $src) -ForegroundColor Red
    Write-Host "            Run restore-skill.ps1 first." -ForegroundColor Yellow
    exit 1
}
$srcFiles = @(Get-ChildItem $src -Recurse -File)
Write-Host ("      OK    local files = " + $srcFiles.Count)
Write-Host ""

# ---------------- [2/4] diff ----------------
Write-Host "[2/4] Comparing local  vs  repo ..."
$changed = New-Object System.Collections.ArrayList

if (Test-Path $dest) {
    $srcMap = @{}
    foreach ($f in (Get-ChildItem $src -Recurse -File)) {
        $rel = $f.FullName.Substring($src.Length).TrimStart("\")
        $srcMap[$rel] = (Get-FileHash $f.FullName -Algorithm MD5).Hash
    }
    $dstMap = @{}
    foreach ($f in (Get-ChildItem $dest -Recurse -File)) {
        $rel = $f.FullName.Substring($dest.Length).TrimStart("\")
        $dstMap[$rel] = (Get-FileHash $f.FullName -Algorithm MD5).Hash
    }

    foreach ($k in $srcMap.Keys) {
        if (-not $dstMap.ContainsKey($k)) {
            [void]$changed.Add("NEW      " + $k)
        }
        elseif ($dstMap[$k] -ne $srcMap[$k]) {
            [void]$changed.Add("MODIFIED " + $k)
        }
    }
    foreach ($k in $dstMap.Keys) {
        if (-not $srcMap.ContainsKey($k)) {
            [void]$changed.Add("DELETED  " + $k)
        }
    }
} else {
    [void]$changed.Add("(repo copy does not exist yet - full copy)")
}

if ($changed.Count -eq 0) {
    Write-Host "      OK    no differences - repo is already up to date"
    Write-Host ""
    Write-Host "  Nothing to do."
    Write-Host ""
    exit 0
}

foreach ($line in $changed) {
    Write-Host ("      " + $line)
}
Write-Host ""

# ---------------- [3/4] copy ----------------
Write-Host "[3/4] Copying local  ->  repo ..."
if (Test-Path $dest) {
    Remove-Item $dest -Recurse -Force
}
$destParent = Split-Path -Parent $dest
if (-not (Test-Path $destParent)) {
    New-Item -ItemType Directory -Path $destParent -Force | Out-Null
}
Copy-Item $src $dest -Recurse -Force
Write-Host ("      OK    copied to: " + $dest)
Write-Host ""

# ---------------- [4/4] verify ----------------
Write-Host "[4/4] Verifying integrity (MD5) ..."
$v1 = @{}
foreach ($f in (Get-ChildItem $src -Recurse -File)) {
    $rel = $f.FullName.Substring($src.Length).TrimStart("\")
    $v1[$rel] = (Get-FileHash $f.FullName -Algorithm MD5).Hash
}
$v2 = @{}
foreach ($f in (Get-ChildItem $dest -Recurse -File)) {
    $rel = $f.FullName.Substring($dest.Length).TrimStart("\")
    $v2[$rel] = (Get-FileHash $f.FullName -Algorithm MD5).Hash
}

$fail = 0
foreach ($k in $v1.Keys) {
    if (-not $v2.ContainsKey($k)) { $fail++ }
    elseif ($v2[$k] -ne $v1[$k]) { $fail++ }
}
if ($v1.Count -ne $v2.Count) { $fail++ }

if ($fail -eq 0) {
    Write-Host ("      PASS  " + $v1.Count + "/" + $v1.Count + " files verified")
    Write-Host ""
    Write-Host "  Repo is now in sync."
    Write-Host ""
    Write-Host "  Next step - publish to GitHub:"
    Write-Host '    git add -A'
    Write-Host '    git commit -m "Sync skill changes"'
    Write-Host '    git push'
    Write-Host ""
} else {
    Write-Host ("      FAIL  " + $fail + " problem(s)") -ForegroundColor Red
    exit 1
}
