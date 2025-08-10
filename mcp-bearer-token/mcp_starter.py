import os
import random
from typing import Annotated
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import Field
from mcp.server.fastapi import MCP
from mcp import tool
from dotenv import load_dotenv

# Load .env
load_dotenv()

AUTH_TOKEN = os.getenv("AUTH_TOKEN", "changeme")

app = FastAPI()
mcp = MCP(app, auth_type="bearer", bearer_token=AUTH_TOKEN)

@tool(description="Generate a weird AI breakup excuse")
async def breakup_excuse_generator(
    partner_name: Annotated[str, Field(description="Name of the person you are breaking up with")],
    style: Annotated[str, Field(description="Style of excuse: dramatic, funny, sci-fi, poetic")]
) -> str:
    templates = {
        "dramatic": [
            f"{partner_name}, our love burns too bright and must extinguish before it consumes the world.",
            f"{partner_name}, you are the storm… and I am but a fragile paper boat."
        ],
        "funny": [
            f"{partner_name}, it’s not you… it’s me and my obsession with competitive cheese rolling.",
            f"{partner_name}, I can’t be with someone who doesn’t alphabetize their cereal boxes."
        ],
        "sci-fi": [
            f"{partner_name}, the Galactic Council forbids our union across star systems.",
            f"{partner_name}, my spaceship departs in 5 minutes and they don’t allow emotional baggage."
        ],
        "poetic": [
            f"{partner_name}, like the tide from the shore, I must drift away.",
            f"{partner_name}, the moon has called my name and I must follow."
        ]
    }
    return random.choice(templates.get(style.lower(), templates["funny"]))

mcp.register_tool(breakup_excuse_generator)

@app.get("/")
async def root():
    return {"status": "MCP Breakup Excuse Generator is running 🚀"}
