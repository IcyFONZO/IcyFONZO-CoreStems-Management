import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to IcyFONZO and CoreStems campaign server! Make sure to be a Citizen of New York in this group: https://www.roblox.com/My/Groups.aspx?gid=2968917 to be able to vote! Thanks for being intrested in IcyFONZO and CoreStems! ')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='IcyFONZO & CoreStems for NYS Government!! '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '-ping':
        await client.send_message(message.channel,'Pong, why not vote IcyFONZO and CoreStems! ')
    if message.content == '-campaignlogo':
        em = discord.Embed(description='IcyFONZO and CoreStems campaign logo! We represent the future of NYS! ')
        em.set_image(url='https://cdn.discordapp.com/attachments/513698920413790220/513734138092584981/Untitled.png')
        await client.send_message(message.channel, embed=em)
    if ('ass') in message.content:
       await client.delete_message(message)
    if ('Ass') in message.content:
       await client.delete_message(message)
    if ('Bitch') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('Fuck') in message.content:
       await client.delete_message(message)
    if ('Cunt') in message.content:
       await client.delete_message(message)
    if message.content == '-vote':
        await client.send_message(message.channel,'Make sure to be a Citizen of New York in this group: https://www.roblox.com/My/Groups.aspx?gid=2968917 to be able to vote!')
    if message.content == '-CoreStems':
        em = discord.Embed(description='Hello my name is CoreStems! I have plenty leadership experience and current roles within New York: NYPD- Captain, NYDOC- Assistant chief, NYCG- Lieutenant junior grade, NYNG- Private First Class, NYDHS- Federal Protective Service, State of New York- State Assembly, NYDOJ- State BAR Attorney. **I will take pride in my position as a LT. Governor Gubernatorial Candidate and uphold that law!Giving you a Government that you always look forward too!**')
        em.set_image(url='https://cdn.discordapp.com/attachments/513698920413790220/513785123913728002/6b49da543d71e2e7da3b0f87e2ab37c3.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '-IcyFONZO':
        em = discord.Embed(description='Hello dear Citizen/Visitor! My name is IcyFONZO, I have many past and current leadership positions! I promise to uphold the Constitution of the State of New York and try at best to do so! Here are some of my past and current leadership positions within the State of New York: NYPD- Inspector, NYDOT- City Inspector, NYFD/EMS- Paramedic, NYPDDOD- Instructor, NYDOJ- Public Defender, State of New York- State Assembly .x2 and LT. Governor! **I promise to take honest and true full pride in my position to uphold the State of New York! Giving you a Government that you always look forward too! Sincerely, your Governor Gubernatorial Candidate @(D) IcyFONZO**')
        em.set_image(url='https://cdn.discordapp.com/attachments/513698920413790220/513786825345728512/64b300ebd6ca6a6c86a91de8209cf3e8.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '-group':
        await client.send_message(message.channel,'https://www.roblox.com/My/Groups.aspx?gid=2968917')
    if message.content == '-invitelink':
        await client.send_message(message.channel,'We want to thank you for trying to support our campaign! Here is our campaign discord link: https://discord.gg/WtF5kmH')
client.run('NTEzNzIzNjU1OTIzMTcxMzI4.DtNHyA.oZ46gIhDMfN9g4KWpIysqcb5P-o')
