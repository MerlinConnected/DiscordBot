import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ui import Select, View, Button
from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingPermissions

load_dotenv() # Load the .env file

TOKEN = os.getenv('DISCORD_TOKEN') # Get the token from the .env file

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=996907904324091944))
            self.synced = True
        print('Logged')
        await client.change_presence(activity=discord.Game(name="Je suis un gentil bot qui fonctionne"))

client = aclient()
tree = app_commands.CommandTree(client)

class MyView(View):
    @discord.ui.button(label='/cmos', emoji='⚙️')
    async def cmos_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            'Par ici le clear CMOS --> https://www.youtube.com/watch?v=Fc0HIDKC1U0',
            ephemeral=True
        )

    @discord.ui.button(label='/temp', emoji='🌡️')
    async def temp_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            'Pour vérifier les températures de votre processeur :'
            '\n- Télécharger OCCT : https://www.ocbase.com/download'
            '\n- Fermer tous les programmes (Discord, Steam...)'
            '\n- Lancer OCCT '
            '\n- Aller dans l\'onglet : "Test" (colonne de gauche)'
            '\n- Sélectionner dans la partie planning des tests : "CPU" '
            '\n- Définir la durée du test --> 15 minutes minimum (en cliquant sur le logo infini au dessus)'
            '\n- Tout laisser en auto et appuyer sur play '
            '\n- Une fois le test terminé, envoyez dans le salon discord un screen des températures de votre processeur qui se trouvent dans la partie "Monitoring" (à droite).'
            '\nExemple ici: https://imgur.com/a/5oWKVfp',
            ephemeral=True
        )

    @discord.ui.button(label='/xmp', emoji='💻')
    async def xmp_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            'Pour activer l\'XMP --> https://www.youtube.com/watch?v=3t6J1EiHb_w',
            ephemeral=True
        )

    @discord.ui.button(label='/key', emoji='🔑')
    async def key_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            'Une clé d\'activation Windows 10 Pro pas cher ? \nC\'est par ici ! -->  https://bit.ly/3jUPNTP'
            '\nIl ne s\'agit pas d\'une livraison instantanée donc patiente le temps que le site t\'envoie la clé par mail :slight_smile:',
            ephemeral=True
        )

    @discord.ui.button(label='/ddu', emoji='💾')
    async def ddu_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            'Pour faire un ddu propre suit le tuto --> https://www.youtube.com/watch?v=0L2XpBGKUa4',
            ephemeral=True
        )

    @discord.ui.button(label='/userdiag', emoji='🩺')
    async def userdiag_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            'Pour télécharger l\'outil de diagnostique --> https://userdiag.com/',
            ephemeral=True
        )

    @discord.ui.button(label='/ram', emoji='💾')
    async def ram_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            'Il existe deux types majeurs de gestion de canal mémoire :'
            '\n'
            '\n**Le Dual Channel :**'
            '\n> Il s\'agit de la technologie la plus répandue sur les cartes mère. Celle-ci met en place deux canaux d\'échange entre le processeur et la mémoire de ton pc. Il est donc plus adapté de faire fonctionner ta CM avec deux barrettes de ram ( 2x4, 2x8, 2x16, … ). À toi de te référer au manuel de ta carte mère pour savoir dans quels slots mettre les deux barrettes (souvent 2 et 4).'
            '\n'
            '\n**Le Quad Channel :**'
            '\n> Une technologie plus haut de gamme faisant fonctionner la CM avec quatre barrettes de ram ( 4x4, 4x8, 4x16, … ) mais n\'étant présente que sur certains sockets de carte mère ( 2066, TR4, … ).'
            '\n'
            '\nÀ toi de te renseigner sur ta carte mère afin de savoir si celle-ci fonctionne en Dual ou Quad Channel.',
            ephemeral=True
        )


@tree.command(name = 'commandes', description='Liste de toutes les commandes disponibles', guild=discord.Object(id=996907904324091944))
async def commandes(interaction: discord.Interaction):
    view = MyView()
    await interaction.response.send_message('Voici les commandes', view=view)


@tree.command(name = 'cmos', description='Comment faire un clear cmos et reset sa carte mère.', guild=discord.Object(id=996907904324091944))
async def cmos(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Par ici le clear CMOS --> https://www.youtube.com/watch?v=Fc0HIDKC1U0',
        ephemeral=True
    )

@tree.command(name = 'temperatures', description='Comment vérifier si les températures de ses composants sont acceptables.', guild=discord.Object(id=996907904324091944))
async def temp(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Pour vérifier les températures de votre processeur :'
        '\n- Télécharger OCCT : https://www.ocbase.com/download'
        '\n- Fermer tous les programmes (Discord, Steam...)'
        '\n- Lancer OCCT'
        '\n- Aller dans l\'onglet : "Test" (colonne de gauche)'
        '\n- Sélectionner dans la partie planning des tests : "CPU" '
        '\n- Définir la durée du test --> 15 minutes minimum (en cliquant sur le logo infini au dessus)'
        '\n- Tout laisser en auto et appuyer sur play '
        '\n- Une fois le test terminé, envoyez dans le salon discord un screen des températures de votre processeur qui se trouvent dans la partie "Monitoring" (à droite).'
        '\nExemple ici: https://imgur.com/a/5oWKVfp',
        ephemeral=True
    )

@tree.command(name = 'xmp', description='Comment activer l\'xmp et tirer le maximum de notre RAM.', guild=discord.Object(id=996907904324091944))
async def xmp(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Pour activer l\'XMP --> https://www.youtube.com/watch?v=3t6J1EiHb_w',
        ephemeral=True
    )

@tree.command(name = 'key', description='Ou trouver une clef windows à pas trop cher.', guild=discord.Object(id=996907904324091944))
async def key(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Une clé d\'activation Windows 10 Pro pas cher ? \nC\'est par ici ! -->  https://bit.ly/3jUPNTP'
        '\nIl ne s\'agit pas d\'une livraison instantanée donc patiente le temps que le site t\'envoie la clé par mail :slight_smile:',
        ephemeral=True
    )

@tree.command(name = 'ddu', description='Désinstaller des pilotes graphiques proprement.', guild=discord.Object(id=996907904324091944))
async def ddu(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Pour faire un ddu propre suit le tuto --> https://www.youtube.com/watch?v=0L2XpBGKUa4',
        ephemeral=True
    )

@tree.command(name = 'diagnostic', description='Faire un diagnostic poussé de sa machine.', guild=discord.Object(id=996907904324091944))
async def diagnostic(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Pour télécharger l\'outil de diagnostique --> https://userdiag.com/',
        ephemeral=True
    )

@tree.command(name = 'ram', description='Explication du dual channel entre autres.', guild=discord.Object(id=996907904324091944))
async def ram(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Il existe deux types majeurs de gestion de canal mémoire :'
        '\n'
        '\n**Le Dual Channel :**'
        '\n> Il s\'agit de la technologie la plus répandue sur les cartes mère. Celle-ci met en place deux canaux d\'échange entre le processeur et la mémoire de ton pc. Il est donc plus adapté de faire fonctionner ta CM avec deux barrettes de ram ( 2x4, 2x8, 2x16, … ). À toi de te référer au manuel de ta carte mère pour savoir dans quels slots mettre les deux barrettes (souvent 2 et 4).'
        '\n'
        '\n**Le Quad Channel :**'
        '\n> Une technologie plus haut de gamme faisant fonctionner la CM avec quatre barrettes de ram ( 4x4, 4x8, 4x16, … ) mais n\'étant présente que sur certains sockets de carte mère ( 2066, TR4, … ).'
        '\n'
        '\nÀ toi de te renseigner sur ta carte mère afin de savoir si celle-ci fonctionne en Dual ou Quad Channel.',
        ephemeral=True
    )
    
@tree.command(name = 'delete', description='Purge le nombre de messages désiré.', guild=discord.Object(id=996907904324091944))
async def delete(interaction: discord.Interaction, amount: int):
    await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(
    f"Purged {amount} message",
    ephemeral=True
    )


tree.data = {}

@tree.command(name = 'config', description='Trouver une configuration adapté à ses besoin.', guild=discord.Object(id=996907904324091944))
async def config(interaction):
    budget = Select( 
        placeholder='Selectionnez votre budget',
        options=[
            discord.SelectOption(
                label='Petite faim',
                emoji='🍟', 
                description='De 800 à 1000€'
            ),
            discord.SelectOption(
                label='Grosse faim', 
                emoji='🍔', 
                description='De 1000 à 1500€'
            ),
            discord.SelectOption(
                label='Petage de bide', 
                emoji='🍗', 
                description='De 1500 à 2000€'
            )
        ]
    )

    async def budget_callback(interaction):
        tree.data[interaction.user.name]['budget'] = interaction.data["values"][0]
        await interaction.response.send_message(
            f'Ton budget a été pris en compte',
            ephemeral=True
        )
    
    usage = Select(
        placeholder='Selectionnez votre utilisation',
        options=[
            discord.SelectOption(
                label='Secretaire',
                emoji='📝',
                description='Bureautique simple'
            ),
            discord.SelectOption(
                label='Gamer',
                emoji='🎮',
                description='Tout sauf fotrnite'
            ),
            discord.SelectOption(
                label='Machine de travail',
                emoji='🔧',
                description='Besoin de fiabilitée'
            )
        ]
    )

    async def usage_callback(interaction):
        tree.data[interaction.user.name]['usage'] = interaction.data["values"][0]
        await interaction.response.send_message(
            f'Ton usage a été pris en compte',
            ephemeral=True
        )

    @tasks.loop(seconds=2)
    async def my_background_task():


        if interaction.user.name in tree.data:
            if len(tree.data[interaction.user.name])==3  and tree.data[interaction.user.name]['continue_to_check']:
                await interaction.followup.send(
                    f'Hello {interaction.user.name }, ton usage est {tree.data[interaction.user.name]["usage"]} avec un budget de type {tree.data[interaction.user.name]["budget"]}',
                    ephemeral=True
                )
                tree.data[interaction.user.name]['continue_to_check'] = False
                del tree.data[interaction.user.name]
            else: pass
        else : pass

        usage.callback = usage_callback
    budget.callback = budget_callback
    my_background_task.start()
    view = View()
    view.add_item(budget)
    view.add_item(usage)
    tree.data[interaction.user.name] = {}
    tree.data[interaction.user.name]['continue_to_check'] = True
    await interaction.response.send_message(
        "Des configurations de pc mise à jour régulièrement pour vous !", 
        view=view,
        ephemeral=True
    )

client.run(TOKEN)
