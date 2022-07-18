import os
from dotenv import load_dotenv
import discord
from discord.ui import Button, View
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='{', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    await bot.change_presence(activity=discord.Game(name="Aide les nuls en informatique de ouf"))

@bot.command()
async def config(ctx):
    button = Button(label = "Link of the first config", url="https://gaetanjestin.com", style=discord.ButtonStyle.link)
    view = View()
    view.add_item(button)
    await ctx.send("Config !", view=view)


bot.run(TOKEN)