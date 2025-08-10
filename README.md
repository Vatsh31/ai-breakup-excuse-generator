# 💔 AI Breakup Excuse Generator - Puch AI Hackathon

A viral-worthy MCP server that generates wildly over-the-top, weird, and funny excuses to end relationships. Perfect for the Puch AI hackathon with **189 unique templates** across 7 different styles!

## 🚀 Features

- **189 Unique Templates** - Massive variety ensures users rarely see the same excuse twice
- **7 Creative Styles**: dramatic, funny, sci-fi, poetic, absurd, viral, trending
- **Viral Potential** - Each excuse is designed to be screenshot and shared on social media
- **Easy to Use** - Just 2 inputs: name + style
- **Perfect for Phase 1** - Weird enough for creativity points!

## 🎯 Why This Works

- **Viral Factor** – People will screenshot & share
- **Easy to Try** – Only 2 inputs required
- **Weird Enough** – Perfect for Phase 1 creativity points
- **Massive Variety** – 189 templates across 7 styles

## 📊 Template Breakdown

| Style | Templates | Description |
|-------|-----------|-------------|
| **Dramatic** | 20 | Epic, theatrical excuses |
| **Funny** | 27 | Absurd, hilarious reasons |
| **Sci-fi** | 25 | Space, aliens, time travel |
| **Poetic** | 25 | Romantic but ending |
| **Absurd** | 25 | Completely ridiculous |
| **Viral** | 25 | Social media focused |
| **Trending** | 25 | Current lifestyle trends |

## 🛠️ Quick Setup

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd mcp-starter
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
pip install fastmcp fastapi uvicorn python-dotenv
```

### 2. Run the Server
```bash
cd mcp-bearer-token
python breakup_generator_simple.py
```

### 3. Make it Public (Required by Puch)
```bash
ngrok http 8087
```

### 4. Connect to Puch AI
```
/mcp connect https://your-ngrok-url.ngrok.app/mcp 95653634309vatshchheda312004
```

## 📱 Usage Examples

### Connect to Puch AI
```
/mcp connect https://your-domain.ngrok.app/mcp 95653634309vatshchheda312004
```

### Generate Excuses
```
"Generate a dramatic breakup excuse for Alex"
"Create a funny breakup excuse for Sarah"
"Give me a trending breakup excuse for Mike"
"Show me a sci-fi breakup excuse for Emma"
```

## 🎭 Sample Excuses

### Dramatic
> "💔 Alex, our love burns too bright and must extinguish before it consumes the world. I cannot bear to watch us both turn to ash."

### Funny
> "😂 Sarah, it's not you… it's me and my obsession with competitive cheese rolling. I can't be with someone who doesn't understand the art of dairy athletics."

### Sci-fi
> "🚀 Mike, the Galactic Council forbids our union across star systems. I received the transmission this morning."

### Viral
> "📱 Emma, I just got 10,000 followers on TikTok for my 'single life' content. My followers say you're holding me back from my true potential."

## 🔧 Technical Details

- **Framework**: FastMCP 2.11.2
- **Language**: Python 3.11+
- **Port**: 8087
- **Auth**: Bearer Token
- **Templates**: 189 unique excuses
- **Styles**: 7 different categories

## 📁 Project Structure

```
mcp-starter/
├── mcp-bearer-token/
│   ├── breakup_generator_simple.py    # Main AI Breakup Excuse Generator
│   ├── mcp_starter.py                 # Original starter
│   └── puch-user-id-mcp-example.py   # Task management example
├── mcp-google-oauth/                  # Google OAuth example
├── mcp-oauth-github/                  # GitHub OAuth example
└── README.md
```

## 🎯 Perfect for Puch AI Hackathon

This project is specifically designed for the **Puch AI hackathon** with:

- ✅ **Viral Potential** - Designed for social media sharing
- ✅ **Easy to Use** - Simple 2-input interface
- ✅ **Creative & Weird** - Perfect for Phase 1 creativity points
- ✅ **Massive Variety** - 189 templates ensure uniqueness
- ✅ **MCP Ready** - Fully compatible with Puch AI

## 🚀 Deployment Options

### Option 1: ngrok (Quick & Easy)
```bash
ngrok http 8087
```

### Option 2: Cloud Deployment
- Railway
- Render
- Heroku
- DigitalOcean App Platform

## 📞 Support

- **Puch AI Discord**: https://discord.gg/VMCnMvYx
- **Puch AI MCP docs**: https://puch.ai/mcp
- **Puch WhatsApp**: +91 99988 81729

## 🏆 Hackathon Ready!

This AI Breakup Excuse Generator is perfect for the Puch AI hackathon because:

1. **Viral Factor** – People will screenshot & share
2. **Easy to Try** – Only 2 inputs required
3. **Weird Enough** – Perfect for Phase 1 creativity points
4. **Massive Variety** – 189 templates across 7 styles
5. **Social Media Ready** – Designed for sharing and engagement

---

**Happy coding! 🚀**

Use the hashtag `#BuildWithPuch` in your posts about your MCP!

---

*This starter makes it super easy to create your own MCP server for Puch AI. Just follow the setup steps and you'll be ready to extend Puch with your custom tools!*
