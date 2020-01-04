import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------------')


bot.remove_command('help')



@bot.command()
async def info(ctx):

    embed = discord.Embed(title="osiris", description="bot du conseil", color=0xeee657)

    # give info about you here

    embed.add_field(name="dévellopeur", value="aro20")

    # Shows the number of servers the bot is member of.

    embed.add_field(name="serveur connecté avec osiris", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server

    embed.add_field(name="Invite", value="non")
    embed.add_field(name="droits", value="administrateur")

    await ctx.send(embed=embed)


@bot.command()
async def help(ctx): # faire que seul les rangs 4 et le chef y accede

    embed = discord.Embed()

    embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)
    embed.add_field(name="!kick", value="Kick the user of this server", inline=False)
    embed.add_field(name="!ban", value="Ban the user of this server", inline=False)



    await ctx.send(embed=embed)


@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    #await cmd_clear.ex()

bot.run(os.environ.get('token'))
