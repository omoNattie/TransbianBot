import random
import discord
import praw
from discord.ext import commands
from random import randrange

reddit = praw.Reddit(
                client_id="QQhHetkbgnNngq8DFYS26g",
                client_secret="pQYPkXoAGSRb_1ReI4WO0kEE7-4fxQ",
                user_agent="Natalie",
                check_for_async=False  # api setup
            )


class TransRate(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def transrate(ctx, m: discord.Member = None):
            if m is None:
                transemb = discord.Embed(color=discord.Color.random())
                transemb.add_field(name="Trans Scale",
                                   value=f"I think that {ctx.author.name} is {randrange(100)}% trans")

                await ctx.send(
                    embed=transemb
                )
            else:
                transembtag = discord.Embed(color=discord.Color.random())
                transembtag.add_field(name="Trans Scale",
                                      value=f"I think that {m.name} is {randrange(100)}% trans")

                await ctx.send(
                    embed=transembtag
                )


class TransMemes(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def transmeme(ctx):
            await ctx.send("Searching for posts... :mag_right:")
            trans_submissions = reddit.subreddit("traaaaaaannnnnnnnnns")  # get subreddit
            all_subs = []  # get all submissions
            top = trans_submissions.top(limit=100)  # set the limit to only pick from top

            for submission in top:
                all_subs.append(submission)  # search all submissions in top and append

            random_sub = random.choice(all_subs)  # get a random submission
            name = random_sub.title
            url = random_sub.url

            transmemeemb = discord.Embed(title=name, description="In subreddit r/traaaaaaannnnnnnnnns",
                                         color=discord.Color.random())
            transmemeemb.set_image(url=url)  # make an embed with title and image

            await ctx.send(
                embed=transmemeemb  # send
            )


class Repel(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def repel(ctx, m: discord.Member = None):
            if m is None:
                await ctx.send(
                    "Off, I say!",
                    file=discord.File("src/imgs/anti-horni-spray.gif")
                )
            elif m == ctx.author:
                await ctx.send("Y-you can't do that to yourself!!!")
            else:
                await ctx.send(
                    f"Off, I say, {m.name}!",
                    file=discord.File("src/imgs/anti-horni-spray.gif")
                )


class Celeste(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def celeste(ctx):
            await ctx.send("Searching for posts... :mag_right:")
            celery = reddit.subreddit("celestegame")  # get celeste reddit
            topcelery = celery.top(limit=100)  # set your limit from top
            all_celeste = []  # all submissions from limit

            for celestepost in topcelery:
                all_celeste.append(celestepost)  # append all posts in limit

            random_celeste = random.choice(all_celeste)  # get a random post from all subs
            celestetitle = random_celeste.title
            celesteurl = random_celeste.url

            celesteemb = discord.Embed(title=celestetitle, description="In subreddit r/celestegame",
                                       color=discord.Color.red())
            celesteemb.set_image(url=celesteurl)  # create embed

            await ctx.send(
                f"{celestetitle}\nfrom subreddit r/celestegame\n{celesteurl}"
            )


class Roll(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def roll(ctx, *, msg=""):
            if msg == "":
                await ctx.send("You need to roll for something you know")
            else:
                rollemb = discord.Embed(color=discord.Color.random())
                rollemb.add_field(name=f"Rolling for {msg}",
                                  value=f"{ctx.author.name} has rolled a {randrange(1,20)} for {msg}")

                await ctx.send(
                    embed=rollemb
                )


def setup(client):
    client.add_cog(TransRate(client))
    client.add_cog(TransMemes(client))
    client.add_cog(Celeste(client))
    client.add_cog(Repel(client))
    client.add_cog(Roll(client))
