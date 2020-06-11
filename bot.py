import os
import random
import discord
from discord.ext import commands

#Prefix to Bot Commands
bot = commands.Bot(command_prefix = '&')

# Event to Change Presence of Bot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with these hoe's Hearts"))


# Command to pick an user for Movie night
@bot.command()
async def pick(ctx):
    await ctx.send(random_user(ctx))

# Command to set movie
@bot.command(pass_context=True)
async def set(ctx, *, arg):
    role = discord.utils.get(ctx.guild.roles, name="movie idiots")
    if role in ctx.author.roles:
        await ctx.send(set_movie(arg))
    else:
        return "Not a Movie Idiot!"

# Command to get movie
@bot.command()
async def get(ctx):
    role = discord.utils.get(ctx.guild.roles, name="movie idiots")
    if role in ctx.author.roles:
        await ctx.send(get_movie())
    else:
        return "Not a Movie Idiot!"

# Set Movie Function
# Take's user input and sets a movie
def set_movie(args):
    global movie_name
    movie_name = str(args)
    return "The next movie is " + "'" + movie_name + "' !"

# Get Movie Function
# Take's user input and gets a movie
def get_movie():
    return "The upcoming movie is " + "'" + movie_name + "' !"


# Random user function
# Determines if User is apart of the Movie Idiots role
# If user is apart of role, random user is sent back otherwise message informs they don't have the role.
def random_user(ctx):
    role = discord.utils.get(ctx.guild.roles, name="movie idiots")
    role_list = role.members
    if role in ctx.author.roles:
        return role_list[random.randrange(len(role_list))].name + " is the Movie Master!"
    else:
        return "Not a Movie Idiot!"


