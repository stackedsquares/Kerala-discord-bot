import os
import sys
import random
import json
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

token = os.getenv('DISCORD_TOKEN')
if token is None:
    sys.exit("DISCORD_TOKEN is not found. Please set the the DISCORD_TOKEN in the environment")

with open('responses.json', encoding='utf-8') as f:
    responses = json.load(f)['responses']


with open('shorthand.json', encoding='utf-8') as f:
    shorthand = json.load(f)['shorthand']


channel = None


@client.event
async def on_ready():
    print('Kunjappan is live')
    global channel, thunjan, introd, suggestions, stream, adimakann
    channel = client.get_channel(618270738247581708)
    thunjan = client.get_channel(620984507033714698)
    introd = client.get_channel(620985606042026005)
    suggestions = client.get_channel(620985649327112210)
    stream = client.get_channel(621683936061292545)
    adimakann = client.get_channel(621377580158943252)
    # await channel.send(f'ജീവനോടുണ്ടേ...\n Stayin\' Alive')


@client.event
async def on_member_join(member):
    print(f'{member} jas joined the server')
    await channel.send(f'Keri Vaa {member.name}.')
    await stream.send(f'{member.name}#{member.id}')


# @client.event
# async def on_message(adimakann.message):
#     #await adimakann.send(f'')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    await channel.send(f'Nandi {member.name}. Veendum varika :)')


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency *1000)} ms')


@client.command(name='kunja')
async def respond(ctx, *args):
    await ctx.send(f'{random.choice(responses)}')


@client.command(name='shaiju')
async def respond(ctx, *args):
    await ctx.send(f'Theerchayayum Shaiju')


@client.command(name='shaji')
async def respond(ctx, *args):
    await ctx.send(f'Ennekond pattumennu thonnunnilla Shajiyetta')


@client.command(name='aara')
async def respond(ctx, *args):
    await ctx.send(f'Ariyanmelanjitt chodikkuva... Nee Aaruva...')


@client.command(name='biri')
async def respond(ctx, *args):
    await ctx.send(f'Ini athava biriyani kittiyalo')


@client.command(name='thiru')
async def respond(ctx, *args):
    await ctx.send(f'Njan onnu Thiuvanthorathekk vilichotte')


@client.command(name='uda')
async def respond(ctx, *args):
    await ctx.send(f'Nee poda... Nee pande udayippa...')


@client.command(name='palli')
async def respond(ctx, *args):
    await ctx.send(f'Angu pallil poyi paranjal mathi')


@client.command(name='chena')
async def respond(ctx, *args):
    await ctx.send(f'Aanakaryathinidayilaano chenakkaryam')


@client.command(name='budhi')
async def respond(ctx, *args):
    await ctx.send(f'Budhiyillatha kuttiya... kshamichu kala')


@client.command(name='thantha')
async def respond(ctx, *args):
    await ctx.send(f'Njan ninte thanthayada thantha')


@client.command(name='bhay')
async def respond(ctx, *args):
    await ctx.send(f'Bhayankaram thanne')


@client.command(name='chetta')
async def respond(ctx, *args):
    await ctx.send(f'Muthalali oru chettayanu')


@client.command(name='idi')
async def respond(ctx, *args):
    await ctx.send(f'Ninte thalayil idithee veezhumeda kaalamada')


@client.command(name='pavam')
async def respond(ctx, *args):
    await ctx.send(f'Njan oru paavam alle... Enne ingane upadravikkamo...?')


@client.command(name='umma')
async def respond(ctx, *args):
    await ctx.send(f'Njan orumma thannal prashnam theerumo...')


@client.command(name='bilal')
async def respond(ctx, *args):
    await ctx.send(f'Kochi pazhaya Kochiyallennariyam... Pakshe Bilal pazhaya Bilal thanneya')


@client.command(name='cm')
async def respond(ctx, *args):
    await ctx.send(f'Mukyamanthri raaji vekkanam')


@client.command(name='oola')
async def respond(ctx, *args):
    await ctx.send(f'Nere poyi valathott thirinjal oolampaaraya... Avide chodichal mathi')


@client.command(name='patti')
async def respond(ctx, *args):
    await ctx.send(f'Ororo pattitheettangale')


if __name__ == '__main__':
    client.run(token)
