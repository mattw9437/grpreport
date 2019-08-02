import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import json
import os

token = os.getenv("trellotoken")
trellokey = os.getenv("trellokey")
boardurl = "https://trello.com/Rknc2a7b/cards"
list = os.getenv("listid")
rblxapi = "http://api.roblox.com/users/get-by-username"

bot = commands.Bot(command_prefix="!")

def iterate(args):
    descproof = ""	
    for proofs in args:
	    descproof += proofs + "\n"

    return descproof

def grabId(rblxuser):
    apiresp = requests.get(rblxapi, timeout=5, data={"username" : rblxuser})
    pijson = json.loads(apiresp.text)

    if "Id" in pijson:
        return (pijson["Id"])

    else:
        return False

@bot.event
async def on_ready():
	print ("meme test")
	print (bot.user.id)
	print (bot.user.name)
	
	
@bot.command(pass_context=True)
async def h(ctx):
	
	print(ctx.message.channel.id == os.getenv("channelid"))
	if ctx.message.channel.id == int(os.getenv("channelid")):
		await ctx.send("to report use !r useryouarereporting proof1 proof2 proof3, and so on")

@bot.command(pass_context=True)
async def r(ctx, user, proof, *args):
	author = ctx.message.author
	userid = grabId(user)	
	if ctx.message.channel.id == int(os.getenv("channelid")) and userid != False:
		adesc = proof + "\n" + iterate(args) + "\n Report by:" + author.name +  "\n DiscordID:" + str(author.id)
		cdata = {"key":trellokey,"token":token,"idList":list,"name":user + ":" + str(userid),"desc":adesc}
		req = requests.post(boardurl, params=cdata)
		jsont = json.loads(req.text)
		clink = jsont["shortUrl"]
		await ctx.send("ty" + author.mention + " " + clink)
	elif ctx.message.channel.id == int(os.getenv("channelid")) and userid == False:
		await ctx.send("{0} is not a valid username {1}".format(user, author.mention))
		





bot.run(os.getenv("disctoken"))

