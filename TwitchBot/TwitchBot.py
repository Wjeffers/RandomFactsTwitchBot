import os
import random
from twitchio.ext import commands

class Bot(commands.Bot):
    

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        # channels object holds streamer/s channel names for bot to join their chat
        # create an otoken.txt file to hold your bot's private oauth token

        channels = []
        with open('otoken.txt', 'r') as f:
            otoken = f.read()
        
        super().__init__(token=otoken, prefix='?', initial_channels=channels)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()    
    async def rndm(self, ctx: commands.Context):
        #Here we have the command rndm, this reads from our text file of facts split by new lines and returns one at random.
        with open('facts.txt', 'r') as f:
            content = f.read()
        Facts = content.split('\n')
        await ctx.send(f'Hello {ctx.author.name}, {random.choice(Facts)}')


bot = Bot()
bot.run()