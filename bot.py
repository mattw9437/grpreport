import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import json
import os

token = os.getenv("trellotoken")
trellokey = os.getenv("trellokey")
boardurl = "https://trello.com/1/cards"
list = os.getenv("listid")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print ("meme test")
	print (bot.user.id)
	print (bot.user.name)

@bot.command(pass_context=True)
async def r(ctx, user, proof, proof2 = "", proof3 = ""):
	if ctx.message.channel.id == os.getenv("channelid"):
		author = ctx.message.author		
		adesc = "{0} \n {1} \n {2} \n Report by: {3} \n DiscordID: {4}".format(proof ,proof2, proof3, author, author.id)
		cdata = {"key":trellokey,"token":token,"idList":list,"name":user,"desc":adesc}
		req = requests.post(boardurl, params=cdata)
		jsont = json.loads(req.text)
		clink = jsont["shortUrl"]
		await bot.say ("ty" + author.mention + " " + clink)


@bot.command(pass_context=True)
async def help(ctx)
if ctx.message.channel.id == os.getenv("channelid"):
	await bot.say("to report use !r useryouarereporting proof1 proof2 proof3, you can add up to 3 proofs ")


bot.run(os.getenv("disctoken"))

ff