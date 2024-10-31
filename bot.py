import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def plastik_geri_dönüsüm_önemi(ctx):
    fikirler = [
        "Sadece bir anlığına daha önce attığınız çöplerin geri geldiğini düşünün... Çok kötü oldu dimi geri dönüşüm olmasa işte böyle olurdu  ama sadece evlerimiz değil sokaklar ve heryer.",
        "Geri dönüşüm çok önemlidir çünkü kaynakları tekrar tekrar kullanabilmemizi sağlar.",
        "Ki bizlerde kendimizce evimizde plastikleri geri dönüştürebiliriz.",
        "Geri dönüşüm yapmak, doğal kaynaklarımızı korumamıza yardımcı olur. Örneğin, geri dönüştürülen bir plastik şişe, yeni bir şişe yapmak için gereken enerji ve su miktarını önemli ölçüde azaltır.",  
    
    await ctx.send(f"Geri dönüşümün önemix:\n- " + "\n- ".join(fikirler))

import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def plastik_geri_dönüsüm_önemi(ctx):
    fikirler = [
        "Sadece bir anlığına daha önce attığınız çöplerin geri geldiğini düşünün... Çok kötü oldu dimi geri dönüşüm olmasa işte böyle olurdu  ama sadece evlerimiz değil sokaklar ve heryer.",
        "Geri dönüşüm çok önemlidir çünkü kaynakları tekrar tekrar kullanabilmemizi sağlar.",
        "Ki bizlerde kendimizce evimizde plastikleri geri dönüştürebiliriz.",
        "Geri dönüşüm yapmak, doğal kaynaklarımızı korumamıza yardımcı olur. Örneğin, geri dönüştürülen bir plastik şişe, yeni bir şişe yapmak için gereken enerji ve su miktarını önemli ölçüde azaltır.",  
    
    await ctx.send(f"Geri dönüşümün önemix:\n- " + "\n- ".join(fikirler))

bot.run('TOKENİNİZİ_BURAYA_YAZIN')  
