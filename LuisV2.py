import asyncio
import os

import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from dotenv import load_dotenv

#load environmental variables from keys.env
load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
openai_key = os.getenv('OPENAI_API_KEY')

# Define intents
intents = discord.Intents.all()

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

#event to lyk in terminal that bot is ready to use
@bot.event 
async def on_ready():
  print('The bot is ready!')

#command for bot to say hello in text channel 
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm here.")

#command for bot to join voice channel
@bot.command()
async def join(ctx):
  if ctx.author.voice:
    channel = ctx.author.voice.channel
    try:
        voice = await channel.connect()
    except discord.ClientException as e:
        await ctx.send(f"An error occurred: {e}")
        return
    # Check if FFmpeg is available


    source = discord.FFmpegPCMAudio('myVoice.wav')
    voice.play(source)

    # Wait for the audio to play before disconnecting or taking another action
    while voice.is_playing():
      await asyncio.sleep(1)
  else:
    await ctx.send("You must be in a voice channel to run this command")

#command for bot to leave voice channel
@bot.command(pass_context = True)
async def leave(arg):
  if (arg.voice_client):
    await arg.voice_client.disconnect()
    await arg.send("I left the voice channel")
    
  else:
    await arg.send("I am not in a voice channel")

bot.run('MTIwNDU4ODc2OTcyMjg5NjM5NA.GPYNqC.N8vmgL4gklyXAHhuu4HhkQ0CEU3JCDyJPAgb04')