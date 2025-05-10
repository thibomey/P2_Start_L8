import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True								# Zorgt ervoor dat we berichtinhoud kunnen lezen
bot = commands.Bot(command_prefix="/", intents=intents)    	# Onze commando's zullen met een $ starten

@bot.event
async def on_ready():
    print(f'We zijn ingelogd als {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:  	# Bericht door de bot verstuurd
        return  						# Return (doe niets meer hierna)


    if message.content.lower() == 'codefever':
        await message.channel.send('is tof')

    if message.content.lower() == 'ping':
        await message.channel.send('pong')
    else:
        await message.channel.send(f"Je zei {message.content}")
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    embed1 = discord.Embed(title="Deleted Message!")
    embed1.add_field(name="..", value=f"Someone has deleted the following:\n{message.content}")
    embed1.colour = (0x90EE90)
    dele = bot.get_channel(1370664570955501713)
    await dele.send(embed=embed1)

@bot.command()
async def test(context):
	await context.send("Dit was een test!")

@bot.command()
async def random_cat (context):
    foto_url = f'https://cataas.com/cat?{random.randint(1, 1000)}'
    await context.send(foto_url)

@bot.command()
async def random_bear (context):
    foto_url = f'https://placebear.com/600/600?{random.randint(1, 1000)}'
    await context.send(foto_url)

from token import discord_token
bot.run(discord_token)