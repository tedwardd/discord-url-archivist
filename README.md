# Simple Discord Link Archiver

A simple Discord bot that looks for and archives URLs using archive.is

Target environment was for Python 3.11.7 but any variant of 3.11 or newer
should be fine but is untested.

## Setup

* Install dependencies: `pip install -r requirements.txt`
* Provide a Discord API key with permissions to send messages and read message
history

## Known Issues

Recently, archive.is has introduced a captcha on it's `/capture` endpoint. This
results in an unfortunately frequent HTTP 427. I've taken this in to account
and the bot will report it in chat, but I've not yet figured out a way around
the issue. Suggestions welcome.
