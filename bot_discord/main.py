import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Desenvolvido por pprisma"))

    print(f'Tamo on paizao {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!say'):
        content = message.content[len('!say '):]

        if content.strip() == "":
            await message.channel.send("Você não disse nada após o comando!")
        else:
            embed = discord.Embed(
                title="📢 Anuncio oficial",
                description=content,
                color=discord.Color.orange()
            )

            if client.user.avatar:
                embed.set_footer(text="Assad's Store", icon_url=client.user.avatar.url)
            else:
                embed.set_footer(text="Assad's Store")

            embed.timestamp = message.created_at

            await message.channel.send(embed=embed)

client.run('SEU TOKEN AQUI')