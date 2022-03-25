# Project Acta Mea by Alex Arbuckle #


# import <
from os import path
from json import load, dump
from discord import Intents
from discord.ext import commands

# >


# global <
path = path.realpath(__file__).split('/')
directory = '/'.join(path[:(len(path) - 1)])
token = ''
actaMea = commands.Bot(

    command_prefix = '',
    intents = Intents.all()

)

# >


def jsonLoad(file: str):
    '''  '''

    # get file <
    # get data <
    with open(f'{directory}{file}', 'r') as fin:

        return load(fin)

    # >


def jsonDump(file: str, data: dict):
    '''  '''

    # set file <
    # set data <
    with open(f'{directory}{file}', 'w') as fout:

        dump(data, fout, indent = 3)

    # >


async def setFunction(ctx, data: dict, key: str, args) -> dict:
    '''  '''

    # if ((key in data) and (value not in data)) <
    if ((key in data.keys()) and (args[0] not in data[key].keys())):

        # set node <
        # delete message <
        data[key][args[0]] = ' '.join(args[1:])
        await ctx.message.delete()

    # >

    # output <
    return data

    # >


async def getFunction(ctx, data: dict, key: str, value: str) -> None:
    '''  '''

    # if (key and value in data) <
    if ((key in data.keys()) and (value in data[key].keys())):

        # get node <
        # delete message <
        await ctx.send(data[key][value], delete_after = 60)
        await ctx.message.delete()

        # >

    # >


async def delFunction(ctx, data: dict, key: str, value: str) -> dict:
    '''  '''

    # if (key and value in data) <
    if ((key in data.keys()) and (value in data[key].keys())):

        # del node <
        # delete message <
        del data[key][value]
        await ctx.message.delete()

        # >

    # >

    # output <
    return data

    # >


async def showFunction(ctx, data: dict, key: str):
    '''  '''

    # if (key in data) <
    if (key in data.keys()):

        # send array <
        # delete message <
        await ctx.send('\n'.join(k for k in data[key].keys()), delete_after = 60)
        await ctx.message.delete()

        # >

    # >


@commands.has_permissions(administrator = True)
@actaMea.command(aliases = jsonLoad(file = '/actaMea.json')['aliases'])
async def commandFunction(ctx, key, *args):
    '''  '''

    # load <
    data = jsonLoad(file = '/actaMea.json')

    # >

    # if (show) <
    # elif (get, set or del) <
    if (ctx.invoked_with.lower() == 'show'): await showFunction(ctx, data, key)
    elif (ctx.invoked_with.lower() == 'get'): await getFunction(ctx, data, key, args[0])
    elif (ctx.invoked_with.lower() == 'set'): data = await setFunction(ctx, data, key, args)
    elif (ctx.invoked_with.lower() == 'del'): data = await delFunction(ctx, data, key, args[0])

    # >

    # dump <
    jsonDump(file = '/actaMea.json', data = data)

    # >


# main <
if (__name__ == '__main__'):

    actaMea.run(token)

# >


# I Love You #
