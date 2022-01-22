import random
from discord.ext import commands
import time
class Fun(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
  
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
      else:
          if message.content.startswith(";;"):
              sentences = ['طيب شغلني يا عرص', 'طيب في واحد خرا بتقدر تشغله عفكرة', 'شو رأيك تشغلني و تعوف دينه لهداك؟','لك يا خرا شغلني الي', 'طلعوني من السيرفر شكلي مالي شغل', 'عم تخونني' ]
              time.sleep(20)
              await message.channel.send(random.choice(sentences))
              await message.channel.send("اذا مالي شغال عملي disconnect و رجاع شغلني")