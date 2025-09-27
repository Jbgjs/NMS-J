# elimNMS 서버 시작 스크립트
Write-Host "elimNMS 서버를 시작합니다..." -ForegroundColor Green

# 프로젝트 디렉토리로 이동
Set-Location "C:\Users\user\Downloads\elim-NMS\elimNMS-public"

# Python 가상환경의 Python으로 서버 시작
& "C:\Users\user\Downloads\elim-NMS\.venv\Scripts\python.exe" app.py

Write-Host "서버가 종료되었습니다." -ForegroundColor Yellow
Read-Host "계속하려면 Enter를 누르세요..."