import requests
from discord.ext import commands

class WebhookCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spam_webhook(self, ctx, url: str, text: str, spam_ammount: int):
        """Spam a webhook multiple times."""
        if not spam_ammount.isdigit():
            await ctx.send("Invalid spam amount. Please enter a valid number.")
            return

        spam_ammount = int(spam_ammount)

        for i in range(spam_ammount):
            payload = {"content": text}
            response = requests.post(url, json=payload)
            if response.status_code == 204:
                await ctx.send("Successfully spammed the webhook!")
            else:
                await ctx.send(f"Failed to spam the webhook. Status Code: {response.status_code}")

    @commands.command()
    async def del_webhook(self, ctx, url: str):
        """Delete a webhook."""
        confirmation = input(f"Are you sure you want to delete this webhook {url}? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            response = requests.delete(url)
            if response.status_code == 204:
                await ctx.send("Webhook deleted successfully!")
            else:
                await ctx.send(f"Failed to delete the webhook. Status Code: {response.status_code}")
        else:
            await ctx.send("Webhook deletion canceled.")

def setup(bot):
    bot.add_cog(WebhookCommands(bot))
