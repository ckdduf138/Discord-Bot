import myStorage as stg
import discord

def help():
    embed = discord.Embed(title = "도움말", description = "봇 서버를 켜지 않은 동안에는 작동하지 않으며, 봇의 온/오프라인 상태 확인으로 확인하실 수 있습니다.", color = 0x00ff56, inline = False)
    embed.add_field(name = ";도움말", value = "도움말을 표시합니다.", inline = False)
    embed.add_field(name = ";list", value = "할일 목록을 볼 수 있습니다..", inline = False)
    embed.add_field(name = ";add (내용)", value = "할일을 추가합니다.", inline = False)
    embed.add_field(name = "✅ 클릭", value = "할일을 완료합니다.", inline = False)
    embed.add_field(name = "❎ 클릭", value = "할일을 삭제합니다.", inline = False)
    embed.set_footer(text = "문의 #3779")
    return embed

def listHeader(userNm, userIcon):
    embed = discord.Embed(title = "To-Do-List", description = userNm + "님의 할일 목록", color = 0x00ff56, inline = False)
    return embed

def list(userMsg):
    
    if(userMsg[1] == '000'):    # 000 -> 할일 하는 중
        color =  0xffff33
    elif(userMsg[1] == '001'):  # 001 -> 할일 완료
        color = 0x00ff56
    else:                       # 002 -> 할일 삭제
        color = 0xEB3324
    embed = discord.Embed(title = userMsg[0], color = color, inline = False)
    return embed

def add(userId, userMsg):
    if len(userMsg) >= 5:
        userMsg = userMsg[5:]
        stg.AddList(userId, userMsg)
        return "추가 되었습니다."
    else:
        return "내용을 입력해주세요."

def delete(ctx):
    return "delete"


def SendUserDm(userNm, userMsgList):
    embed = discord.Embed(title = "To-Do-List", description = userNm + "님의 할일 목록", color = 0x00ff56, inline = False)

    idx = 1
    for userMsg in userMsgList:
        msg = str(idx) + ". " + userMsg[0] 
        embed.add_field(name = "\u200B", value= msg, inline = False)
        idx += 1

    return embed



