import logging

from telegram import Update
from telegram.ext import (
    ContextTypes,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        parse_mode="markdown",
        text="Hi! I am CypherCAT, a super power bot for all Crypto user. Made with love by CypherBOT. I can do a copy trade from influencer/wallet, snipe tokens, buy presales, place limit orders, swap tokens and many more. You can ask me for the current price of any crypto by typing:\n\n"
        "`/p <crypto_symbol>` \n\n"
        "For example, `/p btc` or `/cmc btc` will give you the current price of Bitcoin\n\n"
        "To display the complete list of commands, type `/help`",
    )
    logging.info("Start call")


async def bot_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        parse_mode="markdown",
        disable_web_page_preview=True,
        text="*List of Commands:*\n\n"
        "`/p <crypto_symbol>` - to receive the current price and historical variation from CoinCecko\n"
        "`/c <crypto_symbol>` - to receive the chart in different timeframes of selected crypto\n"
        "`/cmc <crypto_symbol>` - to receive the current price and historical variation from CoinMarketCap\n"
        "`/chart_color` to select chart color theme\n"
        "/cmckey - to reveive info about CoinMarketCap api key usage"
        "/dom - to receive the top 10 most capitalized tokens\n"
        "/gas - to receive real time gas information on ERC\n"
        "/news - to receive CoinTelegraph news\n"
        "/help - to receive this message\n\n"
        "This bot is written with open-source and free code, and you can find it all at "
        "[Website](https://cypherbot.tech)\n\n"
        "`Bot version: 1.0.1`\n",
    )
    logging.info(f"Help call")
