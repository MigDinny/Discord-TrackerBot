import discord
import lib.Log as Log
import lib.Core as core

c = core.Core()

class EventHandler(discord.Client):

    def EventHandler(self):
        self.invites = None

    async def on_ready(self):
        Log.info("Connection made successfully")
        Log.info("Event Handler is ready")

        if (len(self.guilds) > 1): Log.warning("Connected to multiple guilds - might trigger unwanted effects")

        self.invites = await self.guilds[0].invites()
        

    async def on_message(self, message):
        if (message.author == self.user): return
        await c.onMessageReceived(message)

    async def on_member_join(self, member):
        await c.onMemberJoin(member, self.invites)
        self.invites = await self.guilds[0].invites()
            
            
        