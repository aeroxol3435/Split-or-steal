import discord
from discord.ext import commands

TOKEN = "MTQ5ODkwNTUzMjA1NTE2MzAxMA.GH0lDx.1hDPHoKnMDisov0rY7E3ZBCwG1oRNkDgRFiCc0"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Slash command: /ping
@bot.tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    latency = round(bot.latency * 1000)
    await interaction.followup.send(f"🏓 Pong! {latency}ms")

# Slash command: /hello
@bot.tree.command(name="hello", description="Say hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    await interaction.followup.send(f"👋 Hello, {interaction.user.mention}!")

# Button test
class TestView(discord.ui.View):
    @discord.ui.button(label="Click me", style=discord.ButtonStyle.green)
    async def button_click(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.response.is_done():
            await interaction.response.defer(ephemeral=True)

        await interaction.followup.send("✅ Button works!", ephemeral=True)

@bot.tree.command(name="button", description="Test button interaction")
async def button(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Press the button 👇",
        view=TestView(),
        ephemeral=True
    )

# Ready event
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
