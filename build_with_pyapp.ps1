$executable_name = "cv5"
# $env:PYAPP_INCLUDE = "cv4/utils;cv4/cc"
# $env:PYAPP_EXEC_SCRIPT = "C:/cv4/cv4/main.py"
# $env:PYAPP_PROJECT_DEPENDENCY_FILE="$((Get-Item -Path "./requirements.txt").FullName)"
$env:PYAPP_PROJECT_DEPENDENCY_FILE = "C:\cv4\requirements.txt"
$env:PYAPP__PROJECT_DEPENDENCY_FILE_NAME = "requirements.txt"
$env:PYAPP_EXEC_MODULE = "cv4.main"

# poetry export -f requirements.txt > requirements.txt
if (Test-Path -Path "./dist") {
    Remove-Item -Path ./dist -Recurse -Force
}

if (-Not (Test-Path -Path "./dist")) {
    Write-Host "Dist directory does not exist. Running poetry build..."
    poetry build
}
$wheel_file = (Get-Item -Path "./dist/*.whl").FullName

Write-Host "Wheel file path: $wheel_file"
$env:PYAPP_PROJECT_PATH=$wheel_file


if (!(Test-Path -Path "./pyapp-latest")) {
    Invoke-WebRequest https://github.com/ofek/pyapp/releases/latest/download/source.zip -OutFile pyapp-source.zip
    Expand-Archive -Path ./pyapp-source.zip -DestinationPath .
    Move-Item -Path ./pyapp-v* -Destination ./pyapp-latest
    Remove-Item -Path ./pyapp-source.zip
}

Set-Location -Path ./pyapp-latest
cargo build --release

Move-Item target\release\pyapp.exe ..\$executable_name.exe -Force

Set-Location -Path ..

