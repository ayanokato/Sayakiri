import discord
import asyncio
import dotenv
import os
from discord.ext import commands

dotenv.load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix = ";", intents = discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")
    await bot.get_channel(1151313056383647894).send("I'm here!")

    # COGS
    await bot.load_extension("cogs.Moderation")

@bot.command()
async def help(ctx):
    await ctx.send("This is the help menu, or at least will be")

bot.run(token)