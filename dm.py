import discord
import asyncio

client = discord.Client()
token = ''

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('게임명')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(title="메세지전송", description=f"<a:loading_bar_rb:852802276849877043>  메세지를 관리자채널로 전송하는중입니다.", colour=discord.Colour.gold(), timestamp=message.created_at)
            embed.set_footer(text=f'푸터')
            ms = await message.author.send(embed=embed)
            await asyncio.sleep(3)
            await ms.delete()

            embed = discord.Embed(title="문의전송 완료", description=f"정상적으로 관리자 패널에 문의가 처리되었습니다!", colour=discord.Colour.green(), timestamp=message.created_at)
            embed.set_footer(text=f'By. 디스코드 커뮤니티')
            await message.author.send(embed=embed)

            embed = discord.Embed(title="메세지가 도착했습니다.", description=f"전송자: <@{message.author.id}> | {message.author} ({message.author.id})\n내용: {message.content}\n\n답장: !r <@{message.author.id}> [메세지]", colour=discord.Colour.gold(), timestamp=message.created_at)
            embed.set_footer(text=f'푸터')
            await client.get_channel(채널ID).send(embed=embed)

    if message.content.startswith('!r'):
        if message.author.guild_permissions.administrator:
            msg = message.content[25:]
            msgm = message.mentions[0]
            embed = discord.Embed(description=f"[관리진] {message.author.name}: {msg}", colour=0x7289DA)
            await msgm.send(embed=embed)
        #     return

        #     embed = discord.Embed(title="전송됨", description=f"{msgm}님에게 메세지를 전송했습니다.", colour=0x7289DA, timestamp=message.created_at)
        #     embed.set_footer(text=f'디스코드 커뮤니티')
        #     await message.channel.send(embed=embed)
        #     await message.add_reaction(Success)
            
        # else:
        #     await message.add_reaction(Error)
        #     return
        
client.run(token)