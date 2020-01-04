import discord
import asyncio


async def ex(ctx, amount=1):
    await ctx.chanel.purge(limit=amount)