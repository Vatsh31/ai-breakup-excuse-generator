#!/bin/bash

echo "🚀 AI Breakup Excuse Generator Deployment Script"
echo "================================================"

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok is not installed. Please install it from https://ngrok.com/"
    echo "   After installation, get your auth token and update ngrok.yml"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Start the server in background
echo "🔧 Starting MCP server..."
cd mcp-bearer-token
python breakup_generator_simple.py &
SERVER_PID=$!

# Wait for server to start
sleep 3

# Start ngrok tunnel
echo "🌐 Starting ngrok tunnel..."
ngrok http 8087 --config ../ngrok.yml

# Cleanup on exit
trap "echo '🛑 Stopping server...'; kill $SERVER_PID; exit" INT 