import discord
import lib.EventHandler as e
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True

client = e.EventHandler(intents=intents)
client.run(TOKEN)
