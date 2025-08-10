#!/usr/bin/env python3
"""
Direct startup script for AI Breakup Excuse Generator
Runs the MCP server directly without complex imports
"""

import os
import sys
import asyncio
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Main startup function with direct execution"""
    
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
        
        # List files for debugging
        print(f"📂 Files in directory: {os.listdir('.')}")
        
        # Check if the main file exists
        main_file = "breakup_generator_simple.py"
        if not os.path.exists(main_file):
            print(f"❌ Main file not found: {main_file}")
            sys.exit(1)
        
        # Run the Python file directly
        print(f"✅ Running {main_file} directly...")
        result = subprocess.run([sys.executable, main_file], 
                              cwd=os.getcwd(),
                              env=os.environ.copy())
        
        if result.returncode != 0:
            print(f"❌ Application exited with code: {result.returncode}")
            sys.exit(result.returncode)
            
    else:
        print(f"❌ MCP directory not found: {mcp_dir}")
        sys.exit(1)

if __name__ == "__main__":
    main()
