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

    # COGS
    await bot.load_extension("cogs.Moderation")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = "Help",
        description = "This is the help menu",
        color = discord.Colour.dark_grey()
    )
    await ctx.send(embed = embed)

bot.run(token)