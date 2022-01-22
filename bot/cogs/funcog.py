import random
import time
from discord.ext import commands
from datetime import datetime


class Fun(commands.Cog):
    def __init__(self, bot):
        self.lastfredsentence = datetime.now()
        self.bot = bot
    
    @commands.command(name='roll', aliases=['هاتو'])
    async def randomchoice(self, message):
        choices = message.content.split(',')
        choice = random.choice(choices)
        await message.channel.send("اذا مالي شغال عملي disconnect و رجاع شغلني")
    
    @commands.Cog.listener("on_message")
    async def on_message(self,message):
        if(message.content.startswith("بلعه ل")):
            if"موي" in message.content.split("بلعه ل", 1)[1]:
                await message.channel.send("المعلم ما بيبلع ولااااكك")
                return
            await message.channel.send("أمرك معلم")
            time.sleep(1)
            sentence = message.content.split("بلعه ل", 1)[1] + " بلاع"
            await message.channel.send(sentence)
        elif message.content.startswith(";;"):
            now = datetime.now()
            diff = self.lastfredsentence - now
            if diff < 15:
                return
            sentences = ['طيب شغلني يا عرص', 'طيب في واحد خرا بتقدر تشغله عفكرة', 'شو رأيك تشغلني و تعوف دينه لهداك؟','لك يا خرا شغلني الي', 'طلعوني من السيرفر شكلي مالي شغل', 'عم تخونني' ]
            await message.channel.send(random.choice(sentences))
            await message.channel.send("اذا مالي شغال عملي disconnect و رجاع شغلني")
            self.lastfredsentence = datetime.now()