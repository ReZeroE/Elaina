import datetime
import time
import os
import re
import json
import sys
import AnilistPython
import discord
from google_trans_new import google_translator

from bot_info import BotInfo
bot_info_obj = BotInfo()

from guild_logging import BotLog
bot_log_obj = BotLog()

from clearance_scan import ClearanceScan
cs_obj = ClearanceScan()

from input_scan import InputScan
input_scan_obj = InputScan()

from output_scan import OutputScan
output_scan_obj = OutputScan()

from main_functions import BotFunctions
bot_func_obj = BotFunctions()



# ======================================================================================================================
# BOT INFO

guild_id = -1

bot_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
channel_id = 0000000000000000000000
channel_name = "xxxxxxxxxxxxxx"

# ======================================================================================================================

client = discord.Client()
@client.event
async def on_ready():
    bot_testing = client.get_channel(channel_id) 
    new_message = "Hi! I am Elaina! Nice to meet you all!"
    await bot_testing.send(new_message)


@client.event
async def on_message(message):
    #bot_testing = client.Bot(command_prefix = '//')
    user_input = message.content.lower().replace('//elaina', '//')
    if user_input.find('// ') == -1:
        user_input = user_input.replace('//', '// ')

    original_input = message.content
    message_server_id = message.guild.id
    message_server_name = message.guild.name
    user_id = message.author.id
    username = message.author.name

    bot_log_obj.log_guild_info(message_server_id, message_server_name)

    print(f"User Info: {[username, user_id]}")
    print(f"Bot reply (boolean): {message.author == client.user}")

    while message.author != client.user and not message.author.bot:
        scannedResult = input_scan_obj.scanInput(user_input, message_server_id, user_id)
        print(f"Scanned results: {scannedResult}")

        user_input = user_input.replace("permission override>> ", "").replace("permission override>>", "")
        original_input = original_input.replace("permission override>> ", "").replace("permission override>>", "")


        # Not command
        if scannedResult.find('None-Command') != -1:
            break

        # check if permission is denied
        if scannedResult.find('C1D') != -1 or scannedResult.find('C2D') != -1 or scannedResult.find('C0D') != -1:
            await message.channel.send(scannedResult)
            break

        # bot called in a banned server
        if scannedResult.find('Error 0') != -1:
            print(f'\nBot has been called in a banned server with ID {message_server_id}!\n')
            break

        # Program Termination
        if scannedResult.find('Code A1') != -1:
            print("Program Terminated")
            await message.channel.send("Program Terminated Successfully")
            exit(0)

        # Purge
        elif scannedResult.find('Code A2') != -1:
            await message.channel.send("**Password Required (purge > 100)** - please enter the password in the back-end terminal")
            purge_message = bot_func_obj.purgeCheck(user_input)
            if purge_message.lower().find('error') != -1:
                await message.channel.send(purge_message)
            else:
                await message.channel.purge(limit=2)
                await message.channel.send(purge_message)
                time.sleep(3)
                await message.channel.purge(limit=bot_func_obj.purgeNum(user_input) + 1)
            break

        # ========================================================================================================
        # anime search
        if scannedResult.find('Code B1') != -1:
            await message.channel.send(embed=bot_func_obj.searchAnimeInfo(user_input))
            break

        # character search
        elif scannedResult.find('Code B2') != -1:
            await message.channel.send(embed=bot_func_obj.searchCharacterInfo(user_input))
            break

        # get perm
        elif scannedResult.find('Code B3') != -1:
            await message.channel.send(embed=bot_func_obj.getPerm(username, user_id))
            break

        # Pick command
        elif scannedResult.find('Code B4') != -1:
            print("Milim Pick Initiated")
            # await message.channel.send(embed=functionPointer.pickItem(original_input))
            await message.channel.send(bot_func_obj.pickItemNonEmbed(original_input))
            break

        # rate command
        elif scannedResult.find('Code B5') != -1:
            print("Milim Rate Initiated")
            await message.channel.send(bot_func_obj.rateItem(original_input))
            break

        # translator
        elif scannedResult.find('Code B6') != -1:
            translationStr = bot_func_obj.translation(user_input)
            if translationStr != "NONE":
                await message.channel.send(f"**Translated Text: **{bot_func_obj, translationStr}")
            break

        break

# ======================================================================================================================
# HELPER FUNCTIONS


# ======================================================================================================================

while True:
    client.run(bot_id)