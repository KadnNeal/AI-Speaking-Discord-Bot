import asyncio
import os
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from openai import OpenAI

#API keys (necessary for authenticating your requests to the API)
openai.api_key = os.getenv('PENAI_API_KEY')
discord_token = os.getenv('DISCORD_TOKEN')

#clip and turn users audio to an audio file

#use openai whisper to turn audio file to text

#use chatgpt to generate response
response = openai.Completion.create(
  engine="text-davinci-003",  #specifies gpt model 
  prompt="What is the capital of France?", 
  temperature=0.7, #controls randomness of text, higher means more diversity, 0.7 balanced
  max_tokens=60, #max length of generated response
  top_p=1.0, #
  frequency_penalty=0.0, #both f&p pen is likliness to repeat same line
  presence_penalty=0.0
)

# Define intents
intents = discord.Intents.all()

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event 
async def on_ready():
  print('The bot is ready!')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm here.")

@bot.command()
async def join(ctx):
  if ctx.author.voice:
    channel = ctx.author.voice.channel
    try:
        voice = await channel.connect()
    except discord.ClientException as e:
        await ctx.send(f"An error occurred: {e}", 
           executable="C:\\FFMPEG\\ffmpeg.exe")
        return

    # Check if FFmpeg is available
    try:
        source = FFmpegPCMAudio('myVoice.wav', executable='C:\\FFMPEG\\ffmpeg.exe')
        voice.play(source)

        # Wait for the audio to play before disconnecting or taking another action
        while voice.is_playing():
            await asyncio.sleep(1)
    except Exception as e:
        await ctx.send(f"An error occurred while trying to play audio: {e}")
  else:
    await ctx.send("You must be in a voice channel to run this command")
    
@bot.command(pass_context = True)
async def leave(arg):
  if (arg.voice_client):
    await arg.voice_client.disconnect()
    await arg.send("I left the voice channel")
    
  else:
    await arg.send("I am not in a voice channel")

@bot.command()
async def play()

bot.run('MTIwNDU4ODc2OTcyMjg5NjM5NA.GkvI17.6CSVlRB__DIk7LzsK6heZVdmRkdq2YeO9y5yHo')