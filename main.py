import json
import discord
from discord.ext import commands, tasks
from parser import GetCurrency

TOKEN = "" #SET YOUR TOKEN HERE
def main():
    client = commands.Bot(command_prefix = '/')

    @client.event
    async def on_ready():
        with open("config.ini","r") as f:
            configjson = f.read()
            f.close()
        if configjson == "":
            with open("config.ini","w")as f:    
                f.write("[]")
                f.close()
        print("Готов к работе!")

    
    @client.command()
    async def ping(ctx, arg=1):
        await ctx.send("pong "*arg)

    @client.command()
    async def whoami(ctx):
        await ctx.send(f"Nickname: {ctx.author.nick} \nID: {ctx.author.id}")

    @client.command()
    async def setupcurcheck(ctx):
        try:
            with open("config.ini","r") as f:
                configjson = json.loads(f.read())
                f.close()
            with open("config.ini", "w") as f:
                guild =  ctx.message.guild
                usd = await guild.create_voice_channel(name = "USD")
                eur = await guild.create_voice_channel(name = "EUR")
                configjson.append({"guild": guild.id,"usd":usd.id, "eur": eur.id})
                json.dump(configjson, f)
                f.close()
            await ctx.send("Функция настроена!")
        except Exception as e:
            await ctx.send("Что-то пошло не так...")
            await ctx.send("Ошибка: "+ str(e))
    
    @client.command()
    async def cancelcurcheck(ctx):
        try:
            with open("config.ini","r") as f:
                configjson = json.loads(f.read())
                f.close()
            with open("config.ini", "w") as f:
                guild = ctx.message.guild.id

                for i in configjson:
                    if i["guild"] == guild:
                        usdchannel = client.get_channel(i["usd"])
                        eurchannel = client.get_channel(i["eur"])
                        await usdchannel.delete()
                        await eurchannel.delete()
                        configjson.pop(configjson.index(i))
                json.dump(configjson, f)
                f.close()
            await ctx.send("Функция отключена!")
        except Exception as e:
            await ctx.send("Что-то пошло не так...")
            await ctx.send("Ошибка: "+ str(e))

    @tasks.loop(seconds=60)
    async def CheckCurrency():
        await client.wait_until_ready()
        with open("config.ini","r") as f:
            try:
                configjson = json.loads(f.read())
                for i in configjson:
                    try:
                        usdchannel = client.get_channel(i["usd"])
                        eurchannel = client.get_channel(i["eur"])
                        await usdchannel.edit(name = "USD: {0}".format(GetCurrency("usd")))
                        await eurchannel.edit(name = "EUR: {0}".format(GetCurrency("eur")))
                    except Exception:
                        continue
            except Exception:
                pass

    CheckCurrency.start()
    client.run(TOKEN)

if __name__ == '__main__':
    main()