#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time
import telebot

import urllib3
urllib3.disable_warnings()

from carontepass.settings_local import TOKEN_BOT, ID_GROUP_RECEIVER, ID_GROUP_LOG_RECEIVER


tb = telebot.TeleBot(TOKEN_BOT)


#Telegram message to users
def send_simple_msg(chatid, message):
    try:
        tb.send_message(chatid, message)
    except:
        pass

#Message to telegram group when entering the first or the last to leave out  
def send_group_msg(SiteOpen, user_name):
  
    if SiteOpen == True:
        try:
            tb.send_message(ID_GROUP_RECEIVER, "Site Open ("+user_name+")" )
        except:
            pass
    else:
        try:
            tb.send_message(ID_GROUP_RECEIVER, "Site Closed ("+user_name+")")
        except:
            pass

#Message to telegram group only with entry and exit logs      
def send_log_msg(User_In, user_name):

    if User_In == True:
        try:
            tb.send_message(ID_GROUP_LOG_RECEIVER, user_name+" has entered the building." )
        except:
            pass
    else:
        try:
            tb.send_message(ID_GROUP_LOG_RECEIVER, user_name+" has left the building." )
        except:
            pass