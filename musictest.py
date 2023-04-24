from django.forms import URLField
from django.core.exceptions import ValidationError
import youtube_dl
import discord
from discord.ext import commands
from youtubesearchpython import *

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format = {'format': 'bestaudio'}

ytdl = youtube_dl.YoutubeDL(ytdl_format)

ffmpeg_options = {
    'before_options':
    '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def player(self, bot):
      pass
      
    @commands.command()
    async def join(self, ctx):

        canal = ctx.author.voice.channel
        canalbot = ctx.voice_client

        if canalbot is not None and canalbot != canal:
            await canalbot.move_to(canal)
        elif canal == None:
            await ctx.send('Você não está conectado em nenhum canal!')

        else:
            await canal.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.voice_client.disconnect().cleanup()

    @commands.command()
    async def play(self, ctx, *, music):
        musica = music
        self.join(self, ctx)
        validarURL = URLField()

        try:
          buscaVideo = CustomSearch(f'{x}', SearchMode.videos, limit=1)
          url = ytdl.extract_info(x, download=False)
          urlusable = url['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(
                urlusable, **ffmpeg_options)
          ctx.voice_client.play(source)

          embed = discord.Embed(
                title=f"{buscaVideo.result()['result'][0]['title']}",
                url=f"{x}",
                description='',
                color=discord.Color.green())

          embed.set_author(name=ctx.author.display_name,
                             icon_url=ctx.author.avatar_url)

          embed.set_thumbnail(
                url=
                f"{buscaVideo.result()['result'][0]['thumbnails'][0]['url']}",
            )

          embed.add_field(name='Duração: ',
                            value=buscaVideo.result()['result'][0]['duration'],
                            inline=True)

          embed.add_field(
                name='Visualizações: ',
                value=buscaVideo.result()['result'][0]['viewCount']['text'],
                inline=True)

          embed.add_field(
                name='Publicado: ',
                value=buscaVideo.result()['result'][0]['publishedTime'],
                inline=False)
          await ctx.send("**Tocando agora:**", embed=embed)

        except ValidationError:
            buscaVideo = CustomSearch(f"{musica}", SearchModvideos, limit=20)
            embed = discord.Embed(
                title=f"{buscaVideo.result()['result'][0]['title']}",
                url=f"{buscaVideo.result()['result'][0]['link']}",
                description='',
                color=discord.Color.green())

            embed1 = discord.Embed(title='Pesquisa no Youtube: ',
                                   description='',
                                   color=discord.Color.blue())

            embed1.add_field(name='Página 1/4', value='---------', inline=True)

            for x in range(4):
                embed1.add_field(
                    name=f"{x+1}: {buscaVideo.result()['result'][x]['title']}",
                    value=
                    f"duração: {buscaVideo.result()['result'][x]['duration']}",
                    inline=False)

            embed2 = discord.Embed(title='Pesquisa no Youtube: ',
                                   description='',
                                   color=discord.Color.blue())
            embed2.add_field(name='Página 2/4', value='---------', inline=True)

            for x in range(4, 8):
                embed2.add_field(
                    name=f"{x+1}: {buscaVideo.result()['result'][x]['title']}",
                    value=
                    f"duração: {buscaVideo.result()['result'][x]['duration']}",
                    inline=False)

            embed3 = discord.Embed(title='Pesquisa no Youtube: ',
                                   description='',
                                   color=discord.Color.blue())

            embed3.add_field(name='Página 3/4', value='---------', inline=True)

            for x in range(8, 12):
                embed3.add_field(
                    name=f"{x+1}: {buscaVideo.result()['result'][x]['title']}",
                    value=
                    f"duração: {buscaVideo.result()['result'][x]['duration']}",
                    inline=False)

            embed4 = discord.Embed(title='Pesquisa no Youtube: ',
                                   description='',
                                   color=discord.Color.blue())

            embed4.add_field(name='Página 4/4', value='---------', inline=True)
          
            for x in range(12, 16):
                embed4.add_field(
                    name=f"{x+1}: {buscaVideo.result()['result'][x]['title']}",
                    value=
                    f"duração: {buscaVideo.result()['result'][x]['duration']}",
                    inline=False)

            paginas = [embed1, embed2, embed3, embed4]
            messagem = await ctx.send(embed=embed1)

            await messagem.add_reaction('◀')
            await messagem.add_reaction('1️⃣')
            await messagem.add_reaction('2️⃣')
            await messagem.add_reaction('3️⃣')
            await messagem.add_reaction('4️⃣')
            await messagem.add_reaction('▶')

            def check(reaction, user):
                return user == ctx.author
              
            i = 0
            reaction = None

            while True:
                if str(reaction) == '◀':
                  if i > 0:
                    i -= 1
                    await messagem.edit(embed=paginas[i])
                  elif i == 0:
                    await ctx.send('Você já está na primeira página!')
                    return
                elif str(reaction) == '1️⃣':
                  for j in range(4):
                    if i == j:
                      x == 4 * j
                      url = buscaVideo.result()['result'][x]['link']
                      info = ytdl.extract_info(url, download=False)
                      urlusable = info['formats'][0]['url']
                      source = await discord.FFmpegOpusAudio.from_probe(
                      urlusable, **ffmpeg_options)
                      ctx.voice_client.play(source)

                      embed.title = f"{buscaVideo.result()['result'][x]['title']}"
                      embed.url = f"{buscaVideo.result()['result'][x]['link']}"
                      embed.set_author(name=ctx.author.display_name,
                                      icon_url=ctx.author.avatar_url)
                      embed.set_thumbnail(
                        url=
                        f"{buscaVideo.result()['result'][x]['thumbnails'][0]['url']}")
                      embed.add_field(
                        name='Duração: ',
                        value=buscaVideo.result()['result'][x]['duration'],
                        inline=True)
                      embed.add_field(name='Visualizações: ',
                        value=buscaVideo.result()['result'][x]
                        ['viewCount']['text'],
                        inline=True)
                      embed.add_field(name='Publicado: ',
                        value=buscaVideo.result()['result'][x]
                        ['publishedTime'],
                        inline=False)

                      await messagem.edit(embed=embed)
                
                elif str(reaction) == '2️⃣':
                  for j in range(4):
                    if i == j:
                      x == (4 * j) + 1
                      url = buscaVideo.result()['result'][x]['link']
                      info = ytdl.extract_info(url, download=False)
                      urlusable = info['formats'][0]['url']
                      source = await discord.FFmpegOpusAudio.from_probe(
                      urlusable, **ffmpeg_options)
                      ctx.voice_client.play(source)

                      embed.title = f"{buscaVideo.result()['result'][x]['title']}"
                      embed.url = f"{buscaVideo.result()['result'][x]['link']}"
                      embed.set_author(name=ctx.author.display_name,
                                      icon_url=ctx.author.avatar_url)
                      embed.set_thumbnail(
                        url=
                        f"{buscaVideo.result()['result'][x]['thumbnails'][0]['url']}")
                      embed.add_field(
                        name='Duração: ',
                        value=buscaVideo.result()['result'][x]['duration'],
                        inline=True)
                      embed.add_field(name='Visualizações: ',
                        value=buscaVideo.result()['result'][x]
                        ['viewCount']['text'],
                        inline=True)
                      embed.add_field(name='Publicado: ',
                        value=buscaVideo.result()['result'][x]
                        ['publishedTime'],
                        inline=False)

                      await messagem.edit(embed=embed)
                      
                elif str(reaction) == '3️⃣':
                  for j in range(4):
                    if i == j:
                      x == (4 * j) + 2
                      url = buscaVideo.result()['result'][x]['link']
                      info = ytdl.extract_info(url, download=False)
                      urlusable = info['formats'][0]['url']
                      source = await discord.FFmpegOpusAudio.from_probe(
                      urlusable, **ffmpeg_options)
                      ctx.voice_client.play(source)

                      embed.title = f"{buscaVideo.result()['result'][x]['title']}"
                      embed.url = f"{buscaVideo.result()['result'][x]['link']}"
                      embed.set_author(name=ctx.author.display_name,
                                      icon_url=ctx.author.avatar_url)
                      embed.set_thumbnail(
                        url=
                        f"{buscaVideo.result()['result'][x]['thumbnails'][0]['url']}")
                      embed.add_field(
                        name='Duração: ',
                        value=buscaVideo.result()['result'][x]['duration'],
                        inline=True)
                      embed.add_field(name='Visualizações: ',
                        value=buscaVideo.result()['result'][x]
                        ['viewCount']['text'],
                        inline=True)
                      embed.add_field(name='Publicado: ',
                        value=buscaVideo.result()['result'][x]
                        ['publishedTime'],
                        inline=False)

                      await messagem.edit(embed=embed)
                      
                elif str(reaction) == '4️⃣':
                  for j in range(4):
                    if i == j:
                      x == (4 * j) + 3
                      url = buscaVideo.result()['result'][x]['link']
                      info = ytdl.extract_info(url, download=False)
                      urlusable = info['formats'][0]['url']
                      source = await discord.FFmpegOpusAudio.from_probe(
                      urlusable, **ffmpeg_options)
                      ctx.voice_client.play(source)

                      embed.title = f"{buscaVideo.result()['result'][x]['title']}"
                      embed.url = f"{buscaVideo.result()['result'][x]['link']}"
                      embed.set_author(name=ctx.author.display_name,
                                      icon_url=ctx.author.avatar_url)
                      embed.set_thumbnail(
                        url=
                        f"{buscaVideo.result()['result'][x]['thumbnails'][0]['url']}")
                      embed.add_field(
                        name='Duração: ',
                        value=buscaVideo.result()['result'][x]['duration'],
                        inline=True)
                      embed.add_field(name='Visualizações: ',
                        value=buscaVideo.result()['result'][x]
                        ['viewCount']['text'],
                        inline=True)
                      embed.add_field(name='Publicado: ',
                        value=buscaVideo.result()['result'][x]
                        ['publishedTime'],
                        inline=False)

                      await messagem.edit(embed=embed)
                      
                elif str(reaction) == '▶':
                    if i < 4:
                        i += 1
                        await messagem.edit(embed=paginas[i])
                elif str(reaction) == '▶':
                    if i == 4:
                        await ctx.send('Você já está na última página!')
                        return
                try:
                    reaction, user = await self.bot.wait_for('reaction_add',
                                                             timeout=30.0,
                                                             check=check)
                    await messagem.remove_reaction(reaction, user)
                except:
                    break

            await messagem.clear_reactions()

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client == None:
            await ctx.send('Já não estou tocando nada.')
        else:
            ctx.voice_client.stop()

    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()


def setup(bot):
    bot.add_cog(music(bot))
