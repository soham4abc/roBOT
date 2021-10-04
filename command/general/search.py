import json
import discord
from discord.ext import commands
from duckduckgo_search import ddg
from googlesearch import search

class Search(commands.Cog):
    def __init__(self, client):
        self.client = client

    """
    ISSUE:
    it returns a dict
    and not the first result.
    someone fix it who is familiar with ddg
    """


    @commands.command()
    async def search(self, ctx, query):

        results = ddg(query, region = 'wt-wt', safesearch = 'Off', time = 'y', max_results = 1)[0]
        data = json.loads(str(results).replace("'", '"'))
        
        embed = discord.Embed(
            title = data['title'],
            color = discord.Color.blue(),
            description = data['body'],
            url = data['href'],
        )

        await ctx.send(embed=embed)
        await ctx.message.add_reaction("\U0001f44d")

    @commands.command()
    async def gsearch(self,ctx,*args):
        results = search('{}'.format(' '.join(args)),num_results=5, lang="en")
        em = discord.Embed(title="Google Search", color=0x212121)
        for links in results:
            em.add_field(name="Result",value=links, inline=False)
        await ctx.send(embed=em)


def setup(client):
    client.add_cog(Search(client))