import subprocess
import sys

import discord
import interactions
from discord import app_commands
from discord.ext import commands, tasks
import os
import random
import responses
import requests, json, random
import asyncio
import choice
import webbrowser
import codecs
import now
import string
from datetime import datetime
import urllib.parse, urllib.request, re
import time
from itertools import cycle
import functools
from random import choice
from datetime import datetime
import sqlite3
from keep_alive import keep_alive


con = sqlite3.connect('level.db')
cur = con.cursor()

import io
import colorama
from colorama import Fore
from flask import Flask
from threading import Thread
from discord import client, Button, ButtonStyle
from discord import guild

intents = discord.Intents.all()
intents.presences = True
intents.members = True
#####################
######## CORE #######
#####################

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

bot = discord.Client(intents=intents)
bot = commands.Bot(".", intents=intents)

tts_language = "en"

bot.copycat = None
bot.remove_command('help')


@bot.command()
async def hi(ctx):
    await ctx.send("hi!")

    # List of GIF URLs
    gif_urls = [
        "https://example.com/gif1.gif",
        "https://example.com/gif2.gif",
        "https://example.com/gif3.gif",
        # Add more GIF URLs as needed
    ]


import discord
import random


@bot.command()
async def howac(ctx):
    # Generate a random percentage for the Assassin level
    assassin_percentage = random.randint(0, 100)

    # Create an embed
    embed = discord.Embed(
        title=f"{ctx.author.display_name}'s Assassin Level",
        description=f"{ctx.author.mention} is {assassin_percentage}% Assassin 🥷",
        color = 0x84DAFF
    )

    embed.set_image(url="https://media.discordapp.net/attachments/1157770692054487111/1158453119877922989/gip_2.gif?ex=651c4d0a&is=651afb8a&hm=5814e8b9c3d28a2237dad8dbc95892c2825312d15531ff949834a0971e4d2775&=&width=600&height=337")
    # Send the embed message
    await ctx.send(embed=embed)


mainshop = [{"name": "TomaHawk", "price": 150, "description": "", "category": "Weapons"},
    {"name": "AltairSuit", "price": 500, "description": "", "category": "Skins"},
    {"name": "Jacob", "price": 750, "description": "", "category": "Weapons"}]
    # Add more items with their respective categories here]


@bot.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance! 🪙 ', color=discord.Color.blue())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name='Bank Balance', value=bank_amt)

    em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    await ctx.send(embed=em)


@bot.command()
async def battle(ctx, opponent: discord.Member):
    outcomes_and_gifs = {
        "You were on a fight with {opponent} and you knifed his neck!": [
            "https://media.discordapp.net/attachments/1158878665040478389/1159224674966851715/R.gif?ex=65303f1b&is=651dca1b&hm=96ee0f0ff401cf83bedff866c6f2b48bd2cd02a86bf26e6e3c3a87266cae871e&=&width=625&height=212"

        ]
    }

    outcome_text = random.choice(list(outcomes_and_gifs.keys())).format(opponent=opponent.mention)
    gif_urls = outcomes_and_gifs[outcome_text]
    gif_url = random.choice(gif_urls)

    # Create an embed message
    embed = discord.Embed(
        title="Battle Outcome",
        description=outcome_text,
        color=discord.Color.green() if "won" in outcome_text else discord.Color.red()
    )

    # Set the GIF URL in the embed
    embed.set_image(url=gif_url)

    await ctx.send(embed=embed)





















# Load user data from users.json
def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save user data to users.json
def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

@bot.command()
async def lvlleaderboard(ctx, *, option='level'):
    users = load_users()
    
    if option == 'level':
        # Sort users by level
        sorted_users = sorted(users.items(), key=lambda x: x[1]['level'], reverse=True)
        leaderboard_text = "Leaderboard by Level:\n"
    elif option == 'experience':
        # Sort users by experience
        sorted_users = sorted(users.items(), key=lambda x: x[1]['experience'], reverse=True)
        leaderboard_text = "Leaderboard by Experience:\n"
    else:
        await ctx.send("Invalid option. Use `!leaderboard level` or `!leaderboard experience`.")
        return
    
    # Create an embed for the leaderboard
    embed = discord.Embed(title=f"Leaderboard - {option.capitalize()}", color=discord.Color.blue())
    
    # Generate leaderboard text and add it to the embed
    for index, (user_id, user_data) in enumerate(sorted_users, start=1):
        user = bot.get_user(int(user_id))
        leaderboard_text += f"{index}. {user.name} - Level {user_data['level']} - Experience {user_data['experience']}\n"
        if index == 10:  # Limiting the leaderboard to the top 10 users
            break
    
    embed.description = leaderboard_text
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    users = load_users()
    user_id = str(message.author.id)
    
    # Update user data
    if user_id not in users:
        users[user_id] = {'experience': 0, 'level': 1}
    
    # ... Add logic to gain experience and level up here ...
    
    save_users(users)
    
    await bot.process_commands(message)





# Define possible response choices
response_choices = [
    "Ezio and he gave you 🪙 **(amount)**",
    "Altair while crying, and he gave you 🪙 **(amount)**",
    "Arno and got 🪙 **(amount)**",
]

@bot.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    # Randomly select a response choice
    response_choice = random.choice(response_choices)

    # Replace '(amount)' with the actual earnings
    response_choice = response_choice.replace("(amount)", f"{earnings}")

    embed = discord.Embed(
        title=f"Begging.. 🙏",
        description=f"{ctx.author.mention} Congrats! You Begged {response_choice} **Helix credits**! `Very proud of you son` 🍷",
        color=discord.Color.green()
    )

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)

    await ctx.send(embed=embed)


@bot.command(aliases=['with'])
async def withdraw(ctx, amount=None, current_datetime=None):
    await open_account(ctx.author)

    if amount is None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, 'bank')

    # Get the current date and time
    current_datetime = datetime.now()

    embed = discord.Embed(
        title="**✅ Withdrawing Credits**",
        description=f'{ctx.author.mention} You withdrew 🪙 **{amount} Helix Credits**',
        color=discord.Color.green()

    )
    embed.set_footer(text=f'As of {current_datetime.strftime("%Y-%m-%d %H:%M:%S")}')

    await ctx.send(embed=embed)










@bot.command(aliases=['dep'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)

    if amount is None:
        await ctx.send("`Please enter the amount` 🥷")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('**Amount must be positive!** 🥷')
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, 'bank')

    embed = discord.Embed(
        title="🪙 **Deposit Credits**",
        description=f'{ctx.author.mention} You deposited 🪙 **{amount} Helix Credits**',
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)



@bot.command(aliases=['sn'])
async def send(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, -1 * amount, 'bank')
    await update_bank(member, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You Gave {member} 🪙 **{amount} Helix Credits**!')


# Function to create a blue embed
def create_blue_embed(title, description, ctx):
    embed = discord.Embed(title=title, description=description, color=discord.Color.blue())
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    return embed



# Define the cooldown duration in seconds (2 hours)
COOLDOWN_DURATION = 2700

# Define a custom error for the cooldown
class CooldownError02(commands.CommandError):
    pass

# Add the cooldown decorator to the hunt command

# Command to rob a member
@bot.command(aliases=['ro'])
@commands.cooldown(1, COOLDOWN_DURATION, commands.BucketType.user)
async def rob(ctx, member: discord.Member):
    # Define your open_account, update_bank, and other functions here if not already defined
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)

    if bal[0] < 100:
        embed = create_blue_embed('Robbing Attempt', 'It is useless to rob him :(', ctx)
        await ctx.send(embed=embed)
        return

    earning = random.randrange(0, bal[0])

    await update_bank(ctx.author, earning)
    await update_bank(member, -1 * earning)
  

    embed = create_blue_embed('Rob Successful', f'{ctx.author.mention} You robbed {member} and got 🪙 **{earning}** Helix Credits', ctx)
   
    await ctx.send(embed=embed)

weekly_claimed = {}

@bot.command()
async def weekly(ctx):

    user_id = ctx.author.id
  

    # Check if the user has claimed their weekly salary in the past week
    if user_id in weekly_claimed and weekly_claimed[user_id] + 1500 >= ctx.message.created_at.timestamp():
        await ctx.send("You've already claimed your weekly salary this week.")
    else:
        # Simulate a random salary amount (you can modify this as needed)
        salary = random.randint(100, 1000)


        embed = discord.Embed(title="Weekly Salary Claimed", color=0x00ff00)
        embed.add_field(name="Success", value=f"You successfully claimed your weekly salary of ${salary}!")
        await ctx.send(embed=embed)

        # Update the timestamp for the user's weekly claim
        weekly_claimed[user_id] = ctx.message.created_at.timestamp()



  # Define an error handler for the CooldownError
@rob.error
async def rob_error(ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
          # Calculate the remaining cooldown time
          remaining_time = round(error.retry_after)
          await ctx.send(f"You're on cooldown for {remaining_time} seconds. Please try again later.")
      else:
          # Handle other errors
          await ctx.send(f"An error occurred: {error}")





@bot.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)

    if amount is None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    symbols = ['🍒', '🍋', '🍇','🎰','🍎']  # Emojis for the slot symbols
    final = [random.choice(symbols) for _ in range(3)]

    slot_result = ' '.join(final)  # Display the slot results using emojis

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        win_amount = 2 * amount
        await update_bank(ctx.author, win_amount)
        message = f'You won 🪙 {win_amount} **Helix Credits**! {ctx.author.mention} 🎉'
    else:
        lose_amount = -1 * amount
        await update_bank(ctx.author, lose_amount)
        message = f'You lose 🪙 **{amount} Helix Credits**. Better luck next time! {ctx.author.mention} 😔'

    embed = discord.Embed(
        title="🎰 Slotting!",
        description=f'{slot_result}\n\n{message}',
        color=discord.Color.green()
    )

    await ctx.send(embed=embed)





# Define a custom error for the cooldown
class CooldownError(commands.CommandError):
    pass

# Create a dictionary to store user cooldown data
user_cooldowns = {}

# Define a constant for the command cooldown duration
COOLDOWN_DURATION = 7200

# Define a constant for the number of times a user needs to trigger the cooldown to be banned
BAN_THRESHOLD = 2

# Define a constant for the ban duration in seconds (2 days)
BAN_DURATION = 2 * 24 * 60 * 60

# Add the cooldown decorator to the work command
@bot.command()
async def work(ctx):
    # Check if the user is in the cooldown dictionary
    if ctx.author.id in user_cooldowns:
        # Check if the user has reached the ban threshold
        if user_cooldowns[ctx.author.id]["count"] >= BAN_THRESHOLD:
            # Ban the user for the specified duration
            await ctx.send("You are banned from using the work command for 2 days.")
            await asyncio.sleep(BAN_DURATION)
            # Remove the user from the cooldown dictionary after the ban is lifted
            del user_cooldowns[ctx.author.id]
            return
        else:
            # Calculate the remaining cooldown time
            remaining_time = user_cooldowns[ctx.author.id]["timestamp"] + COOLDOWN_DURATION - int(time.time())
            if remaining_time > 0:
                await ctx.send(f"You're on cooldown for {remaining_time} seconds. Please try again later.")
                return

    # List of job opportunities
    jobs = [
        {"name": "As Altair in Stealth", "min_earnings": 350, "max_earnings": 800},
        {"name": "On Edward's Jackdaw damaged armor, fixed it", "min_earnings": 500, "max_earnings": 700},
        {"name": "As Basim", "min_earnings": 480, "max_earnings": 750},
        {"name": "On Arno's Hidden Blade To Fix It", "min_earnings": 480, "max_earnings": 750},
        {"name": "In Jacobs Factory", "min_earnings": 480, "max_earnings": 750},
        {"name": "On Edwards House", "min_earnings": 480, "max_earnings": 750},
        {"name": "As Ezio In The Darkness", "min_earnings": 400, "max_earnings": 700},
        # Add more job opportunities as needed
    ]

    job = random.choice(jobs)
    earnings = random.randint(job["min_earnings"], job["max_earnings"])

    # Simulate earning money and update the user's bank
    await update_bank(ctx.author, earnings)

    embed = discord.Embed(
        title="🥷 Working..",
        description=f'{ctx.author.mention} You worked {job["name"]} and earned 🪙 **{earnings} Helix Credits**!')

    await ctx.send(embed=embed)

    # Update the user's cooldown data in the dictionary
    if ctx.author.id in user_cooldowns:
        user_cooldowns[ctx.author.id]["count"] += 1
        user_cooldowns[ctx.author.id]["timestamp"] = int(time.time())
    else:
        user_cooldowns[ctx.author.id] = {"count": 1, "timestamp": int(time.time())}

# Define an error handler for the CooldownError
@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        # Calculate the remaining cooldown time
        remaining_time = round(error.retry_after)
        await ctx.send(f"You're on cooldown for {remaining_time} seconds. Please try again later.")
    else:
        # Handle other errors
        await ctx.send(f"An error occurred: {error}")





@bot.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await bot.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))

    if lvl_start < lvl_end:
        channel_id = 1066849406357344326  # Replace with your desired channel ID
        channel = message.guild.get_channel(channel_id)  # Fetch the channel by its ID

        if channel:
            embed = discord.Embed(
                title=f'{user.display_name} has leveled up!',
                description=f'Great job, {user.mention}! You are now at level {lvl_end} 🥷',
                color=0x00ff00
            )
            embed.set_footer(text='Keep going bro! 🤺🔥')
            embed.set_image(url="https://media.discordapp.net/attachments/1158878665040478389/1159082002096590878/daeAGsjkmkscuz9c6krRVF_1.jpg?ex=651e96bc&is=651d453c&hm=c64dc291dfcfefe92a26b827&=&width=807&height=77")
            await channel.send(embed=embed)
        
        users[f'{user.id}']['level'] = lvl_end

@bot.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        embed = discord.Embed(
            title="Your Level ⬆️",
            description=f'**You are at level** **{lvl}** keep grinding bud 🤺!',
            color = 0x00000

        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)


        await ctx.send(embed=embed)
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        embed = discord.Embed(
            title=f"{member}'s Level",
            description=f'{member} is at level **{lvl}**!',
            color=member.color
        )
        await ctx.send(embed=embed)






@bot.command()
async def shop(ctx):
    em = discord.Embed(title="Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        category = item.get("category", "Uncategorized")  # Get the category or default to "Uncategorized"
        em.add_field(name=name, value=f"🪙 HELIX CREDITS `{price}` | {desc}")

    em.set_image(url="https://media.discordapp.net/attachments/1158878665040478389/1159935694005882930/maxresdefault.jpg?ex=6532d54c&is=6520604c&hm=dfe13647be98b475febb62fd5d05f518277705a01e630ef4d41557aa2568f1e9&=&width=1070&height=601")
  
    await ctx.send(embed=em)



# Define the cooldown duration in seconds (2 hours)
COOLDOWN_DURATION = 7200

# Define a custom error for the cooldown
class CooldownError(commands.CommandError):
    pass

# Add the cooldown decorator to the hunt command
@bot.command()
@commands.cooldown(1, COOLDOWN_DURATION, commands.BucketType.user)
async def hunt(ctx):
    # List of animals that can be hunted
    animals = ["🦌 deer", "🐻 bear", "🐅 tiger", "🐆 leopard"]

    # Randomly select an animal from the list
    hunted_animal = random.choice(animals)

    # Determine the outcome of the hunt (success or failure)
    hunt_success = random.choice([True, False])

    # Prepare the embed message
    embed = discord.Embed(
        title="You went hunting and encountered a wild animal!",
        color=discord.Color.green() if hunt_success else discord.Color.red()
    )
    embed.add_field(
        name="🏹",
        value=f"You found a **{hunted_animal}** in the wilderness.\n{'You successfully hunted it down!' if hunt_success else 'Unfortunately, it got away.'}",
        inline=False
    )

    # Set a footer with the user's name and avatar
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)









# Define an error handler for the CooldownError
@hunt.error
async def hunt_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        # Calculate the remaining cooldown time
        remaining_time = round(error.retry_after)
        await ctx.send(f"You're on cooldown for {remaining_time} seconds. Please try again later.")
    else:
        # Handle other errors
        await ctx.send(f"An error occurred: {error}")

@bot.command()
async def buy(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have enough credits in your wallet to buy {amount} {item}")
            return

    await ctx.send(f"Congrats! You just bought **{amount}** {item} **✅**")


@bot.command()
async def inv(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title="**Your Items**")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]


@bot.command()
async def sell(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1] == 3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"Sad! 🥺 You just sold **{amount} {item}**.")


async def sell_this(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost, "wallet")

    return [True, "Worked"]


@bot.command(aliases=["rich"])
async def richest(ctx, x=1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(title=f"Top {x} Richest People",
                       description="This is decided on the basis of raw money in the bank and wallet",
                       color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed=em)


# ----------------------------------------------------

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open('mainbank.json', 'r') as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)
    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank']
    return bal


@bot.event
async def on_ready():
    activity = discord.Game(name="AC REBORN V1!", type=3)
    await bot.change_presence(activity=discord.Game(name="Assassin's Creed Mirage | .help"))
    print("Bot is ready!")



@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help Panel", description='developer: JamezssYT, contact if any bugs found!', color=0xFFFFFF)
    embed.add_field(name='.help 🆘', value="This shows you all of the available help commands example: fun, games, economy, etc.")
    embed.add_field(name='.utility ⚙️', value="general commands to use.")
    embed.add_field(name='.fun 💀', value="Fun commands, examples: 8ball - answer a given question.")
    embed.add_field(name='.games 🕹️', value="Gaming commands, examples: mission - go on a mission and earn a trophy.")
    embed.add_field(name='.economy 🤑', value="Money-based commands, examples: work, bal, rob, dep")
   

    # Replace 'YOUR_INVITE_LINK' with your bot's invitation link
    invite_link = f"https://discord.com/api/oauth2/authorize?client_id=1158148924402565251&permissions=8&scope=bot"
    embed.set_footer(text=f'🥷 | Version 1.0.0 BETA ✅')

    await ctx.send(embed=embed)


@bot.command()
async def fun(ctx):
    embed = discord.Embed(title="Fun Commands", description="list of all fun commands",

                          )

    embed.add_field(name='.howac', value="percentage of how ac you are")
    embed.add_field(name='.8ball', value="an answer based on your question")
    embed.set_image(
        url="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/e35d8c47287397.5875eef53f061.jpg")

    await ctx.send(embed=embed)

 



@bot.command()
async def games(ctx):
    embed = discord.Embed(title="Gaming Commands", description="list of all gaming commands",

                          )
    
    embed.add_field(name='.actoe', value="2 players tictactoe ac game")
    embed.add_field(name='.mission', value="play a mission and earn a achievement")
    embed.set_image(
        url="https://th.bing.com/th/id/R.0620046106bb34dac4bad5c0ce0147ca?rik=%2fiRfBUSCdki5dw&riu=http%3a%2f%2fwww.pixelstalk.net%2fwp-content%2fuploads%2f2016%2f05%2fLogo-assassins-creed-emblem-wallpapers-sign.jpg&ehk=%2fkQCHgemZXKZW80Bhp%2beO%2fgAvslwb1FE4VrnhCodtSU%3d&risl=1&pid=ImgRaw&r=0")
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)


@bot.command()
async def actoe(ctx, opponent: discord.Member):
    if ctx.author == opponent:
        await ctx.send("You cannot play against yourself!")
        return

    # Create a blank Tic-Tac-Toe board
    board = ['⬜', '⬜', '⬜',
             '⬜', '⬜', '⬜',
             '⬜', '⬜', '⬜']

    # Initialize the players
    player1 = ctx.author
    player2 = opponent

    # Create a dictionary to map positions to board indices
    position_to_index = {
        '1': 0, '2': 1, '3': 2,
        '4': 3, '5': 4, '6': 5,
        '7': 6, '8': 7, '9': 8
    }

    # Create a function to display the current board as an embed
    def display_board():
        board_str = ''
        for i, cell in enumerate(board):
            board_str += cell
            if (i + 1) % 3 == 0:
                board_str += '\n'
        embed = discord.Embed(title='Tic-Tac-Toe', description=board_str, color=0x00ff00)
        return embed

    # Send the initial board as an embed
    message = await ctx.send(embed=display_board())

    # Game loop
    current_player = player1
    while '⬜' in board:
        try:
            # Wait for the current player to make a move
            await ctx.send(f'{current_player.mention}, choose a position (1-9):')

            def check_move(message):
                return message.author == current_player and message.content in ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            move_msg = await client.wait_for('message', check=check_move, timeout=30.0)
            position = move_msg.content

            # Check if the move is valid
            if board[position_to_index[position]] == '⬜':
                board[position_to_index[position]] = '🥷' if current_player == player1 else '🤺'
                await message.edit(embed=display_board())

                # Check for a win
                win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
                for pattern in win_patterns:
                    if all(board[i] == '🥷' for i in pattern):
                        await ctx.send(f'{player1.mention} wins! 🎉')
                        return
                    elif all(board[i] == '🤺' for i in pattern):
                        await ctx.send(f'{player2.mention} wins! 🎉')
                        return

                # Switch to the other player's turn
                current_player = player1 if current_player == player2 else player2

            else:
                await ctx.send('Invalid move! Please choose an empty cell (1-9).')

        except asyncio.TimeoutError:
            await ctx.send('The game has ended due to inactivity.')
            return

    # If the board is full and there is no winner, it's a tie
    await ctx.send('It\'s a tie! 😕')




def display_board(board):
    embed = discord.Embed(title='Tic-Tac-Toe', color=0x00ff00)
    embed.add_field(name='1️⃣ 2️⃣ 3️⃣', value=f'{board[0]} {board[1]} {board[2]}', inline=False)
    embed.add_field(name='4️⃣ 5️⃣ 6️⃣', value=f'{board[3]} {board[4]} {board[5]}', inline=False)
    embed.add_field(name='7️⃣ 8️⃣ 9️⃣', value=f'{board[6]} {board[7]} {board[8]}', inline=False)
    return embed











@bot.command()
async def economy(ctx):
    embed = discord.Embed(title='Economy Commands', description="list of all economy commands",

                          )

    embed.add_field(name='.bal', value="shows your balance and bank")
    embed.add_field(name='.work', value="work and earn credits")
    embed.add_field(name='.pickpocket', value="steals member's items")
    embed.add_field(name='.hunt', value="hunts an animal")
    embed.add_field(name='.beg', value="begs and earn coins")
    embed.add_field(name='.rob', value="robs members coins")
    embed.add_field(name='.shop', value="items to buy at shop")
    embed.add_field(name='.inv', value="shows your bought items")
    embed.add_field(name='.send', value="sends member coins")
    embed.add_field(name='.dep', value="deposits from the bank")
    embed.add_field(name='.slots', value="bet your money and try to earn more")
    embed.add_field(name='.withdraw', value="withdraws coins")
    embed.add_field(name='.petstore', value="buy pets you like")
    embed.add_field(name='.buypet', value="feed your pets, play with them")
    embed.add_field(name='.play', value="play with your pet and increase happiness")
    embed.add_field(name='.feed', value="feed your pet")
    embed.add_field(name='.buy', value="buys item from the shop")
    embed.add_field(name='.sell', value="sells the item")
    color = 0x000000
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    embed.set_image(url="https://media.discordapp.net/attachments/1158878665040478389/1158890800831287418/apps.31083.68164954561423838.0e17ca7c-dc16-4e8e-af0d-151a46e32d6e.jpeg?ex=651de4aa&is=651c932a&hm=aef9d246fe8a177f27e9d04e52207a0f27107a0cac9c39b9fa73bf0c945052ef&=&width=1033&height=581")
    await ctx.send(embed=embed)




# Load user data from the mainbank.json file
def load_user_data(user_id):
    try:
        with open("mainbank.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    return data.get(str(user_id), {"wallet": 0, "bank": 0, "bag": []})

# Save user data to the mainbank.json file
def save_user_data(user_id, data):
    with open("mainbank.json", "r") as f:
        all_data = json.load(f)
    
    all_data[str(user_id)] = data

    with open("mainbank.json", "w") as f:
        json.dump(all_data, f, indent=4)

@bot.command()
async def use(ctx, item_name: str):
    user_id = ctx.author.id
    user_data = load_user_data(user_id)
    user_items = user_data.get("bag", [])

    for item in user_items:
        if item.get("item") == item_name and item.get("amount") > 0:
            # Use the item (replace this with your desired item functionality)
            # For demonstration purposes, we'll just send an embed message.
            embed = discord.Embed(
                title="Item In Use! 🤺",
                description=f"You just used one of your **{item_name}** on {ctx.author.mention} and killed him with it!",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

            # Remove one of the used item from the user's inventory
            item["amount"] -= 1

            # Save the updated data
            save_user_data(user_id, user_data)

            # Send the embed message
            await ctx.send(embed=embed)
            return

    # If the user doesn't have the specified item or the quantity is zero
    embed = discord.Embed(
        title="Item Not Found",
        description=f"You don't have any **{item_name}** to use.",
        color=discord.Color.red()
    )
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

    # Send the embed message
    await ctx.send(embed=embed)











def load_user_data():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user data to a JSON file
def save_user_data(data):
    with open("users.json", "w") as file:
        json.dump(data, file)


@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    # Load user data from the JSON file
    user_data = load_user_data()

    # Check if the user exists in the user_data dictionary
    if str(member.id) in user_data:
        user_info = user_data[str(member.id)]
        level = user_info.get("level", 1)
    else:
        level = 1

    # Create an embed to display user information
    embed = discord.Embed(title="User Info", color=0x00ff00)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="User ID", value=member.id, inline=True)
    embed.add_field(name="Level", value=level, inline=True)
    embed.set_footer(text=f"✅ Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)



@bot.command()
async def utility(ctx):
    embed = discord.Embed(title='Util Commands', description="list of all utility commands",

                          )

    embed.add_field(name='.ping', value="checks the bots latency")
    embed.add_field(name='.uptime', value="checks how long the bots running")
    embed.add_field(name='.userinfo', value="checks user's id and level & more")
    embed.add_field(name='.lvlleaderboard', value="shows all the members levels they have")
    color = 0x000000
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    embed.set_image(url="https://media.discordapp.net/attachments/1158878665040478389/1159247191148339231/R_4.jpeg?ex=65305414&is=651ddf14&hm=596c88e157c074c2999eef13659f8dd0e273fa614e925e23b5b0b44435e211a1&=&width=1038&height=583")
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(bot.latency * 1000)}ms')

# Record the bot's start time
start_time = datetime.now()

@bot.command()
async def uptime(ctx):
    current_time = datetime.now()
    uptime = current_time - start_time
    uptime_str = str(uptime)

    embed = discord.Embed(
        title="Bot's Uptime 🥷",
        description=f"**Bot has been running for `{uptime_str}`**",
        color=discord.Color.green()
    )
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    embed.set_image(url="https://media.discordapp.net/attachments/1158878665040478389/1159593041502408864/ac_u_clock_teaser_1.webp?ex=6531962d&is=651f212d&hm=0a3a6d396737d978e1387961aa740bd54962e0c428eec8140e3c34910c6b9a1a&=&width=1177&height=410")

    await ctx.send(embed=embed)



# Load user data from the mainbank.json file
def load_user_data(user_id):
    try:
        with open("mainbank.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    return data.get(str(user_id), {"wallet": 0, "bank": 0, "bag": []})

# Save user data to the mainbank.json file
def save_user_data(user_id, data):
    with open("mainbank.json", "r") as f:
        all_data = json.load(f)
    
    all_data[str(user_id)] = data

    with open("mainbank.json", "w") as f:
        json.dump(all_data, f, indent=4)

@bot.command()  # 1 week cooldown
async def pickpocket(ctx, target: discord.Member):
    try:
        if target == ctx.author:
            await ctx.send("You can't pickpocket yourself!")
            return

        user_data = load_user_data(target.member.id)
        user_items = user_data.get("bag", [])

        if not user_items:
            # Send a DM to the command author with the result
            pickpocket_result = f"{target.display_name} doesn't have any items to steal."
            await ctx.author.send(f"Pickpocket Result: {pickpocket_result}", delete_after=10)
            return

        # Send a DM to the command author with a simplified result message
        pickpocket_result = f"You attempted to pickpocket {target.display_name}, but nothing happened."
        await ctx.author.send(f"Pickpocket Result: {pickpocket_result}", delete_after=10)
    
    except Exception as e:
        print(e)  # Print the error for debugging
        await ctx.send("this command is under work.")


  
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  
  responses = [
  discord.Embed(title='It is certain.'),
  discord.Embed(title='It is decidedly so.'),
  discord.Embed(title='Without a doubt.'),
  discord.Embed(title='Yes - definitely.'),
  discord.Embed(title='You may rely on it.'),
  discord.Embed(title='Most likely.'),
  discord.Embed(title='Outlook good.'),
  discord.Embed(title='Yes.'),
  discord.Embed(title='Signs point to yes.'),
  discord.Embed(title='Reply hazy, try again.'),
  discord.Embed(title='Ask again later.'),
  discord.Embed(title='Better not tell you now.'),
  discord.Embed(title='Cannot predict now.'),
  discord.Embed(title='Concentrate and ask again.'),
  discord.Embed(title="Don't count on it."),
  discord.Embed(title='My reply is no.'),
  discord.Embed(title='My sources say no.'),
  discord.Embed(title='Outlook not very good.'),
  discord.Embed(title='Very doubtful.')
    ]
  responses = random.choice(responses)
  await ctx.send(content=f'Question: {question}\nAnswer:', embed=responses)







# Load achievements from the JSON file
try:
    with open("achievements.json", "r") as f:
        achievements = json.load(f)
except FileNotFoundError:
    achievements = {}

# List of Assassin's Creed Unity-inspired achievements
achievement_names = [
    "Master Assassin",
    "Paris Explorer",
    "Silent But Deadly",
    "Stealthy Shadow",
    "Revolutionary Hero",
    "Eagle Vision Pro",
    "Parkour Expert",
    "Arno's Mentor",
    "Secrets Unveiled",
    "Unity in Chaos",
    "Cafe Theatre Owner",
    "Legendary Outfit",
]

# List of random mission names
mission_names = [
    "Assassination",
    "Infiltration",
    "Heist",
    "Reconnaissance",
    "Sabotage",
    "Rescue",
    "Espionage",
]

# List of random mission outcomes
mission_outcomes = [
    "found keys to templar's hideout and went there, killed all of them while using smoke bombs with hidden blades, then ran away",
    "sneaked in stealth, stole the keys, and ran away",
    "discovered a secret passage, ambushed the guards, and successfully escaped",
]

# Cooldown time in seconds (24 hours)
cooldown_time = 24 * 60 * 60

# Dictionary to store mission cooldowns
mission_cooldowns = {}

@bot.command()
async def earn_achievement(ctx, achievement_name):
    user_id = str(ctx.author.id)

    if user_id not in achievements:
        achievements[user_id] = []

    if achievement_name not in achievements[user_id]:
        achievements[user_id].append(achievement_name)
        await ctx.send(f"Congratulations, {ctx.author.mention}, you've earned the {achievement_name} achievement!")

        # Save achievements to the JSON file
        with open("achievements.json", "w") as f:
            json.dump(achievements, f, indent=4)
    else:
        await ctx.send(f"{ctx.author.mention}, you've already earned the {achievement_name} achievement!")

@bot.command()
async def my_achievements(ctx):
    user_id = str(ctx.author.id)

    if user_id in achievements:
        await ctx.send(f"{ctx.author.mention}, your achievements: {', '.join(achievements[user_id])}")
    else:
        await ctx.send(f"{ctx.author.mention}, you haven't earned any achievements yet.")

@bot.command()
@commands.cooldown(1, cooldown_time, commands.BucketType.user)
async def mission(ctx):
    user_id = str(ctx.author.id)
    mission_name = random.choice(mission_names)

    if user_id not in achievements:
        achievements[user_id] = []

    # Check if the user already has all the achievements
    if len(achievements[user_id]) == len(achievement_names):
        await ctx.send(f"{ctx.author.mention}, you've already earned all available achievements!")
        return

    # Check if the user is on cooldown
    if user_id in mission_cooldowns:
        remaining_time = cooldown_time - (int(time.time()) - mission_cooldowns[user_id])
        remaining_hours, remainder = divmod(remaining_time, 3600)
        remaining_minutes, remaining_seconds = divmod(remainder, 60)
        
        cooldown_embed = discord.Embed(
            title="Cooldown",
            description=f"{ctx.author.mention}, you are on cooldown for the mission command.\n"
                        f"Remaining time: {remaining_hours} hours, {remaining_minutes} minutes, {remaining_seconds} seconds",
            color=discord.Color.red()
        )
        await ctx.send(embed=cooldown_embed)
        return

    # Create an initial mission embed message
    mission_embed = discord.Embed(
        title="Mission in Progress",
        description=f"{ctx.author.mention}, you went on a mission to {mission_name}. Please wait until it's finished...",
        color=discord.Color.blue()
    )

    # Send the initial mission embed and store the message object
    mission_msg = await ctx.send(embed=mission_embed)

    # Store the mission start time
    mission_cooldowns[user_id] = int(time.time())

    await asyncio.sleep(5)  # Simulate mission duration (you can adjust the delay)

    # Edit the mission message with the completed mission and achievement earned
    achievement_name = random.choice(achievement_names)
    mission_outcome = random.choice(mission_outcomes)

    if achievement_name not in achievements[user_id]:
        achievements[user_id].append(achievement_name)

        # Create the "Mission Completed" embed
        mission_completed_embed = discord.Embed(
            title="Mission Results",
            description=f"{ctx.author.mention} completed the {mission_name} mission, {mission_outcome}!",
            color=discord.Color.green()
        )
        mission_completed_embed.add_field(name="Achievement Earned", value=achievement_name)

        # Use await mission_msg.edit to update the message with the new embed
        await mission_msg.edit(embed=mission_completed_embed)

        # Save achievements to the JSON file
        with open("achievements.json", "w") as f:
            json.dump(achievements, f, indent=4)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = cooldown_time - (int(time.time()) - mission_cooldowns[str(ctx.author.id)])
        remaining_hours, remainder = divmod(remaining_time, 3600)
        remaining_minutes, remaining_seconds = divmod(remainder, 60)
        
        cooldown_embed = discord.Embed(
            title="Cooldown",
            description=f"{ctx.author.mention}, Woah slow down bud, you are on cooldown for the mission command.\n"
                        f"Remaining time: {remaining_hours} hours, {remaining_minutes} minutes, {remaining_seconds} seconds",
            color=discord.Color.red()
        )
        await ctx.send(embed=cooldown_embed)

# Define other commands as needed...




# Define loot box names and their possible contents
loot_boxes = {
    "White": ["SimpleSwords", "SimplePistols", "ArnoSkinWhite"]
    # Add more loot boxes and items as needed
}

# Function to load user data from a JSON file
def load_user_data():
    try:
        with open('mainkbank.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Function to save user data to a JSON file
def save_user_data(user_data):
    with open('mainkbank.json', 'w') as f:
        json.dump(user_data, f, indent=4)

@bot.command()
async def open_lootbox(ctx, box_name):
    user_id = str(ctx.author.id)
    user_data = load_user_data()

    if box_name in loot_boxes:
        items = random.choice(loot_boxes[box_name])
        color = discord.Color.green()  # Embed color for success
        message = f"You opened {box_name} and found: {items}"

        # Add the looted item to the user's bag
        if user_id not in user_data:
            user_data[user_id] = {"wallet": 1289, "bank": 9999, "bag": []}
        
        user_bag = user_data[user_id]["bag"]
        found_item = False

        for item in user_bag:
            if item["item"] == items:
                item["amount"] += 1
                found_item = True
                break
        
        if not found_item:
            user_bag.append({"item": items, "amount": 1})

        # Save the updated user data to the JSON file
        save_user_data(user_data)
    else:
        color = discord.Color.red()  # Embed color for failure
        message = "Invalid loot box name"

    # Create an embed with the specified color
    embed = discord.Embed(description=message, color=color)
    await ctx.send(embed=embed)







# Define a pet store with available pets and their prices
pet_store = {
    "dog": 100,
    "cat": 150,
    "eagle": 250,
    "hamster": 200,
}

# Function to create a pet status embed
def create_pet_embed(pet):
    embed = discord.Embed(title=f"{pet['name'].capitalize()}'s Status", color=discord.Color.green())
    embed.add_field(name="Hunger", value=f"{pet['hunger']}%", inline=True)
    embed.add_field(name="Happiness", value=f"{pet['happiness']}%", inline=True)
    return embed


# Define the 'petstatus' command to check the status of a specific virtual pet

@bot.command()
async def petstatus(ctx, *, pet_name: str):
    user_id = ctx.author.id
    pet_name = pet_name.lower()

    # Load virtual pets from the JSON file
    virtual_pets = load_virtual_pets()

    if user_id in virtual_pets and virtual_pets[user_id]['name'] == pet_name:
        pet = virtual_pets[user_id]
        embed = create_pet_embed(pet)
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=discord.Embed(description="You don't have a pet with that name. Use `.store` to see available pets or `.buypet` to buy one.", color=discord.Color.red()))

    # Save virtual pets back to the JSON file after checking status
    save_virtual_pets(virtual_pets)











# Function to create a pet store embed
def create_store_embed():
    embed = discord.Embed(title="Pet Store 🐇", color=discord.Color.blue())
    for pet, price in pet_store.items():
        embed.add_field(name=pet.capitalize(), value=f"Price: **🪙 {price}**", inline=True)
    return embed

# Function to save virtual pets to the JSON file
def save_virtual_pets(virtual_pets):
    with open("pet_store.json", "w") as file:
        json.dump(virtual_pets, file)

# Function to load virtual pets from the JSON file (called at the start of your bot)
def load_virtual_pets():
    try:
        with open("pet_store.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

# Initialize virtual_pets by loading data from the JSON file
virtual_pets = load_virtual_pets()

# ... (other commands)

# Define the 'buypet' command to buy a pet from the store
@bot.command()
async def buypet(ctx, *, pet_name: str):
    user_id = ctx.author.id
    pet_name = pet_name.lower()

    if user_id not in virtual_pets:
        if pet_name in pet_store:
            virtual_pets[user_id] = {
                "name": pet_name,
                "hunger": 50,
                "happiness": 50
            }
            save_virtual_pets(virtual_pets)  # Save the virtual pets after a purchase
            await ctx.send(embed=discord.Embed(description=f"You've bought a {pet_name.capitalize()}! Use `.petstatus {pet_name}` to check its status.", color=discord.Color.green()))
        else:
            await ctx.send(embed=discord.Embed(description="Invalid pet name. Use `.store` to see available pets.", color=discord.Color.red()))
    else:
        await ctx.send(embed=discord.Embed(description="You already have a virtual pet. Use `.petstatus` to check its status.", color=discord.Color.red()))

# Define the 'store' command to display the pet store
@bot.command()
async def store(ctx):
    embed = create_store_embed()
    await ctx.send(embed=embed)
























keep_alive()

bot.run(os.getenv('TOKEN'))