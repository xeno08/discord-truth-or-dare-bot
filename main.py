import profanity
import json, discord
from random import choice
from discord.ext import commands
import webserver
from webserver import keep_alive
import os

client = commands.Bot(command_prefix= '~', help_command=None)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Activity(
        type=discord.ActivityType.listening, name="~help"))

     
@client.command()
async def help(ctx):
    with open('helps.json') as helps:
        helps = list(json.load(helps).items())
        helps = choice(helps)
        helps, author = helps
    embed = discord.Embed(title="Truth or Dare", description=helps,color=0xe75480)
    await ctx.reply(embed=embed)

@client.command(aliases=['d'])
async def dare(ctx):
    with open('dare.json') as dare:
        dare = list(json.load(dare).items())
        dare = choice(dare)
        dare, author = dare
    embed = discord.Embed(title="Dare", description=dare,color=0xa020f0)
    await ctx.reply(embed=embed)


@client.command(aliases=['t'])
async def truth(ctx):
    with open('truth.json') as truth:
        truth = list(json.load(truth).items())
        truth = choice(truth)
        truth, author = truth
    embed = discord.Embed(title="Truth", description=truth,color=0xffb6c1)
    await ctx.reply(embed=embed)


@client.command()
async def hye(ctx):
    with open('hye.json') as hye:
        hye = list(json.load(hye).items())
        hye = choice(hye)
        hye, author = hye
    embed = discord.Embed(title="Have You Ever", description=hye,color=0x007fff)
    await ctx.reply(embed=embed)


@client.command()
async def wyr(ctx):
    with open('wyr.json') as wyr:
        wyr = list(json.load(wyr).items())
        wyr = choice(wyr)
        wyr, author = wyr
    embed = discord.Embed(title="Would You Rather", description=wyr,color=0xadd8e6)
    await ctx.reply(embed=embed)


@client.command()
async def inv(ctx):
    with open('inv.json') as inv:
        inv = list(json.load(inv).items())
        inv = choice(inv)
        inv, author = inv
    embed = discord.Embed(title= "Invite me!",description='[Invite me to your Server!](https://discord.com/api/oauth2/authorize?client_id=890608373437980732&permissions=380104727552&scope=bot)' ,color=0xa9a9a9)
    await ctx.reply(embed=embed)

@client.command()
async def server(ctx):
    with open('server.json') as server:
      server = list(json.load(server).items())
      server = choice(server)
      server, author = server
      embed = discord.Embed(title="Join my Server!",description='[Join here!](https://discord.gg/hsPv5bhhs9)',color=0xffea00)
      await ctx.reply(embed=embed)

@client.command()
async def ver(ctx):
    with open('ver.json') as ver:
      ver = list(json.load(ver).items())
      ver = choice(ver)
      ver, author = ver
      embed = discord.Embed(title="Current version",description=ver,color=0xffbf00)
      await ctx.reply(embed=embed)
      
@commands.has_permissions(administrator=True)
@client.command()
async def created(ctx, *, sentence):
  with open('dare.json', "r+") as dare:
    data = json.load(dare)
    data[sentence.capitalize()] = str(ctx.message.author)
    dare.seek(0)
    json.dump(data, dare)
    await ctx.reply("Dare created.\nREMEMBER: Your dare may not break the rules of this server!")
    
@commands.has_permissions(administrator=True)
@client.command()
async def createt(ctx, *, sentence):
  with open('truth.json', "r+") as truth:
    data = json.load(truth)
    data[sentence.capitalize()] = str(ctx.message.author)
    truth.seek(0)
    json.dump(data, truth)
  await ctx.reply("Truth created.\nREMEMBER: Your truth may not break the rules of this server!")

@commands.has_permissions(administrator=True)
@client.command()
async def createhye(ctx, *, sentence):
  with open('hye.json', "r+") as hye:
    data = json.load(hye)
    data[sentence.capitalize()] = str(ctx.message.author)
    hye.seek(0)
    json.dump(data, hye)
  await ctx.reply("HYE created.\nREMEMBER: Your HYE may not break the rules of this server!")

@commands.has_permissions(administrator=True)
@client.command()
async def createwyr(ctx, *, sentence):
  with open('wyr.json', "r+") as wyr:
    data = json.load(wyr)
    data[sentence.capitalize()] = str(ctx.message.author)
    wyr.seek(0)
    json.dump(data, wyr)
  await ctx.reply("WYR created.\nREMEMBER: Your WYR may not break the rules of this server!")


@client.command()
async def mdare(ctx):
  with open('md.json') as md:
    md = list(json.load(md).items())
    md = choice(md)
    md, author = md
    embed = discord.Embed(title="Dare", description=md)
    await ctx.reply(embed=embed)

@commands.has_permissions(administrator=True)
@client.command()
async def createmdare(ctx, *, sentence):
  with open('md.json', "r+") as md:
    data = json.load(md)
    data[sentence.capitalize()] = str(ctx.message.author)
    md.seek(0)
    json.dump(data, md)
  await ctx.reply("Dare created.\nREMEMBER: Your dare may not break the rules of this server!")

@client.command()
async def suggestion(ctx, *, sentence):
  with open('suggestions.json', "r+") as suggestion:
    data = json.load(suggestion)
    data[sentence.capitalize()] = str(ctx.message.author)
    suggestion.seek(0)
    json.dump(data, suggestion)
  await ctx.reply("Thank you for the suggestion :)")

@client.command()
async def feedback(ctx, *, sentence):
  with open('feedback.json', "r+") as fb:
    data = json.load(fb)
    data[sentence.capitalize()] = str(ctx.message.author)
    fb.seek(0)
    json.dump(data, fb)
    await ctx.reply("Your feedback has been submitted.Thank you for using the bot :)")

@client.command()
async def gift(ctx):
  with open('test.json',"r+") as test:
    test = list(json.load(test).items())
    test = choice(test)
    test, author = test
    embed = discord.Embed(color=0xffea00,description='[Open box](https://www.youtube.com/watch?v=xvFZjo5PgG0)')
    await ctx.reply(embed=embed)
  
@client.command()
async def hug(ctx, user: discord.User):
  if user == None:
    await ctx.reply('Mention someone, if you wanna hug them, you silly!')
  else:
    with open('hugurl.json') as hug:
      hug = list(json.load(hug).items())
      hug = choice(hug)
      hug, author = hug 
      embed = discord.Embed(title = f"{ctx.message.author.name} hugs {user.name} ", color = discord.Color.magenta())
      embed.set_image(url = hug)
      embed.set_footer(text = f"Requested by {ctx.message.author}")
      await ctx.send(embed=embed)

@client.command()
async def pickup(ctx, user: discord.User):
  if user == None:
    await ctx.reply("Mention someone, if you wanna use a line")
  else:
    with open('pick.json') as pick:
      pick = list(json.load(pick).items())
      pick = choice(pick)
      pick, author = pick

      await ctx.send(f"{pick}")

keep_alive()

my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))
