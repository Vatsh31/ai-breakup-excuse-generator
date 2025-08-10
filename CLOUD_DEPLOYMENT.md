# ☁️ Cloud Deployment Guide

This guide will help you deploy your AI Breakup Excuse Generator to various cloud platforms.

## 🚀 Quick Deploy to Render.com (Recommended)

### Step 1: Prepare Your Repository

1. **Push all files to GitHub:**
   ```bash
   git add .
   git commit -m "Add cloud deployment support"
   git push origin main
   ```

2. **Ensure these files are in your repository:**
   - `render.yaml` - Render.com configuration
   - `start.py` - Cloud startup script
   - `requirements.txt` - Python dependencies
   - `mcp-bearer-token/breakup_generator_simple.py` - Main application

### Step 2: Deploy on Render.com

1. **Go to [render.com](https://render.com)**
2. **Click "New +" → "Web Service"**
3. **Connect your GitHub repository**
4. **Render will auto-detect the configuration:**
   - **Name**: `ai-breakup-excuse-generator`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python start.py`
   - **Plan**: `Free`

5. **Click "Create Web Service"**

### Step 3: Get Your URL

- Render will provide a URL like: `https://ai-breakup-excuse-generator.onrender.com`
- Your MCP connection string will be:
  ```
  /mcp connect https://ai-breakup-excuse-generator.onrender.com/mcp breakup-excuse-token-2024
  ```

## 🌐 Alternative Cloud Platforms

### Railway.app

1. **Go to [railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Railway will auto-detect Python**
4. **Set environment variables:**
   - `AUTH_TOKEN`: `breakup-excuse-token-2024`
   - `MY_NUMBER`: `919876543210`
5. **Deploy!**

### Heroku

1. **Install Heroku CLI**
2. **Create `Procfile`** (already created)
3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### DigitalOcean App Platform

1. **Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)**
2. **Connect your GitHub repository**
3. **Configure as Python app**
4. **Set environment variables**
5. **Deploy!**

## 🔧 Environment Variables

All cloud platforms will automatically set the `PORT` environment variable. Your app is configured to use:

- `PORT` - Automatically set by cloud platform
- `HOST` - Set to `0.0.0.0` for cloud deployment
- `AUTH_TOKEN` - Your authentication token
- `MY_NUMBER` - Phone number for validation

## 📊 Monitoring Your Deployment

### Health Check

Once deployed, test your app:

```bash
# Health check
curl https://your-app-url.com/health

# Root endpoint
curl https://your-app-url.com/
```

### Expected Response

```json
{
  "status": "healthy",
  "service": "AI Breakup Excuse Generator",
  "timestamp": "2024-01-01T12:00:00",
  "auth_token": "breakup-excuse-token-2024",
  "total_templates": 150
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Build Fails**
   - Check `requirements.txt` has all dependencies
   - Ensure Python version compatibility

2. **App Won't Start**
   - Check logs for import errors
   - Verify `start.py` is executable

3. **Port Issues**
   - Cloud platforms set `PORT` automatically
   - App binds to `0.0.0.0` for external access

4. **Health Check Fails**
   - Ensure `/health` endpoint is working
   - Check app is responding on the correct port

### Debug Commands

```bash
# Check if app is running
curl https://your-app-url.com/health

# Check logs (Render.com)
# Go to your app dashboard → Logs

# Test MCP endpoint
curl -X POST https://your-app-url.com/mcp \
  -H "Authorization: Bearer breakup-excuse-token-2024" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "tools/list", "id": 1}'
```

## 🔐 Security Notes

- **Auth Token**: Change the default token in production
- **Environment Variables**: Use platform secrets management
- **HTTPS**: All cloud platforms provide HTTPS automatically

## 📱 Connect to Puch AI

Once deployed, use this command in Puch AI:

```
/mcp connect https://your-app-url.com/mcp breakup-excuse-token-2024
```

## 🎯 Production Checklist

- [ ] App deploys successfully
- [ ] Health check endpoint responds
- [ ] MCP endpoint is accessible
- [ ] Environment variables are set
- [ ] HTTPS is enabled
- [ ] Can connect from Puch AI

## 🚀 Next Steps

1. **Deploy to your chosen platform**
2. **Test the health check endpoint**
3. **Connect to Puch AI**
4. **Share your MCP server!**

---

**Your AI Breakup Excuse Generator is now cloud-ready! ☁️🚀** 