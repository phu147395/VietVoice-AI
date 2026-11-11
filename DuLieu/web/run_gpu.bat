@echo off
REM VietVoice AI - Chay server GPU (OmniVoice preload tren cuda:0)
REM Double-click file nay. Cua so se GIU NGUYEN neu co loi de xem.
cd /d "%~dp0"
set PY=..\..\venv310\Scripts\python.exe
if not exist "%PY%" (
  echo [LOI] Khong tim thay venv: %PY%
  echo Hay chay file nay tu thu muc LUANVAN\web
  pause
  exit /b 1
)
echo [TTS] Dang khoi dong server (lần đầu load model mất vài phút)...
echo [TTS] Mo trinh duyet: http://127.0.0.1:5000
echo [TTS] Nhan Ctrl+C de dung server
"%PY%" app.py
echo.
echo [TTS] Server da dung (ma loi %ERRORLEVEL%). Xem server.err.log neu can.
pause
