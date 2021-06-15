import discord #Import if not installed Discord.py
import os #Importing Discord again

client = discord.Client() #Logging in with Token Data

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #Tells a message!

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Info'):
        await message.channel.send('Shaggy bot is a bot made by ShainDev ') #Data for senting a message to discord with a Command

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Shaggy'):
        await message.channel.send('Hey guys my names Scoob (This is in devlopment)')

@client.event

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Help'): 
     embed = discord.Embed(title="Shaggy Help", description="You need some help with the bot",colour=0x00ff02) #,color=Hex code
    embed.add_field(text="$Info", value="This Will show some info about the bot")
    embed.add_field(text="$Shaggy", value="This WILL tell you about Shaggy")
    embed.add_field(text="$Sg", value="It is a Guessing game!")
    embed.set_footer(text="©️ShainDev", icon_url="https://i1.sndcdn.com/avatars-000690165539-hns2em-t500x500.jpg") 
    await message.channel.send(embed=embed)
    #Shows Data for the Embed to sent when a Command

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg start'):
        await message.channel.send('S____y Guesss the word? You have 3 hints')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg Hint1 '):
        await message.channel.send('S__o_y Guesss the word? You have 2 hints')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg hint2'):
        await message.channel.send('S__oby Guesss the word? You have 1 hint')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg hint3'):
        await message.channel.send('Sorry the word is to easy :pensive: ')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg A'):
        await message.channel.send('Incorrect! Try again')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg D'):
        await message.channel.send('Incorrect! Try again')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg E'):
        await message.channel.send('Incorrect! Try again')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg F'):
        await message.channel.send('Incorrect! Try again')  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg G'):
        await message.channel.send('Incorrect! Try again') 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg H'):
        await message.channel.send('Incorrect! Try again')    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg I'):
        await message.channel.send('Incorrect! Try again')   

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg J'):
        await message.channel.send('Incorrect! Try again')     


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg K'):
        await message.channel.send('Incorrect! Try again')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg L'):
        await message.channel.send('Incorrect! Try again')      

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg M'):
        await message.channel.send('Incorrect! Try again')      

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg N'):
        await message.channel.send('Incorrect! Try again')    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg O'):
        await message.channel.send('Incorrect! Try again')    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg P'):
        await message.channel.send('Incorrect! Try again')       

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg Q'):
        await message.channel.send('Incorrect! Try again') 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg R'):
        await message.channel.send('Incorrect! Try again')  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg V'):
        await message.channel.send('Incorrect! Try again') 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg X'):
        await message.channel.send('Incorrect! Try again')    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg Z'):
        await message.channel.send('Incorrect! Try again')   

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg R'):
        await message.channel.send('Incorrect! Try again')                                                  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg T'):
        await message.channel.send('Incorrect! Try again')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg U'):
        await message.channel.send('Incorrect! Try again')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg '):
        await message.channel.send('Sorry Unknown Command try $Sg htp? ')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg C'):
        await message.channel.send(' Correct! Sc___y')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg Y'):
        await message.channel.send('Incorrect! Try again')       

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg O'):
        await message.channel.send(' Correct! Scoo_y')    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg B'):
        await message.channel.send(' Correct! Scooby.')            
        

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Sg htp'): 
     embed = discord.Embed(title="How to play!", description="You need to learn the basics!",colour=0x00ff02)  
    embed.add_field(text="Step One", value="Type in ($Sg Start) and will say do you know how to play and say ($sg yes)")
    embed.add_field(text="Step 2", value="It should say S____y and you have to guess, if you need help say hint1 to 3 ")
    embed.add_field(text="Step 3", value="they you go and youre ready to Play! ")
    embed.set_footer(text="©️ShainDev", icon_url="https://i1.sndcdn.com/avatars-000690165539-hns2em-t500x500.jpg")
    await message.channel.send(embed=embed)       

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ '):
        await message.channel.send('Sorry Unknown Command try $Help? ')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Rules'):
        await message.channel.send('Dont Spam or do anything that is against the discord TOS')        














client.run(os.getenv('TOKEN')) #where the Token is!

 
        