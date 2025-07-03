import discord
from discord.ext import commands
import asyncio
import logging
import os

logging.getLogger('discord.http').setLevel(logging.ERROR)
logging.getLogger('discord.gateway').setLevel(logging.ERROR)

bot_token = input("bot token: ")

LIGHT_GRAY = "\033[97m"
ASH_GRAY = "\033[38;5;246m"
DARK_GRAY = "\033[90m"
GRAY = "\033[37m"

CYAN = "\033[96m"
GREEN = "\033[92m"
BLUE = "\033[94m"

BOLD = "\033[1m"
RESET = "\033[0m"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

@bot.event
async def on_ready():
    while True:
        clear_screen()


        activity = discord.Game(name="kreopoliz tool")
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
        print(f"\n {bot.user} ({bot.user.id})")
        print("Kreopoliz Tool UP.\n")

        print(f"{CYAN}(1){RESET} {LIGHT_GRAY}Spam Messages")
        print(f" ├── {CYAN}(2){RESET} {LIGHT_GRAY}Create Channels")
        print(f" ├── {CYAN}(3){RESET} {LIGHT_GRAY}Rename Server")
        print(f" ├── {CYAN}(4){RESET} {LIGHT_GRAY}Delete All Channels")
        print(f" ├── {CYAN}(5){RESET} {LIGHT_GRAY}Delete All Roles")
        print(f" └── {CYAN}(6){RESET} {LIGHT_GRAY}Exit")

        choice = input("Choise? ").strip()

        if choice == "1":
            await spam_messages()
        elif choice == "2":
            await create_custom_channels()
        elif choice == "3":
            await rename_server()
        elif choice == "4":
            await delete_all_channels()
        elif choice == "5":
            await delete_all_roles()
        elif choice == "6":
            print("Exiting...")
            await bot.close()
            break
        else:
            print("LATHOS RE GAY\n")
            input("Press Enter to continue...")

async def spam_messages():
    clear_screen()
    try:
        guild_id = int(input("Guild ID: "))
        guild = bot.get_guild(guild_id)
        if not guild:
            print("LATHOS RE GAY.")
            input("Press Enter to return...")
            return

        msg_content = input("ti thes na stilo?: ")
        msg_count = int(input("poses fores thes na to stilo?: "))
        ch_limit = int(input(f"posa channels na xrisimopohso?: (Max {len(guild.text_channels)}): "))
        channels = guild.text_channels[:ch_limit]

        send_tasks = []
        for ch in channels:
            for _ in range(msg_count):
                send_tasks.append(ch.send(msg_content))

        await asyncio.gather(*send_tasks, return_exceptions=True)
        print(f"stalthkan {msg_count} tosa: {len(channels)} kanalia.")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to return...")

async def create_custom_channels():
    clear_screen()
    try:
        guild_id = int(input("Guild ID: "))
        guild = bot.get_guild(guild_id)
        if not guild:
            print("LATHOS RE GAY.")
            input("Press Enter to return...")
            return

        num_channels = int(input("posa kanalia na dhmiourghso?: "))
        channel_name = input("Pos na ta onomaso?: ")

        for i in range(1, num_channels + 1):
            await guild.create_text_channel(name=f"{channel_name}")
        print(f"ftiaxthkan {num_channels} allaje '{channel_name}-X'")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to return...")

async def rename_server():
    clear_screen()
    try:
        guild_id = int(input("Guild ID: "))
        new_name = input("new server name: ")
        guild = bot.get_guild(guild_id)
        if not guild:
            print("LATHOS RE GAY.")
            input("Press Enter to return...")
            return
        await guild.edit(name=new_name)
        print("To Onoma allaje:", new_name)
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to return...")

async def delete_all_channels():
    clear_screen()
    try:
        guild_id = int(input("Guild ID: "))
        guild = bot.get_guild(guild_id)
        if not guild:
            print("LATHOS RE GAY.")
            input("Press Enter to return...")
            return

        delete_tasks = [channel.delete() for channel in guild.channels]
        await asyncio.gather(*delete_tasks, return_exceptions=True)
        print("diagrafthkan ola ta kanalia.")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to return...")

async def delete_all_roles():
    clear_screen()
    try:
        guild_id = int(input("Guild ID: "))
        guild = bot.get_guild(guild_id)
        if not guild:
            print("LATHOS RE GAY.")
            input("Press Enter to return...")
            return

        delete_tasks = []
        for role in guild.roles:
            if role.name != "@everyone":
                delete_tasks.append(role.delete())

        await asyncio.gather(*delete_tasks, return_exceptions=True)
        print("diagrafthkan ola ta roles (ekto @everyone).")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to return...")

bot.run(bot_token)
