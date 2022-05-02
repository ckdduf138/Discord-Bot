import discord
import myCommand as cmd
import myStorage as stg

from discord.ext import commands
from myToken import Token

bot=commands.Bot(command_prefix=';')
bot.remove_command('help')

@bot.event
async def on_ready():
  print(f"{bot.user.name} success")
  online = discord.Game("뭐라도")      
  await bot.change_presence(status=discord.Status.online, activity=online)
    
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send(f"'{ctx.message.content[1:]}' 명령어를 찾지 못했습니다")
  else:
    await ctx.send(f"명령어를 실행하지 못했습니다")

@bot.event
async def on_reaction_add(reaction, user):
  if user.id != bot.user.id:
    userMsg = reaction.message.embeds[0].title
    if str(reaction.emoji) == "✅":
      await reaction.message.edit(embed=cmd.list(userMsg, 0x00ff56))
    elif str(reaction.emoji) =="❎":
      stg.listDelete(user.id, userMsg)
      await reaction.message.edit(embed=cmd.list(userMsg, 0xEB3324))

#명령어 시작
@bot.command()
async def help(ctx):
  await ctx.channel.send(embed=cmd.help())

@bot.command()
async def list(ctx):
  userId = ctx.message.author.id
  userNm = ctx.message.author.name
  userIcon = ctx.author.avatar_url
  userList = stg.getList(userId)
  if len(userList) <= 1:
    await ctx.send(userNm + "님 할 일이 없습니다.")
    return

  await ctx.send(embed = cmd.listHeader(userNm, userIcon))
  for userMsg in userList:
    if(userId == userMsg):
      continue
    msg = await ctx.send(embed=cmd.list(userMsg, 0xffff33))
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")

@bot.command()
async def add(ctx):
  userId = ctx.message.author.id
  userMsg = ctx.message.content
  await ctx.send(cmd.add(userId, userMsg))

@bot.command()
async def delete(ctx):
  await ctx.send(cmd.delete(ctx))


#명령어 종료

bot.run(Token)
