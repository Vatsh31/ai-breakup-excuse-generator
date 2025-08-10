# AI Breakup Excuse Generator 🚀

A hilarious MCP (Model Context Protocol) server that generates over-the-top, viral-worthy breakup excuses. Perfect for the Puch AI hackathon!

## Features

- 🎭 **7 Different Styles**: Dramatic, Funny, Sci-fi, Poetic, Absurd, Viral, and Trending
- 🔥 **150+ Templates**: Massive collection of creative breakup excuses
- 🌐 **MCP Protocol**: Compatible with any MCP client
- 🔐 **Bearer Token Auth**: Secure authentication
- 📱 **Viral Ready**: Designed to be screenshot and shared on social media

## Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   cd mcp-bearer-token
   python breakup_generator_simple.py
   ```

3. **Test the API:**
   ```bash
   curl http://localhost:8087/health
   ```

### Using ngrok for Local Development

1. **Install ngrok:**
   - Download from [ngrok.com](https://ngrok.com/)
   - Get your auth token from the dashboard

2. **Configure ngrok:**
   - Update `ngrok.yml` with your auth token
   - Or use the deployment script:
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

3. **Manual ngrok setup:**
   ```bash
   # Start your server first
   cd mcp-bearer-token
   python breakup_generator_simple.py
   
   # In another terminal, start ngrok
   ngrok http 8087
   ```

4. **Connect to MCP:**
   ```bash
   /mcp connect https://your-ngrok-url.ngrok.io/mcp breakup-excuse-token-2024
   ```

## Deploy to Render.com

### Option 1: Using render.yaml (Recommended)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add deployment files"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` file
   - Deploy!

### Option 2: Manual Deployment

1. **Create a new Web Service on Render:**
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd mcp-bearer-token && python breakup_generator_simple.py`

2. **Set Environment Variables:**
   - `AUTH_TOKEN`: `breakup-excuse-token-2024`
   - `MY_NUMBER`: `919876543210`

3. **Deploy!**

## API Endpoints

- `GET /` - Root endpoint with service info
- `GET /health` - Health check for Render.com
- `POST /mcp` - MCP protocol endpoint

## MCP Connection

Once deployed, connect using:

```bash
/mcp connect https://your-render-app.onrender.com/mcp breakup-excuse-token-2024
```

## Available Styles

1. **Dramatic** - Over-the-top dramatic excuses
2. **Funny** - Hilarious and absurd reasons
3. **Sci-fi** - Space and technology themed
4. **Poetic** - Beautiful and metaphorical
5. **Absurd** - Completely ridiculous excuses
6. **Viral** - Social media and influencer themed
7. **Trending** - Current internet trends and memes

## Environment Variables

- `AUTH_TOKEN` - Bearer token for authentication (default: `breakup-excuse-token-2024`)
- `MY_NUMBER` - Phone number for validation (default: `919876543210`)

## Development

### Project Structure

```
├── mcp-bearer-token/
│   └── breakup_generator_simple.py  # Main MCP server
├── requirements.txt                 # Python dependencies
├── render.yaml                     # Render.com deployment config
├── Procfile                        # Render.com process file
├── ngrok.yml                       # ngrok configuration
├── deploy.sh                       # Local deployment script
└── README.md                       # This file
```

### Adding New Templates

Edit `BREAKUP_TEMPLATES` in `breakup_generator_simple.py` to add new excuses:

```python
BREAKUP_TEMPLATES = {
    "your_style": [
        "Your template here with {name} placeholder",
        "Another template...",
    ],
    # ... existing styles
}
```

## Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Find and kill the process
   lsof -ti:8087 | xargs kill -9
   ```

2. **ngrok not working:**
   - Check your auth token in `ngrok.yml`
   - Ensure ngrok is installed and in your PATH

3. **Render deployment fails:**
   - Check the build logs
   - Ensure all dependencies are in `requirements.txt`
   - Verify the start command is correct

### Health Check

Test if your server is running:

```bash
curl http://localhost:8087/health
```

Should return:
```json
{
  "status": "healthy",
  "service": "AI Breakup Excuse Generator",
  "timestamp": "2024-01-01T12:00:00",
  "auth_token": "breakup-excuse-token-2024",
  "total_templates": 150
}
```

## License

MIT License - Feel free to use this for your hackathon projects!

## Contributing

1. Fork the repository
2. Add your creative breakup excuses
3. Submit a pull request

---

Made with ❤️ for the Puch AI hackathon! 🚀
