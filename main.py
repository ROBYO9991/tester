# M1





import logging
import nextcord
import asyncio
from nextcord import Interaction, SlashOption 
from nextcord.ext import commands



command_prefix = "+"

intents = nextcord.Intents.default()
intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix=command_prefix , intents=intents)

@bot.event
async def on_ready():
  print(f"{bot.user.name} is ready!")
  while True:
    await bot.change_presence(activity=nextcord.Game(name=f"Prefix = {command_prefix}"))
    await asyncio.sleep(1)
    await bot.change_presence(activity=nextcord.Game(name=f"{command_prefix}CMD"))

logging = True
logschannel = 1235611924746731562



# kick

@bot.command()
async def kick(ctx, user: nextcord.Member, *, reason: str):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You don't have permission to use this command.")
        return

    await ctx.send(f"Kicked {user.mention}")

    if logging is True:
        log_channel = ctx.guild.get_channel(logschannel)
        await log_channel.send(f"{user.mention} has been kicked by {ctx.author.mention} for {reason}")
        await user.kick(reason=reason)






# unban

@bot.command()
async def unban(ctx, user: nextcord.Member, * str):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You don't have permission to use this command.")
        return

    await ctx.send(f"Unbanned {user.mention}")
    if logging is True:
        log_channel = ctx.guild.get_channel(logschannel)
        await log_channel.send(f"{user.mention} has been Unbanned by {ctx.author.mention}")
        await user.unban()



# clear


@bot.command(aliases=["Ms7", "MS7" , "ms7"])
async def clear(ctx: nextcord.Interaction, amount: int):
  if not ctx.author.guild_permissions.administrator:
    await interaction.response.send_message("ma3ndkx perm bax tdir had cmd, you dont have permetion to use this command.", ephemeral=True)
    return
  await ctx.channel.purge(limit=amount)
  await ctx.response.send_message("Cleared!")







  # ban

@bot.command()
async def ban(ctx, user: nextcord.Member, *, reason: str):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("err")
        return

    ban_list = await ctx.guild.bans()
    for ban_entry in ban_list:
        if ban_entry.user.id == user.id:
            await ctx.guild.unban(ban_entry.user, reason=reason)
            await ctx.send(f"{user.name} has been unbanned.")
            return
    await ctx.send(f"{user.name} ma mbanich,dont banned.")



# warn

@bot.command()
async def warn(ctx, user: nextcord.Member, *, reason: str):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You don't have permission to use this command.")
        return

    await ctx.send(f"{user.mention} got Warnd!")

    if logging is True:
        log_channel = ctx.guild.get_channel(logschannel)
        await log_channel.send(f"{user.mention} has been warned by {ctx.author.mention} for `{reason}`")
        await user.warn(reason=reason)




    # add_role

@bot.command()
async def add(ctx, user: nextcord.Member, role: nextcord.Role):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use this command.")
        return

    await user.add_roles(role)
    await ctx.send(f"Role {role.name} has been given to {user.mention}")

    log_channel_id = 1235611924746731562
    log_channel = bot.get_channel(log_channel_id)
    await log_channel.send(f"{user.mention} has been given {role.mention} by {ctx.author.mention}")


  # help 


@bot.command(aliases=["c", "cmd", "commands", "Help"])
async def cmds(ctx):
  embed = nextcord.Embed(title="<a:nitro:1228011670362783816>〡CMD",
    description=f"ㅤ\n**--- Commands ---**\n\n **<a:verify:1226522601573322802>`kick`\n<a:verify:1226522601573322802>`ban `\n<a:verify:1226522601573322802>`mute`\n<a:verify:1226522601573322802>`unmute`\n<a:verify:1226522601573322802>`warn`\n<a:verify:1226522601573322802>`warn_remove`\n<a:verify:1226522601573322802>`clear`\n<a:verify:1226522601573322802>`lock`\n<a:verify:1226522601573322802>`unlock`\n<a:verify:1226522601573322802>`unban`\n<a:verify:1226522601573322802>`add `\n<a:verify:1226522601573322802>`cmd_use `\n<a:verify:1226522601573322802>`jail`\n<a:verify:1226522601573322802>`unjail`\n<a:verify:1226522601573322802>`vb`\n<a:verify:1226522601573322802>`vg` \n\n\n ```BY ROBYO```**",
    colour=0x6bff89)


  embed.set_image(url='https://media.discordapp.net/attachments/1234278697280868353/1234952547848949760/Design_sans_titre.gif?ex=663494ef&is=6633436f&hm=ea52ab07c17bbd46c066ce6f0efe788ec1c6c859f714fee3c4dd4015bff41908&=&width=960&height=12 ')
  await ctx.send(embed=embed)




# cmd_use


@bot.command(aliases=["c_use","c_u"])
async def cmd_use(ctx):
  embed = nextcord.Embed(title="use the commands",
                        description="**Moderation_Commands**\n\n`kick <id,Mention> <reason>`\n`ban <id,Mention> <reason>`\n`mute  <id,Mention> <reason>`\n`unmute <id,Mention>`\n`warn <id,Mention> <reason>`\n`warn_remove <id,Mention> `\n`clear <amount>`\n`lock`\n`unlock`\n`unban <id,user>`\n`add <id,Mention> <Role> `\n\n **More commands Comming soon!** <a:verify:1226522601573322802> ",
                        colour=0x00f556)

  await ctx.send(embed=embed)
                 
              
                 



@bot.command()
async def remove_role(ctx, user: nextcord.Member, role: nextcord.Role):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use this command.")
        return

    if role in user.roles:
        await user.remove_roles(role)
        await ctx.send(f"Role {role.name} has been removed from {user.mention}")
    else:
        await ctx.send(f"{user.mention} does not have the role {role.name}")

    log_channel_id = 1235611924746731562
    log_channel = bot.get_channel(log_channel_id)
    await log_channel.send(f"{role.name} has been removed from {user.mention} by {ctx.author.mention}")



















@bot.command()
async def jail(ctx, user: nextcord.Member, *, reason: str):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use this command.")
        return

    role_id = 1226506083321909248
    role = ctx.guild.get_role(role_id)

    if role is None:
        await ctx.send("Role not found.")
        return

    # Remove current roles
    for user_role in user.roles:
        if user_role != ctx.guild.default_role:
            await user.remove_roles(user_role)

    # Assign the specified role
    await user.add_roles(role)

    await ctx.send(f"{user.mention} has been assigned the role {role.name} automatically.")

    log_channel_id = 1235654517849067562
    log_channel = bot.get_channel(log_channel_id)
    await log_channel.send(f"{user.mention} has been assigned the role {role.name} automatically by {ctx.author.mention} for `{reason}`")









# Update the jail command to remove the jail role and add the verified role
@bot.command()
async def unjail(ctx, user: nextcord.Member):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use this command.")
        return

    jail_role_id = 1226506083321909248
    verified_role_id = 1226307733867724893

    jail_role = ctx.guild.get_role(jail_role_id)
    verified_role = ctx.guild.get_role(verified_role_id)

    if jail_role is None or verified_role is None:
        await ctx.send("Role not found.")
        return

    if jail_role in user.roles:
        await user.remove_roles(jail_role)
        await user.add_roles(verified_role)
        await ctx.send(f"Role {jail_role.name} has been removed and role {verified_role.name} has been added to {user.mention}")
    else:
        await ctx.send(f"{user.mention} does not have the role {jail_role.name}")

    log_channel_id = 1235654517849067562
    log_channel = bot.get_channel(log_channel_id)
    await log_channel.send(f"{user.mention} unjailed by {ctx.author.mention}.")








@bot.command(aliases=["vb"])
async def verify_and_send_dm(ctx, user: nextcord.Member):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use this command.")
        return

    unverified_role_id = 1226497828931502120
    verified_role_id = 1226307733867724893

    unverified_role = ctx.guild.get_role(unverified_role_id)
    verified_role = ctx.guild.get_role(verified_role_id)

    if unverified_role is None or verified_role is None:
        await ctx.send("Role not found.")
        return

    if unverified_role in user.roles:
        await user.remove_roles(unverified_role)
        await user.add_roles(verified_role)
        await ctx.send(f"Role {unverified_role.name} has been removed and role {verified_role.name} has been added to {user.mention}")
    else:
        await ctx.send(f"{user.mention} does not have the role {unverified_role.name}")

    log_channel_id = 1235891313870901328
    log_channel = bot.get_channel(log_channel_id)
    await log_channel.send(f"{user.mention} verified by {ctx.author.mention}.")

    if verified_role not in user.roles:
        await ctx.send(f"{user.mention} does not have the verified role.")
        return

    embed = nextcord.Embed(
        title="Verification Success",
        description=f"{user.mention}, You are now verified!",
        color=0x6bff89
    )
    embed.set_image(url='https://media.discordapp.net/attachments/1226288069796298793/1237045667642343545/Kings1online-video-cutter.com2-ezgif.com-overlay.gif?ex=663a380e&is=6638e68e&hm=134b1be739d9d6483e73776660a6716e50ffb3c6344e90329872c71f4bd18305&=&width=400&height=400 ')

    channel = await user.create_dm()  # Creating a direct message channel

    try:
        await channel.send(embed=embed)  # Sending the embed message with the GIF
        await ctx.send(f"Sent a DM to {user.mention} with a verification success message.")
    except nextcord.Forbidden:
        await ctx.send(f"Failed to send a DM to {user.mention}. Please make sure the user allows DMs from this server.")









# token


bot.run(token)
