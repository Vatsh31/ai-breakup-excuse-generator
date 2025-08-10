@echo off
echo 🚀 AI Breakup Excuse Generator Deployment Script
echo ================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Start the server
echo 🔧 Starting MCP server...
cd mcp-bearer-token
start "MCP Server" python breakup_generator_simple.py

REM Wait a moment for server to start
timeout /t 3 /nobreak >nul

echo.
echo ✅ Server is running on http://localhost:8087
echo.
echo 🌐 To expose with ngrok:
echo    1. Install ngrok from https://ngrok.com/
echo    2. Get your auth token
echo    3. Update ngrok.yml with your token
echo    4. Run: ngrok http 8087
echo.
echo 📱 Connect to MCP with:
echo    /mcp connect https://your-ngrok-url.ngrok.io/mcp breakup-excuse-token-2024
echo.
echo Press any key to stop the server...
pause >nul

REM Kill the server process
taskkill /f /im python.exe >nul 2>&1
echo 🛑 Server stopped. 