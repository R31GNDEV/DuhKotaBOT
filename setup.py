import asyncio
import os

import mongoengine
from dotenv import find_dotenv, load_dotenv

from data.model.guild import Guild

load_dotenv(find_dotenv())

async def setup():
    print("STARTING SETUP...")
    guild = Guild()

    # you should have this setup in the .env file beforehand
    guild._id          = int(os.environ.get("MAIN_GUILD_ID"))

    # If you're re-running this script to update a value, set case_id
    # to the last unused case ID or else it will start over from 1!
    guild.case_id      = 1

    # required for permissions framework!
    guild.role_administrator = 1018609543971885056  # put in the role IDs for your server here
    guild.role_moderator     = 1025299807302078504  # put in the role IDs for your server here
    guild.role_birthday      = 1025297892925243393  # put in the role IDs for your server here
    guild.role_sub_mod       = 1018609616755626034  # put in the role IDs for your server here
    guild.role_genius        = 1025299268745056317  # put in the role IDs for your server here
    guild.role_dev           = 1025298021979787274  # put in the role IDs for your server here
    guild.role_memberone     = 1025300540533514280 # put in the role IDs for your server here
    guild.role_memberedition = 1025298167228547092  # put in the role IDs for your server here
    guild.role_memberpro     = 1025298451837243392  # put in the role IDs for your server here
    guild.role_memberplus    = 1025298318932312075  # put in the role IDs for your server here
    guild.role_memberultra   = 1025298500029792288  # put in the role IDs for your server here

    guild.channel_reports        = 1025290702306947152  # put in the channel IDs for your server here
    # channel where reactions will be logged
    guild.channel_emoji_log      = 1025290702306947152  # put in the channel IDs for your server here
    # channel for private mod logs
    guild.channel_private        = 1025290702306947152  # put in the channel IDs for your server here
    # channel where self-assignable roles will be posted
    guild.channel_reaction_roles = 1018278587020890142  # put in the channel IDs for your server here
    # rules-and-info channel
    guild.channel_rules          = 1018278238864281681  # put in the channel IDs for your server here
    # not required
    guild.channel_applenews      = 1025301839954063401  # put in the channel IDs for your server here
    # channel for public mod logs
    guild.channel_public         = 1025290702306947152 # put in the channel IDs for your server here
    # optional, used for /subnrews command or something
    guild.channel_common_issues  = 1006692824118472829  # put in the channel IDs for your server here
    # #general, required for permissions
    guild.channel_general        =  1006692824118472829 # put in the channel IDs for your server here
    # required for filter
    guild.channel_development    = 1018280651251781743  # put in the channel IDs for your server here
    # required, #bot-commands channel
    guild.channel_botspam        = 1018280651251781743  # put in the channel IDs for your server here
    # optional, needed for booster #emote-suggestions channel
    guild.channel_booster_emoji  = 1018280651251781743  # put in the channel IDs for your server here

    # you can fill these in if you want with IDs, or you ca use commands later
    guild.logging_excluded_channels = []  # put in a channel if you want (ignored in logging)
    guild.filter_excluded_channels  = []  # put in a channel if you want (ignored in filter)
    guild.filter_excluded_guilds    = []  # put guild ID to whitelist in invite filter if you want

    guild.nsa_guild_id = 1018609543971885056 # you can leave this as is if you don't want Blootooth (message mirroring system)

    guild.save()
    print("DONE")

if __name__ == "__main__":
    if os.environ.get("DB_CONNECTION_STRING") is None:
        mongoengine.register_connection(
            host=os.environ.get("DB_HOST"), port=int(os.environ.get("DB_PORT")), alias="default", name="botty")
    else:
        mongoengine.register_connection(
            host=os.environ.get("DB_CONNECTION_STRING"), alias="default", name="botty")
    res = asyncio.get_event_loop().run_until_complete( setup() )
