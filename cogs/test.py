from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *args):
        await ctx.send(' '.join(args))

    @commands.command()
    async def clear(self, ctx, arg = 1):
        await ctx.channel.purge(limit=arg + 1)
        
def setup(bot):
    bot.add_cog(Test(bot))