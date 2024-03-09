import discord
from botOyun import tas_kagıt_makas_oyunu
from model import detect_arduino


intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('HELLO LORD'):
        await message.channel.send("HI! :grinning:")
    elif message.content.startswith('I NEED SOME HELP'):
        await message.channel.send(":star:TAŞ KAĞIT MAKAS OYUNU İÇİN 'RPS GAME' YAZABİLİRSİNİZ""\n"":star:RESİM ÇİZMESİNİ İSTİYORSANIZ VE SEÇENEKLERİ GÖRMEK İSTİYORSANIZ 'PICTURE' YAZABİLİRSİNİZ""\n"":star:HELLO LORD""\n"":star:HOW CAN I CHAT WITH YOU""\n"":star:HOW ARE YOU""\n"":star:THANK YOU""\n"":star:GOOD BYE LORD""\n""gibi ifadeler kullanırsan Lord'dan karşılık alabilirsin.")
        await message.channel.send(":warning::bangbang::no_entry:UYARI: BU KALIPLAR HARİÇ BİR GİRİŞ YAPTIĞINDA LORD BOT SANA GİRDİĞİN ŞEYİ ÇIKTI OLARAK TEKRAR SANA GÖNDERECEKTİR")
    elif message.content.startswith("PICTURE"):
        await message.channel.send("PAINT 1"" |"" PAINT 2 ""|"" PAINT 3""\n""PAINT 4"" | ""PAINT 5 ""| ""PAINT 6""\n""PAINT 7 ""| ""PAINT 8"" |"" PAINT 9")
    elif message.content.startswith('PAINT 1'):
        await message.channel.send("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""\n""░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░""\n""░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░""\n""░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░""\n""░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░""\n""░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░""\n""░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░""\n""░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░""\n""░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░""\n""░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░""\n""░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░""\n""░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░""\n""░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░""\n""░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░""\n""░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░""\n""░░░░█░░░░░░░░░░░░░░░░░░░░░█░░""\n""░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░""\n""░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░""\n""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    elif message.content.startswith('PAINT 2'):
        await message.channel.send("\t"" ▔▔▔▔▔╲""\n""▕╮╭┻┻╮╭┻┻╮╭▕╮╲""\n""▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏""\n""▕╭┻┻┻┛┗┻┻┛ ▕ ╰▏""\n""▕╰━━━┓┈┈┈╭╮▕╭╮▏""\n""▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏""\n""▕╰╯┈┗┛┗┛┈╭╮▕╮┈")
    elif message.content.startswith('PAINT 3'):
        await message.channel.send("╭━┳━╭━╭━╮╮""\n""┃┈┈┈┣▅╋▅┫┃""\n""┃┈┃┈╰━╰━━━━━━╮""\n""╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣""\n""╲┃┈┈┈┈┈┈┈┈┈▉▉▉""\n""╲┃┈┈┈┈┈┈┈┈┈◥▉◤""\n""╲┃┈┈┈┈╭━┳━━━━╯""\n""╲┣━━━━━━┫﻿")
    elif message.content.startswith('PAINT 4'):
        await message.channel.send("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""\n""░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░""\n""░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░""\n""░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░""\n""░█░░░▄██▄░░░░▄██▄░░░░▄██▄░░░█░""\n""░█░░░▀██▀░░░░▀██▀░░░░▀██▀░░░█░""\n""░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░""\n""░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░""\n""░░▀▄▄▄▄░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀░░""\n""░░░░░░█░░░░█░░░░░░░░░░░░░░░░░░""\n""░░░░░█░░░▄▀░░░░░░░░░░░░░░░░░░░""\n""░░░░▄▀▀▀▀░░░░░░░░░░░░░░░░░░░░░""\n""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    elif message.content.startswith('PAINT 5'):
        await message.channel.send("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───""\n""───█▒▒░░░░░░░░░▒▒█───""\n""────█░░█░░░░░█░░█────""\n""─▄▄──█░░░▀█▀░░░█──▄▄─""\n""█░░█─▀▄░░░░░░░▄▀─█░░█""\n""█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█""\n""█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█""\n""█░░║║║╠─║─║─║║║║║╠─░░█""\n""█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█""\n""█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    elif message.content.startswith('HOW CAN I CHAT WITH YOU'):
        await message.channel.send("You can use everyday chat phrases :speaking_head:")
    elif message.content.startswith('HOW ARE YOU'):
        await message.channel.send("FINE AND YOU")
    elif message.content.startswith('THANK YOU'):
        await message.channel.send("YOU'RE WELCOME")
    elif message.content.startswith('GOOD BYE LORD'):
        await message.channel.send("SEE YOU LATER :wave:")
    elif message.content.startswith('RPS GAME'):
        await message.channel.send("\t""-_-ŞANS OYUNU TAŞ KAĞIT MAKAS-_-")
        await message.channel.send("AŞAĞIDA AÇILAN EKRANDAN SEÇİMİNİ YAP VE""\n""OYUNU KAZANMAYA ÇALIŞ. UNUTMA TAMAMEN ŞANS OYUNU :)")
        await message.channel.send("SEÇİMİNİ YAP...:(TAŞ İÇİN 'TAS', KAĞIT İÇİN 'KAGIT', MAKAS İÇİN 'MAKAS' YAZINIZ")
    elif message.content.startswith("TAS"):
        result = tas_kagıt_makas_oyunu("TAS")
        await message.channel.send(result)
    elif message.content.startswith("KAGIT"):
        result = tas_kagıt_makas_oyunu("KAGIT")
        await message.channel.send(result)
    elif message.content.startswith("MAKAS"):
        result = tas_kagıt_makas_oyunu("MAKAS")
        await message.channel.send(result)
    else:
        await message.channel.send(message.content)



client.run("ODI4MTg2MTA4NzU1MDUwNTI2.GsIjXL.ArzCyu2qXbDhxbA83tG9zAUL-ykiG-UUx_99Dc")