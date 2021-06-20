# -*- coding: utf-8 -*-
from __future__ import print_function
from dics import tw_url_dic, tw_id_dic
from os.path import join, dirname
from dotenv import load_dotenv
from tools import twitter_api
import os
import time
import requests
import json
import tweepy

api = twitter_api()
sl_time = 3
no_icon = 'white_icon.png'
no_header = 'white_header.png'


# Twitterプロフィールの内容を返す。
# tw_icon、tw_bannerは画像のURLが入っている。
def get_twitter_profile(name):
    time.sleep(sl_time)
    h = 0

    id = tw_id_dic[name]
    tw_user = api.get_user(id)
    tw_name = tw_user.name
    tw_desc = tw_user.description.replace('\n', ' ')
    tw_place = tw_user.location
    tw_url = tw_user.url
    try:
        tw_icon = tw_user.profile_image_url.replace('normal', '400x400')
    except AttributeError:
        h = 1

    try:
        tw_banner = tw_user.profile_banner_url
    except AttributeError:
        if h == 0:
            h = 2
        elif h == 1:
            h = 3

    if h == 0:
        contents = {
            '名前': tw_name,
            'bio': tw_desc,
            '場所': tw_place,
            'URL': tw_url,
            'アイコン': tw_icon,
            'ヘッダー': tw_banner
        }
    elif h == 1:
        contents = {
            '名前': tw_name,
            'bio': tw_desc,
            '場所': tw_place,
            'URL': tw_url,
            'アイコン': no_icon,
            'ヘッダー': tw_banner
        }
    elif h == 2:
        contents = {
            '名前': tw_name,
            'bio': tw_desc,
            '場所': tw_place,
            'URL': tw_url,
            'アイコン': tw_icon,
            'ヘッダー': no_header
        }
    elif h == 3:
        contents = {
            '名前': tw_name,
            'bio': tw_desc,
            '場所': tw_place,
            'URL': tw_url,
            'アイコン': no_icon,
            'ヘッダー': no_header
        }

    return contents
