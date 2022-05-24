import os
import discord
from discord.ext import commands
from os import environ
from discord.utils import find
from dotenv import load_dotenv

load_dotenv()
token = environ["TOKEN"]
client = commands.Bot(command_prefix="t!", activity=discord.Game(name="t!owo to begin"), help_command=None)

for file in os.listdir("src\\cogs"):  # search cogs for giles
    if file.endswith(".py"):  # if the file ends in .py load cogs.file
        client.load_extension(f"cogs.{file[:-3]}")
        print(f"loaded {file[:-3]}")
    else:  # tell console it didn't load
        print(f"unable to load {file[:-3]}")


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")


@client.command()
async def owo(ctx):
    natalie = await client.fetch_user(824606337719074817)
    welcome = discord.Embed(title="Hello, fellow transbian! t!help for commands!",
                            description="I am TransbianBot! I am here to aid you in this server, for my commands, "
                                        "refer to t!help",
                            color=discord.Color.red())
    welcome.set_author(name=f"{natalie.name}", icon_url=f"{natalie.avatar_url}")
    welcome.add_field(name="I am an all purpose bot",
                      value="I do anything around the server, as long as you tell my creator to make it first.",
                      inline=False)
    welcome.add_field(name="I am community driven",
                      value="I am made based on your ideas, so don't be shy to ask for a command!")
    welcome.set_footer(text="Have fun!\n-N")  # create an embed named welcome
    await ctx.send(
        embed=welcome  # sends embed
    )


client.run(token)  # run bot
