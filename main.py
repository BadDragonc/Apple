import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

#variables

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    game = discord.Game("Being programmed..")
    await client.change_presence(activity=game)

    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        print(f"{message.author.name} sent: {message.content}")
        await client.get_user(509214395356676096).send(f"{message.author.name} sent: {message.content}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mention in message.content:
        await message.channel.send('apple')

    if 'apple' in message.content.lower() and message.author != client.user:
        await message.channel.send('There are more than 8,000 varieties of apples in the world.')

    if '!rng' in message.content.lower():

        await message.channel.send("Guess the number between 1-10...")
        number = random.randint(1,10)

        for i in range(0,3):
            guess = await client.wait_for('message', check=lambda message: message.author == message.author)

            if guess.content.isdigit():
                if int(guess.content) == number:
                    await message.channel.send("You got it hehehehar *hands you apple*")
                    break
                elif int(guess.content) < number:
                    await message.channel.send("it was higher >:(")
                elif int(guess.content) > number:
                    await message.channel.send("lower...")
                elif int(guess.content) < 1 or int(guess.content) > 10:
                    await message.channel.send('The number has to be in BETWEEN 1-10.')
            else:
                await message.channel.send("Invalid input buckaroo. Enter a number 1-10")

        else:
            await message.channel.send(f'You had a 10% chance and LOST you LOSERRRR HAHAHAHHA! The number was {number}.')


    #legit the only command I was too lazy to do... (I went on stack overflow for it)
    if message.content.startswith('!clear'):
        if not message.author.guild_permissions.administrator:
            await message.channel.send("You don't have permission to use this command.")
            return

        try:
            amount = int(message.content.split()[1])
        except:
            amount = 25

        if amount > 25:
            await message.channel.send("You can only clear up to 25 messages, {interaction.user.mention}")

        await message.channel.purge(limit=amount)

@client.tree.command(name="intro")
async def say(interaction: discord.Interaction):
    await interaction.response.send_message(f"Don\'t tell anyone {interaction.user.mention} I came from Memphis...", ephemeral=True)
