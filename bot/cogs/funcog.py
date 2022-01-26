import random
import time
from discord.ext import commands
from datetime import datetime


class Fun(commands.Cog):
    def __init__(self, bot):
        self.lastfredsentence = datetime.now()
        self.bot = bot
    
    @commands.command(name='roll', aliases=['هاتو'])
    async def randomchoice(self, ctx: commands.Context, *, message: str):
        choices = message.split(',')
        choice = random.choice(choices)
        await ctx.send(choice)
    
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
            if diff.seconds < 40:
                return
            sentences = ['طيب شغلني يا عرص', 'طيب في واحد خرا بتقدر تشغله عفكرة', 'شو رأيك تشغلني و تعوف دينه لهداك؟','لك يا خرا شغلني الي', 'طلعوني من السيرفر شكلي مالي شغل', 'عم تخونني' ]
            await message.channel.send(random.choice(sentences))
            await message.channel.send("صرت شغال انا عفكرة بدون تصليح")
            self.lastfredsentence = datetime.now()
        elif message.content.startswith("ايري ب"):
            if"موي" in message.content:
                await message.channel.send("المعلم ما بيبلع ولااااكك")
                return
            sentences = ['حصل بصراحة', 'اتفق', 'فعلا', 'له له', 'لك طول بالك يا زلمة', 'يا عيب الشوم', 'معك حق', '++']
            await message.channel.send(random.choice(sentences))
        elif message.content.startswith("عبد كول خرا"):
            sentences = ['بتأمر معلم', 'بتمون انت', 'طيب خلص لا تصرعنا', 'طيب اوكي', 'طيب شو دخلني لك عيسى', 'أمرك', 'ملطشة يلي خلقك لأني', 'لك انت كول خرا ولا']
            await message.channel.send(random.choice(sentences))