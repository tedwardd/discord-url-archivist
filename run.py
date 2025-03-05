#!/usr/bin/env python3

import discord
import archiveis
import re

from requests.exceptions import HTTPError

"""
NOTES:
    BASE_URL = https://discord.com/api
"""

API_KEY = '<my_secret_key>'

URL_LIST = [
    "wired.com",
    "spytalk.co",
    "science.org",
    "theatlantic.com",
    "nytimes.com",
    "wsj.com",
    "ajc.com"
]

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('%ping'):
        await message.channel.send('pong')

    for url in URL_LIST:
        if url in message.content:
            target_url = re.search(r"(?P<url>https?://[^\s]+)", message.content)
            if target_url is not None:
                try:
                    archive_url = archiveis.capture(target_url.group("url"), user_agent = user_agent)
                except HTTPError as e:
                    archive_url = f"archive.is returned {e.response.status_code}: {e.response.reason}"

                await message.channel.send(archive_url)

def main():
    client.run(API_KEY)

if __name__ == "__main__":
    main()
