import youtube_dlc
import discord
import asyncio
import functools
from discord.ext import commands

youtube_dlc.utils.bug_reports_message = lambda: ''

class YTDLError(Exception):
    pass

class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
        'cookies': 'youtube-cookies.txt'
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dlc.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data
        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        if self.title is not None:
            return '**{0.title}** by **{0.uploader}**'.format(self)
        else:
            return "No title available"

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()
        if search.startswith('https') or search.startswith('https'):
            required = "https://youtu.be/SIhv4bPiq6s"
            partial = functools.partial(cls.ytdl.extract_info, url=required, download=False)
            data = await loop.run_in_executor(None, partial)
            print("Finished")
            if data is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))
            else:
                info = data
                return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)
        else:
            required = f"ytsearch:{search}"
            partial = functools.partial(cls.ytdl.extract_info, url=required, download=False)
            print("Start search")
            data = await loop.run_in_executor(None, partial)
            print("Finished")
            if data is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

            if 'entries' not in data and not search.startswith('انا عبد'):
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))
            else:
                print("Try get info")
                info = data['entries'][0]
                return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)