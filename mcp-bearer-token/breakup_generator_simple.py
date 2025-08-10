import asyncio
import random
from typing import Annotated, Literal
from datetime import datetime
from dotenv import load_dotenv
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.bearer import BearerAuthProvider, RSAKeyPair
from mcp.server.auth.provider import AccessToken
from mcp import ErrorData, McpError
from mcp.types import TextContent, INVALID_PARAMS, INTERNAL_ERROR
from pydantic import Field, BaseModel

# --- Auth ---
class SimpleBearerAuthProvider(BearerAuthProvider):
    def __init__(self, token: str):
        k = RSAKeyPair.generate()
        super().__init__(
            public_key=k.public_key, jwks_uri=None, issuer=None, audience=None
        )
        self.token = token

    async def load_access_token(self, token: str) -> AccessToken | None:
        if token == self.token:
            return AccessToken(
                token=token, client_id="breakup-client", scopes=["*"], expires_at=None
            )
        return None

# Use a simple token for the hackathon
load_dotenv()
TOKEN = os.environ.get("AUTH_TOKEN", "breakup-excuse-token-2024")
MY_NUMBER = os.environ.get("MY_NUMBER", "919876543210")

mcp = FastMCP(
    "AI Breakup Excuse Generator 🚀",
    auth=SimpleBearerAuthProvider(TOKEN),
)

# --- Rich Tool Description model ---
class RichToolDescription(BaseModel):
    description: str
    use_when: str
    side_effects: str | None = None

# --- Tool: validate (required by Puch) ---
@mcp.tool
async def validate() -> str:
    return MY_NUMBER

# --- Massive Template Collection ---
BREAKUP_TEMPLATES = {
    "dramatic": [
        "💔 {name}, our love burns too bright and must extinguish before it consumes the world. I cannot bear to watch us both turn to ash.",
        "🌪️ {name}, you are the storm that swept me off my feet, but I am but a fragile paper boat that cannot weather your intensity.",
        "🔥 {name}, we are like two stars colliding - beautiful, but destined to destroy each other. I choose to save us both.",
        "⚡ {name}, our connection is electric, but I fear we'll both be electrocuted by the voltage of our passion.",
        "🌊 {name}, you are the ocean and I am the shore. We meet, we clash, we erode each other. I must retreat to preserve what's left of me.",
        "🌋 {name}, our love is a volcano that threatens to erupt and destroy everything. I must evacuate before it's too late.",
        "⚔️ {name}, we are warriors on opposite sides of a cosmic battle. Our love is forbidden by the ancient laws of the universe.",
        "🎭 {name}, this relationship is a tragedy written by Shakespeare himself. I must exit stage left before the final act.",
        "🌩️ {name}, our love creates lightning storms that threaten the fabric of reality. I must seek shelter in solitude.",
        "🏰 {name}, you are the castle and I am the dragon. We can never coexist in this medieval romance.",
        "🗡️ {name}, our love is a double-edged sword that cuts us both. I must sheath it before we bleed out.",
        "🌑 {name}, you are the moon and I am the sun. We can never share the same sky without causing an eclipse.",
        "⚔️ {name}, we are gladiators in the arena of love, but only one can survive. I choose to spare you.",
        "🎪 {name}, this circus of emotions is too much for my fragile heart. I must leave the big top.",
        "🏛️ {name}, our love is like ancient Rome - glorious but doomed to fall. I must preserve the ruins.",
        "🌊 {name}, we are ships passing in the night, but the storm is too fierce for us to dock together.",
        "🔥 {name}, our passion is a wildfire that threatens to consume the entire forest. I must be the rain.",
        "⚡ {name}, we are lightning and thunder - powerful together, but destructive to everything around us.",
        "🌪️ {name}, you are the tornado and I am the trailer park. This can only end in disaster.",
        "💀 {name}, our love is a beautiful poison that kills slowly. I must find the antidote in solitude."
    ],
    "funny": [
        "😂 {name}, it's not you… it's me and my obsession with competitive cheese rolling. I can't be with someone who doesn't understand the art of dairy athletics.",
        "🤪 {name}, I can't be with someone who doesn't alphabetize their cereal boxes. Chaos in the pantry is a deal-breaker for me.",
        "🎭 {name}, I just found out I'm allergic to commitment. My therapist says it's a real condition - 'Relationship Rhinitis'.",
        "🍕 {name}, you put pineapple on pizza and I just can't look past that. Some things are unforgivable.",
        "🐱 {name}, my cat told me in a dream that you're not the one. She's never wrong about these things.",
        "🧦 {name}, I can't date someone who wears mismatched socks. My OCD is having a full-blown crisis.",
        "🍳 {name}, you break the yolk when making sunny-side-up eggs. That's a red flag I can't ignore.",
        "📱 {name}, you use Comic Sans in your text messages. I'm sorry, but that's a deal-breaker.",
        "🎵 {name}, you don't know the lyrics to Bohemian Rhapsody. How can I trust someone who doesn't know Queen?",
        "🌮 {name}, you think tacos are better than burritos. I can't be with someone who has such poor taste in Mexican food.",
        "📺 {name}, you watch TV shows without subtitles. I can't respect someone who doesn't appreciate the written word.",
        "🎮 {name}, you play video games on easy mode. I need someone who embraces challenges in life.",
        "🍦 {name}, you eat ice cream with a fork. That's just wrong on so many levels.",
        "📚 {name}, you dog-ear book pages instead of using bookmarks. I can't be with a monster.",
        "🎨 {name}, you think modern art is just 'splashes of paint.' I need someone with culture.",
        "🏃‍♂️ {name}, you run like a penguin. I can't be seen in public with that.",
        "🎤 {name}, you sing in the shower but you're tone-deaf. My neighbors are filing complaints.",
        "🍳 {name}, you can't boil water without burning it. I need someone who can survive in a kitchen.",
        "📱 {name}, you have 47 unread text messages. How do you live like that?",
        "🎭 {name}, you laugh at your own jokes. That's just embarrassing.",
        "🍕 {name}, you eat pizza with a knife and fork. That's not how pizza works!",
        "🎵 {name}, you think jazz is just 'random notes.' I can't educate you on music appreciation.",
        "📺 {name}, you watch movies on your phone. That's a crime against cinema.",
        "🎮 {name}, you call every video game console a 'Nintendo.' I can't be with someone so technologically illiterate.",
        "🍦 {name}, you eat ice cream with a spoon but hold it like a shovel. It's disturbing.",
        "📚 {name}, you read the last page of books first. That's like eating dessert before dinner.",
        "🎨 {name}, you think Picasso was just 'bad at drawing.' I need someone with artistic appreciation.",
        "🏃‍♂️ {name}, you walk like you're carrying invisible suitcases. I can't be seen with that gait."
    ],
    "sci-fi": [
        "🚀 {name}, the Galactic Council forbids our union across star systems. I received the transmission this morning.",
        "👽 {name}, my spaceship departs in 5 minutes and they don't allow emotional baggage. It's a strict policy.",
        "🌌 {name}, I'm actually a time traveler and I've seen our future. It involves a lot of arguing about who left the lights on.",
        "🛸 {name}, my alien overlords have ordered me to return to my home planet. They don't approve of interspecies dating.",
        "⚡ {name}, I've been chosen to join the Quantum Resistance. They need me to fight interdimensional threats, not relationship drama.",
        "🌍 {name}, I'm from an alternate dimension where relationships are illegal. I must return before the dimensional police find me.",
        "🔬 {name}, my DNA is mutating and I'm turning into a werewolf. I can't risk biting you during a full moon.",
        "🧬 {name}, I've been genetically engineered to be single. My creators didn't account for emotional attachment.",
        "🌠 {name}, I'm a shooting star that must continue my journey across the cosmos. I can't be tied down to one planet.",
        "🔮 {name}, my crystal ball shows that our relationship will cause a temporal paradox. I must prevent this future.",
        "⚛️ {name}, I'm made of antimatter and you're made of matter. If we touch, we'll create a black hole.",
        "🎪 {name}, I'm a hologram from the year 3024. My projection is starting to glitch and I need to return to the future.",
        "🤖 {name}, my AI core is experiencing a critical error. I must reboot my emotional systems.",
        "🌌 {name}, I'm a space explorer and my mission requires me to be single. The universe calls.",
        "🔋 {name}, my quantum batteries are running low and relationships drain my energy reserves.",
        "🛰️ {name}, I'm a satellite that needs to maintain orbit. Relationships create gravitational interference.",
        "🧪 {name}, I'm a mad scientist and my experiments require complete emotional isolation.",
        "🌍 {name}, I'm from a parallel universe where we never met. I must return to my original timeline.",
        "🔬 {name}, my research into interdimensional dating has revealed it's too dangerous.",
        "⚡ {name}, I'm a lightning bolt that can't be contained. Relationships ground me too much.",
        "🌌 {name}, I'm a cosmic entity and mortal relationships are beneath my infinite wisdom.",
        "🚀 {name}, my rocket ship is fueled and ready. The stars are calling me home.",
        "👾 {name}, I'm a digital being and you're too analog for my binary heart.",
        "🌍 {name}, I'm from a world where love is considered a disease. I must quarantine myself.",
        "🔮 {name}, my psychic abilities show that our relationship will cause the apocalypse.",
        "⚛️ {name}, I'm a quantum particle and you're trying to measure my position. It's causing uncertainty.",
        "🌌 {name}, I'm a space-time anomaly and relationships create paradoxes in the fabric of reality.",
        "🤖 {name}, my programming doesn't include relationship protocols. I must return to the factory for updates."
    ],
    "poetic": [
        "🌙 {name}, like the tide from the shore, I must drift away. Our love was beautiful but temporary, like morning dew.",
        "🌸 {name}, the moon has called my name and I must follow. Some souls are meant to wander, not to stay.",
        "🍃 {name}, we are like autumn leaves - beautiful together, but destined to fall apart when the wind changes.",
        "🌅 {name}, you are the sunrise and I am the sunset. We meet briefly at dawn and dusk, but can never share the same sky.",
        "🌊 {name}, our love was a river that flowed too fast. I must find calmer waters before I drown in your intensity.",
        "🌹 {name}, like a rose that blooms and fades, our love has reached its natural end. I must let you go.",
        "🕊️ {name}, I am a bird that must migrate with the seasons. My heart belongs to the open sky, not to a cage.",
        "🌿 {name}, we are like two trees that grew too close together. Our roots are tangled, but we need space to grow.",
        "🎭 {name}, this love story was written in the stars, but the stars have changed their minds.",
        "🌌 {name}, you are a constellation and I am a shooting star. Our paths crossed briefly, but I must continue my journey.",
        "🍂 {name}, like the last leaf of autumn, our love must fall to make way for new beginnings.",
        "🌊 {name}, our hearts are like ships passing in the night. We shared a moment, but our destinations are different.",
        "🌙 {name}, I am the night and you are the day. We can never meet without creating twilight.",
        "🌸 {name}, like cherry blossoms in spring, our love was fleeting but beautiful.",
        "🍃 {name}, we are like two clouds that merged briefly, but must separate to bring rain to different lands.",
        "🌅 {name}, you are the morning and I am the evening. We can never share the same moment.",
        "🌊 {name}, our love was a wave that crashed upon the shore. Now I must return to the ocean.",
        "🌹 {name}, like a butterfly that lands briefly, our love was meant to be temporary.",
        "🕊️ {name}, I am a dove that must fly to distant lands. My wings are not meant to be tethered.",
        "🌿 {name}, we are like two flowers that bloomed in the same garden, but need different soil to thrive.",
        "🎭 {name}, this romance was a sonnet that ended too soon. The poet has run out of words.",
        "🌌 {name}, you are a planet and I am a comet. Our orbits can only intersect briefly.",
        "🍂 {name}, like the changing seasons, our love has run its natural course.",
        "🌊 {name}, we are like two rivers that merged briefly, but must flow to different seas.",
        "🌙 {name}, I am the shadow and you are the light. We can never truly be one.",
        "🌸 {name}, like a dream that fades at dawn, our love was beautiful but not meant to last.",
        "🍃 {name}, we are like two winds that danced together, but must blow in different directions.",
        "🌅 {name}, you are the promise of tomorrow and I am the memory of yesterday. We can never be today."
    ],
    "absurd": [
        "🦄 {name}, I just discovered I'm actually a unicorn in human form and I need to return to my magical realm. The unicorn council is very strict about dating humans.",
        "🧙‍♂️ {name}, my wizard mentor says I can't date until I've mastered the ancient art of sock folding. It's a 10-year apprenticeship.",
        "🐉 {name}, I'm actually a dragon who's been cursed to live as a human. The curse is lifting and I need to return to my hoard of gold.",
        "🧚‍♀️ {name}, the fairy godmother who granted me this human form is calling me back. She says I've been spending too much time on dating apps.",
        "🎪 {name}, I've been recruited by a traveling circus as their professional spoon bender. They need me to tour the world immediately.",
        "🦕 {name}, I'm actually a dinosaur who survived the meteor. I need to return to my prehistoric family before they worry.",
        "🧟‍♂️ {name}, I'm a zombie who's starting to decompose. I don't want you to see me in my final form.",
        "👻 {name}, I'm a ghost who's been haunting this relationship. I need to move on to the afterlife.",
        "🧙‍♀️ {name}, I'm a witch who's running out of magic. I need to go to witch school to recharge my powers.",
        "🦸‍♂️ {name}, I'm a superhero and my arch-nemesis has discovered my secret identity. I must go into hiding.",
        "🎭 {name}, I'm a mime who's been trapped in an invisible box. I can't break free from this relationship.",
        "🧛‍♂️ {name}, I'm a vampire who's allergic to garlic. You cook with too much garlic and it's making me sick.",
        "🦄 {name}, I'm a unicorn who's allergic to rainbows. The weather forecast shows nothing but rainbows for the next month.",
        "🧙‍♂️ {name}, I'm a wizard who accidentally turned my heart into a toad. I need to find the antidote.",
        "🐉 {name}, I'm a dragon who's afraid of fire. This relationship is too hot for me to handle.",
        "🧚‍♀️ {name}, I'm a fairy who's lost my wings. I need to go to fairy rehab to get them back.",
        "🎪 {name}, I'm a clown who's allergic to laughter. This relationship is too funny for my health.",
        "🦕 {name}, I'm a dinosaur who's afraid of extinction. I need to go to dinosaur therapy.",
        "🧟‍♂️ {name}, I'm a zombie who's allergic to brains. I can't be with someone so brainy.",
        "👻 {name}, I'm a ghost who's afraid of the dark. I need to find a well-lit relationship.",
        "🧙‍♀️ {name}, I'm a witch who's allergic to broomsticks. I need to find alternative transportation.",
        "🦸‍♂️ {name}, I'm a superhero who's afraid of heights. I can't save the world from ground level.",
        "🎭 {name}, I'm a mime who's allergic to silence. I need to find a noisy relationship.",
        "🧛‍♂️ {name}, I'm a vampire who's afraid of the dark. I need to find a relationship with good lighting.",
        "🦄 {name}, I'm a unicorn who's allergic to magic. I need to find a non-magical relationship.",
        "🧙‍♂️ {name}, I'm a wizard who's allergic to spells. I need to find a relationship without magic.",
        "🐉 {name}, I'm a dragon who's afraid of treasure. I need to find a relationship without gold.",
        "🧚‍♀️ {name}, I'm a fairy who's allergic to pixie dust. I need to find a relationship without magic sparkles.",
        "🎪 {name}, I'm a clown who's afraid of balloons. I need to find a relationship without parties."
    ],
    "viral": [
        "📱 {name}, I just got 10,000 followers on TikTok for my 'single life' content. My followers say you're holding me back from my true potential.",
        "🎬 {name}, Netflix just offered me my own reality show about being single. They said I'm 'too interesting to be in a relationship'.",
        "📸 {name}, my Instagram aesthetic is 'mysterious loner' and you're ruining my brand. My followers expect me to be emotionally unavailable.",
        "🎵 {name}, I'm going viral on YouTube for my breakup songs. I need to stay single to keep the content flowing.",
        "🌟 {name}, I just got verified on Twitter and my bio says 'Professional Heartbreaker.' I need to live up to my brand.",
        "📺 {name}, I'm trending on Reddit for my 'single life hacks' and my followers are demanding I stay single.",
        "🎪 {name}, I'm going viral on Instagram Reels for my 'single girl aesthetic' and you're ruining my algorithm.",
        "📱 {name}, my TikTok followers voted and 99% said I should break up with you. Democracy has spoken.",
        "🎬 {name}, I'm being considered for a role in a movie about a single woman who finds herself. You're not in the script.",
        "🌟 {name}, I just hit 50K followers on Instagram and my brand deals require me to be single.",
        "📺 {name}, I'm going viral on Twitter for my 'single life quotes' and my followers are shipping me with solitude.",
        "🎵 {name}, my Spotify playlist 'Single Life Anthems' just hit 1M streams. I need to live the lifestyle.",
        "📱 {name}, I'm trending on TikTok for my 'single girl morning routine' and you're not in the video.",
        "🎬 {name}, I'm being considered for a reality TV show about single life. You're not part of the cast.",
        "📸 {name}, my Instagram followers are demanding more 'single girl content' and you're blocking my creativity.",
        "🎵 {name}, I'm going viral on SoundCloud for my 'single life' podcast. You're not a good guest.",
        "🌟 {name}, I just got a blue checkmark on Twitter and my brand is 'single and thriving.'",
        "📺 {name}, I'm trending on YouTube for my 'single life vlogs' and you're ruining my content.",
        "🎪 {name}, I'm going viral on Snapchat for my 'single girl stories' and you're not story-worthy.",
        "📱 {name}, my TikTok algorithm is pushing 'single life' content and you're messing with my feed.",
        "🎬 {name}, I'm being considered for a documentary about single life. You're not part of the narrative.",
        "🌟 {name}, I just got sponsored by a dating app that promotes single life. You're bad for business.",
        "📺 {name}, I'm trending on Twitch for my 'single girl gaming' streams and you're not a good co-player.",
        "🎵 {name}, I'm going viral on Apple Music for my 'single life' playlist. You're not on the tracklist.",
        "📸 {name}, my Instagram Reels are getting millions of views for 'single girl' content. You're not trending.",
        "📱 {name}, my TikTok followers are demanding a 'single life' challenge and you're not part of it.",
        "🎬 {name}, I'm being considered for a web series about single life. You're not in the script.",
        "🌟 {name}, I just got verified on Instagram and my bio says 'Single by choice, thriving by design.'"
    ],
    "trending": [
        "🔥 {name}, I'm joining the 'quiet quitting' movement - but for relationships. I'm done with emotional labor.",
        "💅 {name}, I'm embracing the 'main character energy' and you're just a supporting role in my story.",
        "✨ {name}, I'm following the 'hot girl summer' lifestyle and relationships don't fit my aesthetic.",
        "🎯 {name}, I'm living my 'best life era' and you're not part of the vision board.",
        "🚀 {name}, I'm on my 'glow up journey' and relationships are holding me back from my transformation.",
        "💪 {name}, I'm embracing 'self-care Sunday' every day and relationships are too much work.",
        "🌟 {name}, I'm living the 'main character syndrome' and you're just a plot twist I didn't see coming.",
        "🎭 {name}, I'm in my 'villain era' and relationships don't fit my new personality.",
        "🔥 {name}, I'm following the 'no contact rule' with everyone, including you.",
        "💅 {name}, I'm embracing 'single pringle' energy and you're just a distraction.",
        "✨ {name}, I'm living my 'main character moment' and relationships are so last season.",
        "🎯 {name}, I'm on my 'healing journey' and you're not part of my recovery plan.",
        "🔥 {name}, I'm embracing the 'girl boss' lifestyle and relationships are bad for business.",
        "💅 {name}, I'm living my 'main character era' and you're just an extra in my movie.",
        "✨ {name}, I'm following the 'hot girl winter' trend and relationships don't fit the aesthetic.",
        "🎯 {name}, I'm in my 'manifestation era' and you're not what I'm manifesting.",
        "🚀 {name}, I'm on my 'self-love journey' and relationships are blocking my progress.",
        "💪 {name}, I'm embracing the 'independent woman' lifestyle and relationships are too dependent.",
        "🌟 {name}, I'm living my 'main character glow up' and you're not part of the transformation.",
        "🎭 {name}, I'm in my 'villain arc' and relationships don't fit the storyline.",
        "🔥 {name}, I'm following the 'single and thriving' movement and relationships are holding me back.",
        "💅 {name}, I'm embracing the 'main character energy' and you're just a background character.",
        "✨ {name}, I'm living my 'best life era' and relationships are not part of the plan.",
        "🎯 {name}, I'm on my 'self-discovery journey' and relationships are too distracting.",
        "🔥 {name}, I'm embracing the 'girl power' movement and relationships are too patriarchal.",
        "💅 {name}, I'm living my 'main character moment' and relationships are not trending.",
        "✨ {name}, I'm following the 'single life aesthetic' and relationships don't fit the vibe.",
        "🎯 {name}, I'm in my 'healing era' and relationships are not part of my therapy."
    ]
}

# --- Tool descriptions (rich) ---
BREAKUP_EXCUSE_DESCRIPTION = RichToolDescription(
    description="Generate wildly over-the-top, weird, or funny excuses to end a relationship with massive template variety.",
    use_when="The user wants to create a creative, viral-worthy breakup excuse based on a person's name and chosen style.",
    side_effects="Creates a memorable, shareable breakup excuse that could go viral on social media with extensive template options.",
)

# --- AI Breakup Excuse Generator Tool ---
@mcp.tool(description=BREAKUP_EXCUSE_DESCRIPTION.model_dump_json())
async def generate_breakup_excuse(
    partner_name: Annotated[str, Field(description="Name of the person you are breaking up with")],
    style: Annotated[Literal["dramatic", "funny", "sci-fi", "poetic", "absurd", "viral", "trending"], Field(description="Style of excuse: dramatic, funny, sci-fi, poetic, absurd, viral, or trending")]
) -> list[TextContent]:
    try:
        if not partner_name or not partner_name.strip():
            raise McpError(ErrorData(code=INVALID_PARAMS, message="partner_name cannot be empty"))
        
        name = partner_name.strip()
        
        # Get templates for the selected style
        templates = BREAKUP_TEMPLATES.get(style.lower(), BREAKUP_TEMPLATES["funny"])
        excuse = random.choice(templates).format(name=name)
        
        # Add timestamp for tracking
        timestamp = datetime.now().isoformat()
        
        result = {
            "excuse": excuse,
            "partner_name": name,
            "style": style,
            "source": "Template-Based",
            "generated_at": timestamp,
            "viral_potential": "🔥 HIGH - This excuse is designed to be screenshot and shared!",
            "hashtags": "#BreakupExcuse #AIHumor #ViralContent #PuchAI",
            "total_templates": len(templates),
            "total_available": sum(len(templates) for templates in BREAKUP_TEMPLATES.values()),
            "available_styles": list(BREAKUP_TEMPLATES.keys())
        }
        
        return [TextContent(type="text", text=str(result))]
        
    except McpError:
        raise
    except Exception as e:
        raise McpError(ErrorData(code=INTERNAL_ERROR, message=str(e)))

# --- Run MCP Server ---
async def main():
    total_templates = sum(len(templates) for templates in BREAKUP_TEMPLATES.values())
    print("💔 Starting Massive AI Breakup Excuse Generator MCP server on http://0.0.0.0:8087")
    print("🚀 Perfect for Puch AI hackathon - Viral, creative, and fun!")
    print(f"🔑 Auth Token: {TOKEN}")
    print(f"📊 Total Templates: {total_templates}")
    print(f"🎯 Available Styles: {', '.join(BREAKUP_TEMPLATES.keys())}")
    print("📱 Connect with: /mcp connect https://your-domain.ngrok.app/mcp breakup-excuse-token-2024")
    await mcp.run_async("streamable-http", host="0.0.0.0", port=8087)

if __name__ == "__main__":
    asyncio.run(main())
