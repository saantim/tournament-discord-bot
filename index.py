import discord
import datetime
import tda_tournament
import random
from discord.ext import commands
from pkg_resources import register_finder

bot = commands.Bot(command_prefix='!', description='Bot de Prueba de Discord.py')

t = tda_tournament.Tournament_t()
#["santi","goku","perro","homero0","taza","cafe","coca","android"]
register_img = ['https://i.ytimg.com/vi/cMJxgpZXP1E/hqdefault.jpg',
                'https://i.ytimg.com/vi/2F7oL4n5U4I/hqdefault.jpg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnQ9V_mWaSNLHQ1eMWPIbjhgLZkqaEytK_UyyVvarlbZsU0CT-zOkJcmIv7fXCzGNJXiU&usqp=CAU',
                'https://pm1.narvii.com/6605/f02af9bd16414db84dde17c26eb2112072aa4641_hq.jpg',
                'https://pbs.twimg.com/media/E2-73yBWYAIE-oc.jpg',
                'https://pbs.twimg.com/media/E2-75MUWEAQlTrd.jpg',
                'https://i.ytimg.com/vi/tqDJTsxkWwQ/mqdefault.jpg',
                'https://img.wattpad.com/891a1bfc8684852e753d572aa2f1f473dfb300c9/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f5f6b34546d674b593774426c4a773d3d2d3531323430323836372e313530333964323537363661383232363330313738313133353139392e6a7067?s=fit&w=720&h=720',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL9WMeXmskSuNxYRdniPgk6ywS7DUio9GbRClwOgqF9T5Y4SZsfSHbIVTO4J_HG3M9ZzI&usqp=CAU',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYmZdOZAOEJ4B04hWwAmpoY_XWEBdBigln4E4IRwmU2qPwEux4yYhaMmgJc4svw1yAVVw&usqp=CAU',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLw5HPJYx60skfNX5gHV-1blB6Trt-zS5nFGSQiGKWgOmXbaawNNRFzEsWCKUjzsiPO9A&usqp=CAU',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXbnVKa33JVtgjK63iciOiZo_vKz9HDS-zSfleMONLhUGlnfTV4Tk0nTMiAbjzQGmwmTw&usqp=CAU'
                ]

announcer_img = ['https://pm1.narvii.com/6570/d4c3d2c58ff5d0bc5708491f5bd71ef56462fb89_hq.jpg',
                'https://i.ytimg.com/vi/URj7UpM88Ss/sddefault.jpg',   
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlXRvA79R77pg4FX5FkMtgqvqW5L2H0FvSgg&usqp=CAU',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyfvhTEIEuaKTpcVHZSwY9j9watwdNN4OgrqTeqb-JbCJHMaX8WjH7ewB314NamTkp77I&usqp=CAU',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBdTqH9MC-_4e9UOXD1oXejzbVqmunOeSOtQ&usqp=CAU',
                'https://i.ytimg.com/vi/hSbdOQc2UH0/mqdefault.jpg'
                ]

def embed_tournament(title, text, src_img):
    embed = discord.Embed(title= f'{title}', description= f'{text}', timestamp= datetime.datetime.utcnow(), color=discord.Color.orange())
    img = random.choice(src_img)
    embed.set_thumbnail(url=img)
    return embed

def list_players(players):
    text = "\n"
    for i, player in enumerate(players, start=1):
        text += f'{i} - {str(player)} \n'
    return text

def _draw_name(name):
    if len(name) > 8:
        return name[:9]
    for _ in range(8):
        name += " "
    return name[:9]

def draw_keys(brackets):
    output = ""
    sep = 0
    for bracket in brackets:
        i = 0
        for b in bracket:
            output += "     " * sep
            output += _draw_name(b)
            output += "     " * sep
            if i == 1:
                output += "|"
                i = 0
            else:
                i += 1
            if len(bracket) == 1:
                output += "CHAMPION!!!" 
        sep += 1 + sep
        output += "\n"
    return output

def draw_keysv2(t):

    output= f'\
|{_draw_name(t[0][0]) if len(t) > 0 else "?        "} ---|\n\
|                 vs--- {_draw_name(t[1][0]) if len(t) > 1 else "?        "}\n\
|{_draw_name(t[0][1]) if len(t) > 0 else "?        "} ---|          |\n\
|                           vs---  {_draw_name(t[2][0]) if len(t) > 2 else "?"}\n\
|{_draw_name(t[0][2]) if len(t) > 0 else "?        "} ---|          |             |\n\
|                 vs--- {_draw_name(t[1][1]) if len(t) > 1 else "?        "}         |\n\
|{_draw_name(t[0][3]) if len(t) > 0 else "?        "} ---|                        |\n\
|                                         vs --- {_draw_name(t[3][0]) if len(t) > 3 else "?"} < - CHAMPION!\n\
|{_draw_name(t[0][4]) if len(t) > 0 else "?        "} ---|                        |\n\
|                 vs--- {_draw_name(t[1][2]) if len(t) > 1 else "?        "}         |\n\
|{_draw_name(t[0][5]) if len(t) > 0 else "?        "} ---|          |             |\n\
|                           vs---  {_draw_name(t[2][1]) if len(t) > 2 else "?"}\n\
|{_draw_name(t[0][6]) if len(t) > 0 else "?        "} ---|          |\n\
|                 vs--- {_draw_name(t[1][3]) if len(t) > 1 else "?        "}\n\
|{_draw_name(t[0][7]) if len(t) > 0 else "?        "} ---| '

    return output

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def register(ctx, player):
    t.register(player)
    embed = embed_tournament("New Registration!!!", f'Player {player} succefully registered', register_img)
    await ctx.send(embed = embed)

@bot.command()
async def start(ctx):
    t.start()
    e = embed_tournament("The Tournament Begins!!!", f"Let's meet the tournament players!:{list_players(t.get_players())}", announcer_img)
    await ctx.send(embed = e)

@bot.command()
async def winner(ctx, player):
    try:
        t.set_winner(player)
        e = embed_tournament("We got a new fight winner!", f'{player} wins his battle!', announcer_img)
        await ctx.send(embed = e)
    except:
        await ctx.send("Player can't be a winner")

@bot.command()
async def players(ctx):
    players = list_players(t.get_players())
    e = embed_tournament("All this people are registered already!", f'{players}', announcer_img)
    await ctx.send(embed = e)

@bot.command()
async def next(ctx):
    player_1, player_2 = t.next_bracket()
    if not player_1:
        e = embed_tournament("No battle left!", 'See ya next tournament!', announcer_img)
        await ctx.send(embed = e)
    else:
        e = embed_tournament("Next battle!!!", f'This round {player_1} will face {player_2}', announcer_img)
        await ctx.send(embed = e)

@bot.command()
async def _debug(ctx):
    print(t)

@bot.command()
async def show(ctx):
    table = draw_keysv2(t.brackets)
    table = "'                  TOURNAMENT TABLE!!!                 \n" + table
    await ctx.send(table)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title= f'{ctx.guild.name}', description= "Description", timestamp= datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name= "server created at", value= f"{ctx.guild.created_at}")
    embed.add_field(name= "Server Owner", value= f"{ctx.guild.owner}")
    embed.add_field(name= "Server region", value= f"{ctx.guild.region}")
    embed.add_field(name= "Server ID", value= f"{ctx.guild.id}") 
    embed.set_thumbnail(url="https://pm1.narvii.com/6268/a8c705140e59bda64b5e9446fa36a6073ee97b2a_hq.jpg")
    await ctx.send(embed = embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity= discord.Streaming(name='TOURNAMENT!', url= "http://www.twitch.tv/accountname"))
    print("Bot Ready!")


bot.run('')

