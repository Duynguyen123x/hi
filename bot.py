import discord,time
import random
import os, sys, requests, json
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from discord.utils import get
from random import choice, randint, shuffle
token = "MTAwNjc2NDE3OTA3NzczNDQ2MQ.G3Zrm9.lbCnZieZ0h-nT5hfRGcux5c4NhRNsk_L4aDBRI"
prefix = "!"
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix,help_command=None, intents=intents)

        
        
        
        
        


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')  
ad = "duynguyenx#4848" 
@bot.event
async def on_connect():
	os.system("clear")
	print(f"Connecting Bot User : {bot.user}")
	time.sleep(1.0)
	print("Bot Is Online Now !!!")
    

    
   
   
   
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		messg = discord.Embed(title="**WARNING !!!**",description="`Vui Lòng Đợi {:.2f}s Mới Có Thể Sử Dụng Lệnh Này!!!`".format(error.retry_after))
		await ctx.reply(embed=messg)
   

@bot.tree.command(name="sms", description="Spam sms ")
async def sms(interaction: discord.Interaction, phone:str, amount: str):	
	embed = discord.Embed(title="</𝙨𝙥𝙖𝙢𝙨𝙢𝙨>", color=discord.Colour.random())
	thna3 = ["https://th.bing.com/th/id/OIP.UAiv5cS9g6uVA1UvTaaCwAHaHa?pid=ImgDet&rs=1"]
	rdthn3 = random.choice(thna3)
	embed.set_thumbnail(url=rdthn3)
	embed.add_field(name="**`👤 User:`**",value=f"[ {interaction.user} ]")
	embed.add_field(name="**`📱 Phone:`**",value=f"[ {phone} ]")
	embed.add_field(name="**`💠 Amount:`**",value=f"[ {amount} ]")
	embed.add_field(name="**`👑 Admin:`**",value=f"[ {ad} ]")
	ima = ["https://media4.giphy.com/media/q217GUnfKAmJlFcjBX/giphy.gif","https://media2.giphy.com/media/dyjrpqaUVqCELGuQVr/giphy.gif"]
	mg = random.choice(ima)
	embed.set_image(url=mg)
	embed.set_footer(text=f"👑 Dev :duynguyen#4848 | Requests By {interaction.user}  ")
	
	await interaction.response.send_message(embed=embed)
	
	os.system(f"python sms.py {phone} {amount}")
			



	 
	 

    
    
    
    
    


@bot.command()
async def sms(ctx, phone, amount:int):
		if (amount < 101):
			embed = discord.Embed(title="</𝙨𝙥𝙖𝙢𝙨𝙢𝙨>", color=discord.Colour.random())
			thna3 = ["https://th.bing.com/th/id/OIP.UAiv5cS9g6uVA1UvTaaCwAHaHa?pid=ImgDet&rs=1"]
			rdthn3 = random.choice(thna3)
			embed.set_thumbnail(url=rdthn3)
			embed.add_field(name="**`👤 User:`**",value=f"[ {ctx.author.name} ]")
			embed.add_field(name="**`📱 Phone:`**",value=f"[ {phone} ]")
			embed.add_field(name="**`💠 Amount:`**",value=f"[ {amount} ]")
			embed.add_field(name="**`👑 Admin:`**",value=f"[ {ad} ]")
			ima = ["https://media4.giphy.com/media/q217GUnfKAmJlFcjBX/giphy.gif","https://media2.giphy.com/media/dyjrpqaUVqCELGuQVr/giphy.gif"]
			mg = random.choice(ima)
			embed.set_image(url=mg)
			embed.set_footer(text=f"👑 Dev :duynguyenx#4848 | Requests By {ctx.author.name} at {ctx.message.created_at} ")
			
			await ctx.channel.send(embed=embed)
			
			os.system(f"python sms.py {phone} {amount}")
			
		else:
			embed = discord.Embed(title="</𝙨𝙥𝙖𝙢𝙨𝙢𝙨>", color=0xFF0000)
			embed.add_field(name="**WARNING**",value="`Spam Max 100 Thôi Nhé !!!`")
			embed.set_footer(text=f"© Dev : duynguyenx | Warning {ctx.author.name} !!!")
			await ctx.send(embed=embed)

		

bot.run(token)
