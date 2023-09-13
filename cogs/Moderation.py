import discord
import asyncio
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_role("Owner")
    async def kick(self, ctx, member: discord.Member, *, reason):
        dm = discord.Embed (
            title = "Kick",
            description = f"You have been kicked for `{reason}`. If you believe this was wrongful, you may appeal.",
            color = discord.Colour.red()
        )
        await member.send(embed = dm)
        await member.kick(reason = reason)
        embed = discord.Embed(
            title = "Kick",
            description = f"Kicked **{member.display_name}**",
            color = discord.Colour.red()
        )
        embed.add_field(name = "Reason", value = f"{reason}")
        await ctx.send(embed = embed)
    
async def setup(bot):
    await bot.add_cog(Moderation(bot))