import os

import logging
import discord
from discord.ext import commands
import random
import tweepy
import math

import calendar
import datetime
import time

import imaplib

# Timestamp is a datetime object in UTC time
# def sample_function()


# DISCORD CREATE EVENT ---------------------------------------------
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# discord.version_info
print(discord.__version__)
bot = commands.Bot(command_prefix='', description='''I am the big crystal... you know?''')


def variable_set():
    nothing = True


# DISCORD EVENTS ---------------------------------------------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    variable_set()


@bot.event
async def on_message(message):

    await bot.say("Test")

    # @bot.event
    # async def on_voice_state_update(before, after):

    # @bot.event
    # async def on_member_join(member):

    # @bot.event
    # async def on_member_remove(member):

    # @bot.event
    # async def on_member_update(before, after):

    # Discord Commands
    # @bot.command(pass_context=True)
    # async def rolelist(ctx):
    """Lists available public roles"""
    # if ctx.message.channel.id == '211678559201132554':
    # global mood
    # await bot.say("Here is the list of available public roles! ```\n" + "\n".join(
    #    publicroles) + "```For private roles, type roleinfo.")


# Run the bot boiiiiiiis
bot.run("NDM0MzkzMDExMjI1NjI0NTc5.DbJvmA.Weft6yQhJbcN2WB8txzHEbFyK5I")
