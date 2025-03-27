from discord.ext import commands

class ServerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def change_server_name(self, ctx, *, new_name: str):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send("You do not have permission to change the server name!")
                return

            await ctx.guild.edit(name=new_name)
            await ctx.send(f"Server name changed to: {new_name}")
        except Exception as e:
            await ctx.send(f"Failed to change the server name: {e}")

def setup(bot):
    bot.add_cog(ServerCommands(bot))
