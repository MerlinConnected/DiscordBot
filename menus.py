import os
from dotenv import load_dotenv
import discord
from discord.ui import Select, View
from discord.ext import commands, tasks

load_dotenv() # Load the .env file

TOKEN = os.getenv("DISCORD_TOKEN") # Get the token from the .env file

bot = commands.Bot(command_prefix='{', intents=discord.Intents.all())

@bot.event 
async def on_ready(): 
    print(f"{bot.user.name} has connected to Discord!") # Prints "Bot has connected to Discord!"
    await bot.change_presence(activity=discord.Game(name="Je suis un sale connard qui marche pas")) # Change the bot's activity

@bot.command()
async def menus(ctx):
    budget = Select( 
        placeholder="Selectionnez votre budget",
        options=[
            discord.SelectOption(
                label="Petite faim",
                emoji="🍟", 
                description="De 800 à 1000€"),
            discord.SelectOption(
                label="Grosse faim", 
                emoji="🍔", 
                description="De 1000 à 1500€"),
            discord.SelectOption(
                label="Petage de bide", 
                emoji="🍗", 
                description="De 1500 à 2000€")
        ]
    )

    async def budget_callback(interaction):
        bot.data['budget'] = interaction.data["values"][0]
        await interaction.response.send_message(f"Ton budget a été pris en compte")
    
    usage = Select(
        placeholder="Selectionnez votre utilisation",
        options=[
            discord.SelectOption(
                label="Secretaire",
                emoji="📝",
                description="Bureautique simple"),
            discord.SelectOption(
                label="Gamer",
                emoji="🎮",
                description="Tout sauf fotrnite"),
            discord.SelectOption(
                label="Machine de travail",
                emoji="🔧",
                description="Besoin de fiabilitée")
            ]
        )

    async def usage_callback(interaction):
        bot.data['usage'] = interaction.data["values"][0]
        await interaction.response.send_message(f"Ton usage a été pris en compte")

    @tasks.loop(seconds=5)
    async def my_background_task():
        if len(bot.data) == 2 and bot.continue_to_check :
            channel = bot.get_channel(997278764994142248)
            await channel.send(f"Ton usage est {bot.data['usage']} avec un budget de type {bot.data['budget']}")
            bot.continue_to_check = False
        else : pass

    usage.callback = usage_callback
    budget.callback = budget_callback
    bot.continue_to_check = True
    bot.data = {}
    my_background_task.start()
    view = View()
    view.add_item(budget)
    view.add_item(usage)
    await ctx.send("Des configurations de pc mise à jour régulièrement pour vous !", view=view)

bot.run(TOKEN)
