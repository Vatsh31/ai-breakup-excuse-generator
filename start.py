#!/usr/bin/env python3
"""
Cloud-ready startup script for AI Breakup Excuse Generator
Handles environment variables and cloud platform requirements
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Main startup function with cloud deployment support"""
    
    # Cloud deployment configuration
    port = int(os.environ.get("PORT", 8087))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"🚀 Starting AI Breakup Excuse Generator...")
    print(f"🌐 Host: {host}")
    print(f"🔌 Port: {port}")
    print(f"🔑 Auth Token: {os.environ.get('AUTH_TOKEN', 'breakup-excuse-token-2024')}")
    
    # Change to the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mcp_dir = os.path.join(script_dir, "mcp-bearer-token")
    
    if os.path.exists(mcp_dir):
        os.chdir(mcp_dir)
        print(f"📁 Working directory: {os.getcwd()}")
    else:
        print(f"❌ MCP directory not found: {mcp_dir}")
        sys.exit(1)
    
    # Import and run the main application
    try:
        # Add current directory to Python path
        sys.path.insert(0, os.getcwd())
        
        # List files in current directory for debugging
        print(f"📂 Files in current directory: {os.listdir('.')}")
        
        # Try to import the module
        from breakup_generator_simple import main as app_main
        print("✅ Application imported successfully")
        
        # Run the async application
        asyncio.run(app_main())
        
    except ImportError as e:
        print(f"❌ Failed to import application: {e}")
        print(f"💡 Current working directory: {os.getcwd()}")
        print(f"💡 Python path: {sys.path}")
        print("💡 Make sure all dependencies are installed: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Application failed to start: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 