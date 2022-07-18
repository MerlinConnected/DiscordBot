import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ui import Select, View
from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingPermissions

load_dotenv() # Load the .env file

TOKEN = os.getenv("DISCORD_TOKEN") # Get the token from the .env file

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=996907904324091944))
            self.synced = True
        print("Logged")
    
client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "commands", description="Affiche toute les commandes", guild=discord.Object(id=996907904324091944))
async def commands(interaction: discord.Interaction):
    await interaction.response.send_message(
    "\n/menus (Affiche menu des configs)"
    "\n/cmos (Montre comment faire un CMOS)"
    "\n/temp (Un tuto pour check les température)"
    "\n/xmp  (Activer l'xmp dans son bios)"
    "\n/key (Lien d'achat clé W10 Pro)",
    ephemeral=True
    )

@tree.command(name = "cmos", description="Comment faire un clear cmos et reset sa carte mère.", guild=discord.Object(id=996907904324091944))
async def cmos(interaction: discord.Interaction):
    await interaction.response.send_message(
    "Par ici le clear CMOS --> https://www.youtube.com/watch?v=Fc0HIDKC1U0",
    ephemeral=True
    )

@tree.command(name = "temperatures", description="Comment vérifier si les températures de ses composants sont acceptables.", guild=discord.Object(id=996907904324091944))
async def temp(interaction: discord.Interaction):
    await interaction.response.send_message(
    "Pour vérifier les températures de votre processeur :"
    "\n- Télécharger OCCT : https://www.ocbase.com/download"
    "\n- Fermer tous les programmes (Discord, Steam...)"
    "\n- Lancer OCCT "
    "\n- Aller dans l'onglet : 'Test' (colonne de gauche)"
    "\n- Sélectionner dans la partie planning des tests : 'CPU' "
    "\n- Définir la durée du test --> 15 minutes minimum (en cliquant sur le logo infini au dessus)"
    "\n- Tout laisser en auto et appuyer sur play "
    "\n- Une fois le test terminé, envoyez dans le salon discord un screen des températures de votre processeur qui se trouvent dans la partie 'Monitoring' (à droite)."
    "\nExemple ici: https://imgur.com/a/5oWKVfp",
    ephemeral=True
    )

@tree.command(name = "xmp", description="Comment activer l'xmp et tirer le maximum de notre RAM.", guild=discord.Object(id=996907904324091944))
async def xmp(interaction: discord.Interaction):
    await interaction.response.send_message(
    "Pour activer l'XMP --> https://www.youtube.com/watch?v=3t6J1EiHb_w",
    ephemeral=True
    )

@tree.command(name = "key", description="Ou trouver une clef windows à pas trop cher.", guild=discord.Object(id=996907904324091944))
async def key(interaction: discord.Interaction):
    await interaction.response.send_message(
    "Une clé d'activation Windows 10 Pro pas cher ? \nC'est par ici ! -->  https://bit.ly/3jUPNTP"
    "\nIl ne s'agit pas d'une livraison instantanée donc patiente le temps que le site t'envoie la clé par mail :slight_smile:",
    ephemeral=True
    )

@tree.command(name = "ddu", description="Désinstaller des pilotes graphiques proprement.", guild=discord.Object(id=996907904324091944))
async def ddu(interaction: discord.Interaction):
    await interaction.response.send_message(
    "Pour faire un ddu propre suit le tuto --> https://www.youtube.com/watch?v=0L2XpBGKUa4",
    ephemeral=True
    )

@tree.command(name = "userdiag", description="Faire un diagnostic poussé de sa machine.", guild=discord.Object(id=996907904324091944))
async def userdiag(interaction: discord.Interaction):
    await interaction.response.send_message(
    "Pour télécharger l'outil de diagnostique --> https://userdiag.com/",
    ephemeral=True
    )

@tree.command(name = "config", description="Trouver une configuration adapté à ses besoin.", guild=discord.Object(id=996907904324091944))
async def config(ctx):
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
        tree.data['budget'] = interaction.data["values"][0]
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
        tree.data['usage'] = interaction.data["values"][0]
        await interaction.response.send_message(f"Ton usage a été pris en compte")

    @tasks.loop(seconds=5)
    async def my_background_task():
        if len(tree.data) == 2 and tree.continue_to_check :
            channel = tree.get_channel(997278764994142248)
            await channel.send(f"Ton usage est {tree.data['usage']} avec un budget de type {tree.data['budget']}")
            tree.continue_to_check = False
        else : pass

    usage.callback = usage_callback
    budget.callback = budget_callback
    tree.continue_to_check = True
    tree.data = {}
    my_background_task.start()
    view = View()
    view.add_item(budget)
    view.add_item(usage)
    await ctx.send("Des configurations de pc mise à jour régulièrement pour vous !", view=view)


client.run(TOKEN)