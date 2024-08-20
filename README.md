# DiscordBot

## Description

This Discord bot tracks and manages "combos" based on user interactions in a Discord server. When different users consecutively post the same text, the bot increments and displays the combo count. If the same user repeats a comment or the text changes, the combo breaks and the bot announces the final combo length.

## Key Features

- **Combo Tracking**: Increments combo counts based on unique user interactions.
- **Discord.py API**: Built using the `discord.py` library.
- **SQLite3 Database**: Manages and stores combo data across servers.
- **Security**: Sensitive data like the Discord token and others, is sanitized.

## Usage

Set up the bot using the provided Python scripts. Ensure that you configure the bot token and other settings in the environment as needed.
