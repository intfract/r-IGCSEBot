from bot import bot, discord
from constants import GUILD_ID, WELCOME_CHANNEL_ID, UNVERIFIED_ROLE, BETA

welcome_embed = discord.Embed.from_dict({'color': 3066993, 'type': 'rich', 'description': "Hello and welcome to the official r/IGCSE Discord server, a place where you can ask any doubts about your exams and find help in a topic you're struggling with! We strongly suggest you read the following message to better know how our server works!\n\n***How does the server work?***\n\nThe server mostly entirely consists of the students who are doing their IGCSE and those who have already done their IGCSE exams. This server is a place where you can clarify any of your doubts regarding how exams work as well as any sort of help regarding a subject or a topic in which you struggle.\n\nDo be reminded that academic dishonesty is not allowed in this server and you may face consequences if found to be doing so. Examples of academic dishonesty are listed below (the list is non-exhaustive) - by joining the server you agree to follow the rules of the server.\n\n> Asking people to do your homework for you, sharing any leaked papers before the exam session has ended, etc.), asking for leaked papers or attempted malpractice are not allowed as per *Rule 1*. \n> \n> Posting pirated content such as textbooks or copyrighted material are not allowed in this server as per *Rule 7.*\n\n***How to ask for help?***\n\nWe have subject helpers for every subject to clear any doubts or questions you may have. If you want a subject helper to entertain a doubt, you should use the command `/helper` in the respective subject channel. A timer of **15 minutes** will start before the respective subject helper will be pinged. Remember to cancel your ping once a helper is helping you!\n\n***How to contact the moderators?***\n\nYou can contact us by sending a message through <@861445044790886467> by responding to the bot, where it will be forwarded to the moderators to view. Do be reminded that only general server inquiries should be sent and other enquiries will not be entertained, as there are subject channels for that purpose.", 'title': 'Welcome to r/IGCSE!'})


@bot.event
async def on_member_join(member: discord.Member):
    if not BETA and member.guild.id == GUILD_ID: 
        await member.send(embed=welcome_embed)
        welcome = member.guild.get_channel(WELCOME_CHANNEL_ID)
        await welcome.send(f"Welcome {member.mention}! Pick up your subject roles from <id:customize> to get access to subject channels and resources!")
        unverified_role = member.guild.get_role(UNVERIFIED_ROLE)
        if not unverified_role in member.roles:
            await member.add_roles(unverified_role)