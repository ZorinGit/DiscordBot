import discord
import database_functions


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# embed
title = "Bot Name"
desc = """Short Description"""
top = "Title"
lines = """Long Description"""

# Important Secret Variables
CH_ID = "COMMAND CHANNEL ID"
ID = "YOUR DISCORD ID"
TOKEN = "SECRET BOT TOKEN"


@client.event
async def on_ready():
    print(f"BOT HAS LOGGED IN @ {database_functions.get_datetime_for_logs()}")
    await client.change_presence(activity=discord.Game(name="BOT COMMAND TO DISPLAY INSTRUCTIONS"))


def number_to_list(number):
    number_list = []
    for numeral in str(number):
        number_list.append(numeral)
    return number_list


@client.event
async def on_message(message):
    # bot ignores it's own messages
    if message.author == client.user:
        return

    # testing and monitoring commands for owner in command channel
    if message.channel.id == int(CH_ID):
        if message.author.id == int(ID):

            if message.content == '!test':
                await message.channel.send("test")

            if message.content == '!chan_joined_len':
                await message.channel.send(database_functions.count_servers())

            if message.content == '!purge':
                guilds = client.guilds
                guild_ids = [guild.id for guild in guilds]

                server_IDs = database_functions.get_all_serverIDs()
                print("\n")
                print(f"databaseIDs: {server_IDs}")
                print(f"bot is in servers: {guild_ids}")
                print("\n")


                for server_ID in server_IDs:
                    print(f"checking: {server_ID}")
                    try:
                        if server_ID in guild_ids:
                            print(f"{server_ID} is OK!")
                            print("\n")
                        else:
                            print(f"deleting {server_ID}")
                            print("\n")
                            database_functions.delete_server_entry(server_ID)
                    except Exception as e:
                            print(f"Error occurred for server ID {server_ID}: {e}")
                            continue
                await message.channel.send("purged!")
                print(f"purged! @ {database_functions.get_datetime_for_logs()}")


    # bot describes it's functions on request
    if message.content == "BOT COMMAND TO DISPLAY INSTRUCTIONS":
        about = discord.Embed(title=title, description=desc, color=0x7359B6)
        about.add_field(name=top, value=lines)
        await message.channel.send(embed=about)

    # main functionality for managing the game
    if message.channel.name == "game":
        combo = discord.utils.get(message.guild.text_channels, name="game")
        messages =[]
        async for msg in combo.history(limit=2):
            messages.append(msg)
        guild_id = message.guild.id
        count = database_functions.get_count(guild_id)

        if messages[0].content == messages[1].content and not messages[0].author.id == messages[1].author.id:
            count += 1
            database_functions.update_count(guild_id, count)

            await message.add_reaction('✅')

            for num_index in range(len(number_to_list(count))):
                if number_to_list(count)[num_index] == '0':
                    await message.add_reaction('0️⃣')
                if number_to_list(count)[num_index] == '1':
                    await message.add_reaction('1️⃣')
                if number_to_list(count)[num_index] == '2':
                    await message.add_reaction('2️⃣')
                if number_to_list(count)[num_index] == '3':
                    await message.add_reaction('3️⃣')
                if number_to_list(count)[num_index] == '4':
                    await message.add_reaction('4️⃣')
                if number_to_list(count)[num_index] == '5':
                    await message.add_reaction('5️⃣')
                if number_to_list(count)[num_index] == '6':
                    await message.add_reaction('6️⃣')
                if number_to_list(count)[num_index] == '7':
                    await message.add_reaction('7️⃣')
                if number_to_list(count)[num_index] == '8':
                    await message.add_reaction('8️⃣')
                if number_to_list(count)[num_index] == '9':
                    await message.add_reaction('9️⃣')

            if count == 69:
                await message.add_reaction('🇴')
                await message.add_reaction('🇭')
                await message.add_reaction('🇾')
                await message.add_reaction('🇪')
                await message.add_reaction('🇦')
                await message.add_reaction('‼️')

            if count == 666:
                await message.add_reaction('🤘')
                await message.add_reaction('👺')
                await message.add_reaction('😈')
                await message.add_reaction('👿')
                await message.add_reaction('👹')
                await message.add_reaction('🤟')

        else:
            if int(count) > 0:
                last_author = message.author.name
                await message.add_reaction('❌')
                await message.channel.send(f'combo is broken! \nfinal length : {count} \n{last_author} did it 😈')
                count = 0
                database_functions.update_count(guild_id, count)


# add or delete entires when the bot joins or leaves a server
@client.event
async def on_guild_join(guild):
    channel = client.get_channel(int(CH_ID))
    await channel.send(f'joined: {guild.id}')
    database_functions.create_server_entry(guild.id)


@client.event
async def on_guild_remove(guild):
    channel = client.get_channel(int(CH_ID))
    await channel.send(f'left: {guild.id}')
    database_functions.delete_server_entry(guild.id)


client.run(TOKEN)