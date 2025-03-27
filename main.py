import discord
from discord.ext import commands
import os

def main_menu():
    print("""\
______          _             __   __          _     _ 
| ___ \        | |            \ \ / /         (_)   | |
| |_/ / __ ___ | |_ ___  _ __  \ V / _ __ __ _ _  __| |
|  __/ '__/ _ \| __/ _ \| '_ \ /   \| '__/ _` | |/ _` |
| |  | | | (_) | || (_) | | | / /^\ \ | | (_| | | (_| |
\_|  |_|  \___/ \__\___/|_| |_\/   \/_|  \__,_|_|\__,_|

              made by 10txn (in beta)
""")

    print("\nProtonXraid menu:")
    print("1. Raid with Discord bot")
    print("2. Spam Webhook")
    print("3. Delete Webhook")
    print("4. Exit")
        
    choice = input("\nEnter your choice (1-4): ")
            
    if choice == '1':
        bot_raid()
    elif choice == '2':
        spam_webhook()
    elif choice == '3':
        del_webhook()
    elif choice == '4':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")

def bot_raid():
    # Prompt for the bot token
    token = input("Please enter your bot token: ").strip()

    # Create the bot instance with necessary intents
    intents = discord.Intents.default()
    intents.guilds = True  # Make sure the bot can access guilds
    intents.messages = True  # To handle messages if needed
    intents.message_content = True  # Required for bots to read messages content in interactions
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Load cogs (commands)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    # Run the bot
    try:
        bot.run(token)
    except Exception as e:
        print(f"Failed to start the bot: {e}")

# Run the menu
if __name__ == "__main__":
    main_menu()
