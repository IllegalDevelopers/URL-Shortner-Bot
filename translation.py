from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """Hi there {} 

Send Me A Link or Post And I'll Shorten It For You!

To Learn More About What I Can Do, Just Type /help.

Method: {}
Shortener website: {}
"""

HELP_MESSAGE = """<b>ʜᴇʏ ᴛʜᴇʀᴇ! ᴍʏ ɴᴀᴍᴇ ɪꜱ {firstname} ᴀɴᴅ ɪ'ᴍ ᴀ ʟɪɴᴋ ᴄᴏɴᴠᴇʀᴛᴏʀ ᴀɴᴅ ꜱʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ ʜᴇʀᴇ ᴛᴏ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴡᴏʀᴋ ᴇᴀꜱɪᴇʀ ᴀɴᴅ ʜᴇʟᴘ ʏᴏᴜ ᴇᴀʀɴ ᴍᴏʀᴇ 💰.

ɪ ʜᴀᴠᴇ ᴀ ᴛᴏɴ ᴏꜰ ʜᴀɴᴅʏ ꜰᴇᴀᴛᴜʀᴇꜱ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴏᴜᴛ, ꜱᴜᴄʜ ᴀꜱ:

- [ʜʏᴘᴇʀʟɪɴᴋ](https://t.me/{username}) ꜱᴜᴘᴘᴏʀᴛ 🔗
- ʙᴜᴛᴛᴏɴ ᴄᴏɴᴠᴇʀꜱɪᴏɴ ꜱᴜᴘᴘᴏʀᴛ 🔘
- ᴅᴏᴍᴀɪɴ ɪɴᴄʟᴜꜱɪᴏɴ ᴀɴᴅ ᴇxᴄʟᴜꜱɪᴏɴ ᴏᴘᴛɪᴏɴꜱ 🌐
- ʜᴇᴀᴅᴇʀ ᴀɴᴅ ꜰᴏᴏᴛᴇʀ ᴛᴇxᴛ ꜱᴜᴘᴘᴏʀᴛ 📝
- ʀᴇᴘʟᴀᴄᴇ ᴜꜱᴇʀɴᴀᴍᴇ ꜰᴜɴᴄᴛɪᴏɴ 📎
- ʙᴀɴɴᴇʀ ɪᴍᴀɢᴇ ꜱᴜᴘᴘᴏʀᴛ 🖼️
- ʙᴀᴛᴄʜ ᴄᴏɴᴠᴇʀꜱɪᴏɴ ꜰᴏʀ ᴄʜᴀɴɴᴇʟ ᴀᴅᴍɪɴꜱ ᴏɴʟʏ 📊
- ᴄʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ ꜰᴏʀ ᴀᴅᴍɪɴꜱ ᴏɴʟʏ 📢

ᴜꜱᴇꜰᴜʟ ᴄᴏᴍᴍᴀɴᴅꜱ:

- /start: ꜱᴛᴀʀᴛ ᴍᴇ ᴜᴘ! ʏᴏᴜ ᴘʀᴏʙᴀʙʟʏ ᴀʟʀᴇᴀᴅʏ ᴜꜱᴇᴅ ᴛʜɪꜱ.
- /help: ꜱᴇɴᴅ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ; ɪ'ʟʟ ᴛᴇʟʟ ʏᴏᴜ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍʏꜱᴇʟꜰ!
- /batch -100xxx: ᴛᴏ ꜱʜᴏʀᴛᴇɴ ᴏʀ ᴄᴏɴᴠᴇʀᴛ ᴀʟʟ ᴘᴏꜱᴛꜱ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ</b>"""

ABOUT_TEXT = """
**My Details:**

`🤖 Name:` ** {} **
    
`📝 𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎:` [𝙿𝚊𝚢𝚝𝚑𝚘𝚗 𝟹](https://www.python.org/)
`👨‍💻 Developer:` [𝙳𝚎𝚟](t.me/IllegalDeveloperBot)
`📢 Support:` [𝚃𝚊𝚕𝚔 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛](t.me/IllegalDeveloperBot)
`🌐 Source Code:` [𝙶𝚒𝚝𝙷𝚞𝚋](t.me/IllegalDeveloperBot)
"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

> `mdlink` - Change all the links of the post to your MDisk account first and then short to {shortener} link.

> `shortener` - Short all the links of the post to {shortener} link directly.

> `mdisk` - Save all the links of the post to your Mdisk account.
    
To change method, choose it from the following options:
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Batch Mode", callback_data="cbatch_command"),
            InlineKeyboardButton("Shortner Mode", callback_data="cshortner_command"),
        ],
        [
            InlineKeyboardButton("Custom Alias", callback_data="alias_conf"),
        ],
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [InlineKeyboardButton("Close", callback_data="delete")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Help", callback_data="help_command"),
            InlineKeyboardButton("About", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("Update", url="https://t.me/Illegal_Developer"),
            InlineKeyboardButton("Support", url="https://t.me/Illegal_Supports"),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "MDLINK", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "Shortener", callback_data="change_method#shortener"
            ),
            InlineKeyboardButton("Mdisk", callback_data="change_method#mdisk"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="help_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Back", callback_data="help_command")]]
)

USER_ABOUT_MESSAGE = """
🔧 Here are the current settings for this bot:

- 🌐 Shortener website: {base_site}

- 🧰 Method: {method}

- 🔌 {base_site} API: {shortener_api}

- 💾 Mdisk API: {mdisk_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}
"""


MDISK_API_MESSAGE = """To add or update your Mdisk API, \n`/mdisk_api mdisk_api`
            
Ex: `/mdisk_api 6LZq851sXoPHugiKQq`
            
Others Mdisk Links will be automatically changed to the API of this Mdisk account

Get your Mdisk API from @VideoToolMoneyTreebot

Current Mdisk API: `{}`"""

SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

To change your Shortener Website: /base_site

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """📝 To set the header text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the header text, use the following command:

`/header remove`

This is a helpful way to add a consistent header to all of your messages. Enjoy! 🎉"""

FOOTER_MESSAGE = """📝 To set the footer text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the footer text, use the following command:

`/footer remove`

This is a helpful way to add a consistent footer to all of your messages. Enjoy! 🎉"""

USERNAME_TEXT = """Current username: {username}

To set the username that will be automatically replaced with other usernames in the post, use the following command:

`/username your_username`

__(Note: Do not include the @ symbol in your username.)__

To remove the current username, use the following command:

`/username remove`

This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
