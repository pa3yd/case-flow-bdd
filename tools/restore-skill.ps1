# ============================================================
#  restore-skill.ps1
#  Deploy the "bdd-inquiry-analyzer" skill FROM this repo
#  INTO the local WorkBuddy skills folder.
#
#  When to run:
#    - First time on a new computer (e.g. office PC)
#    - After pulling newer changes from GitHub
#
#  Usage (PowerShell, no admin rights needed):
#    powershell -ExecutionPolicy Bypass -File .\tools\restore-skill.ps1
# ============================================================

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrEmpty($PSScriptRoot)) {
    $PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$src      = Join-Path $repoRoot "skill\bdd-inquiry-analyzer"
$destRoot = Join-Path $env:USERPROFILE ".workbuddy\skills"
$dest     = Join-Path $destRoot "bdd-inquiry-analyzer"

Write-Host ""
Write-Host "=================================================="
Write-Host " BDD Skill  --  Restore to local WorkBuddy"
Write-Host "=================================================="
Write-Host ""

# ---------------- [1/5] check source ----------------
Write-Host "[1/5] Checking source folder ..."
if (-not (Test-Path $src)) {
    Write-Host "      FAIL  source not found:" -ForegroundColor Red
    Write-Host ("            " + $src) -ForegroundColor Red
    exit 1
}
$srcFiles = @(Get-ChildItem $src -Recurse -File)
Write-Host ("      OK    source files = " + $srcFiles.Count)
Write-Host ""

# ---------------- [2/5] backup existing ----------------
Write-Host "[2/5] Backing up existing local skill (if any) ..."
if (Test-Path $dest) {
    $stamp  = Get-Date -Format "yyyyMMdd-HHmmss"
    $backup = Join-Path $destRoot ("bdd-inquiry-analyzer.bak-" + $stamp)
    Copy-Item $dest $backup -Recurse -Force
    Write-Host ("      OK    backup created at:")
    Write-Host ("            " + $backup)
} else {
    Write-Host "      SKIP  no existing skill installed"
}
Write-Host ""

# ---------------- [3/5] deploy ----------------
Write-Host "[3/5] Deploying files ..."
if (-not (Test-Path $destRoot)) {
    New-Item -ItemType Directory -Path $destRoot -Force | Out-Null
}
if (Test-Path $dest) {
    Remove-Item $dest -Recurse -Force
}
Copy-Item $src $dest -Recurse -Force
Write-Host ("      OK    deployed to:")
Write-Host ("            " + $dest)
Write-Host ""

# ---------------- [4/5] verify md5 ----------------
Write-Host "[4/5] Verifying integrity (MD5) ..."
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

$fail = 0
foreach ($k in $srcMap.Keys) {
    if (-not $dstMap.ContainsKey($k)) {
        Write-Host ("      MISSING       " + $k) -ForegroundColor Red
        $fail++
    }
    elseif ($dstMap[$k] -ne $srcMap[$k]) {
        Write-Host ("      HASH MISMATCH " + $k) -ForegroundColor Red
        $fail++
    }
}
if ($srcMap.Count -ne $dstMap.Count) {
    Write-Host ("      COUNT MISMATCH src=" + $srcMap.Count + " dst=" + $dstMap.Count) -ForegroundColor Red
    $fail++
}

if ($fail -eq 0) {
    Write-Host ("      PASS  " + $srcMap.Count + "/" + $srcMap.Count + " files verified")
    Write-Host ""
} else {
    Write-Host ("      FAIL  " + $fail + " problem(s) found") -ForegroundColor Red
    exit 1
}

# ---------------- [5/5] summary ----------------
Write-Host "[5/5] Done."
Write-Host ""
Write-Host "  Skill installed at:"
Write-Host ("    " + $dest)
Write-Host ""
Write-Host "  Next step:"
Write-Host "    1. Restart WorkBuddy so it rescans the skills folder."
Write-Host "    2. Ask it something like: background-check company XXX"
Write-Host "       The skill triggers automatically - no name needed."
Write-Host ""
