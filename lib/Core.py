import constants
import lib.TriggerMessage as trigger
import lib.Log as Log
import random

t = trigger.TriggerMessage()

class Core():

    def __init__(self):
        self.message = None
        pass
        
    async def onMessageReceived(self, message):
        self.message = message

        if (t.checkTrigger(message.content, constants.TRIGGER_TYPE_PING)):
            Log.info("Trigger type: PING")
            await self.ping()
        """else:
            Log.info("Trigger type: NO_RESULTS")
            await self.no_results()"""

    async def onMemberJoin(self, member, oldInvites):
        Log.info("Event type: MEMBER_JOIN")
        newInvites = await member.guild.invites()
        code = ""
        
        for oi in oldInvites:
            for ni in newInvites:
                if (oi.code == ni.code):
                    # match codes, compare uses
                    if (oi.uses != ni.uses):
                        # right one
                        code = oi.code

        channels = member.guild.channels
        for c in channels:
            if (c.name == "join-logs"):
                await c.send(member.name + " - " + code)

    # choose random non-sense answer
    async def no_results(self):
        f = open(constants.NO_RESULTS_PATH, "r")
        fileArray = f.read().splitlines()

        await self.message.channel.send(random.choice(fileArray))

    async def ping(self):
        await self.message.channel.send("online")