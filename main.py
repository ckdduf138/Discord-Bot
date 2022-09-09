import discord
import myCommand as cmd
import myStorage as stg

from discord.ext import commands
from myToken import Token

# User Direct Message 
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=';', intents = intents)
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
async def on_member_join(member):
  await member.send("반갑습니다. ;help를 통해 도움말을 확인하세요.")

@bot.event
# reaction Check
async def on_reaction_add(reaction, user):

  # 봇이 추가한 경우 reutrn
  if user.bot: 
    return

  userMsg = [reaction.message.embeds[0].title]

  if str(reaction.emoji) == "✅":
    stg.UpdateList(user.id, userMsg[0])
    userMsg.append('001')
    await reaction.message.edit(embed=cmd.list(userMsg))
  elif str(reaction.emoji) =="❎":
    stg.DeleteList(user.id, userMsg[0])
    userMsg.append('002')
    await reaction.message.edit(embed=cmd.list(userMsg))

#명령어 시작

# help
@bot.command()
async def help(ctx):
  await ctx.channel.send(embed=cmd.help())

# list
@bot.command()
async def list(ctx):

  # 유저 정보 
  userId = ctx.message.author.id
  userNm = ctx.message.author.name

  # 할 일이 없을 경우 return 
  userMsgList = stg.SelectList(str(userId))
  if len(userMsgList) < 1:
    await ctx.send(userNm + "님 할 일이 없습니다.")
    return

  # 할 일이 있을 경우

  # server Message
  await ctx.send(embed=cmd.SendServerMessage(userNm, userMsgList))

  # 유저 Direct Message
  try:
    await ctx.message.author.send(embed = cmd.listHeader(userNm))
    for userMsg in userMsgList:
      msg = await ctx.message.author.send(embed=cmd.list(userMsg))
      await msg.add_reaction("✅")
      await msg.add_reaction("❎")
  except discord.errors.Forbidden:
    await ctx.send(f"{userNm}님\n서버 이름 클릭 - 개인정보 보호 설정 - 서버 멤버가 보내는 개인 메시지 허용해주세요.")

# add
@bot.command()
async def add(ctx):
  userId = ctx.message.author.id
  userMsg = ctx.message.content
  await ctx.send(cmd.add(userId, userMsg))

#명령어 종료


bot.run(Token)
