#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Car, CarType, User
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
app = Flask(__name__)


# this for handling search page in new page and  I added search
#alghrothem to showCars() without new page
@app.route('/search/', methods=['GET', 'POST'])
def makeSearch():
    top_songs = ["top songs", "popular songs",
                 "popular songs on the radio","i'm good songs",
                 "top songs of all time", "top songs billboard",
                 "i top songs", "high views",
                 "top watched songs on youtube",
                 "top 10 watched songs on youtube",
                 "top 10 most watched songs on youtube",
                 "top most watched songs on youtube",
                 "top most watched songs on youtube",
                 "top 10 watched songs",
                 "top watched songs", "top 10 songs",
                 "this site top songs", "your top songs",
                 "most popular songs", "most watched songs",
                 "top 10 most watched songs", "trending google"
                 "trending youtube", "trending i phone"
                 "trending on netflix", "trending songs",
                 "trending lyrics", "trending videos",
                 "top trending", "trend", "trend google",
                 "most listened songs", "most listened to song ever",
                 "most listened to artist on spotify",
                 "top music", "top music videos",
                 "good music", "most viewed", "songs popular",
                 "songs top", "many views songs",
                 "highr views songs", "top lyrics",
                 "top lyrics songs", "i got top lyrics",
                 "t top lyrics", "top 10 lyrics", "most lyrics watched",
                 "top views songs", "top viewed songs",
                 "song with high views", "best songs", "best lyrics",
                 "top 10", "top songs forever", "give me top songs",
                 "i need top songs", "i need top lyrics",
                 "give me songs viewed alot",
                 "i need top watched songs on youtube",
                 "give me top songs on youtube",
                 ]
    
    if request.method == 'POST':                           
        user_search = request.form['search']
        result = session.query(Songs).filter_by(name = user_search).first()
        if result == None:
            result = session.query(Songs).filter_by(actor = user_search).first()
        elif result == None and len(str(user_search)) == 4:
            result = session.query(Songs).filter_by(year = user_search).first()
        #if user searched for the top watched songs use top_songs list     
        elif result == None and user_search in top_songs:
            result = session.query(Songs).order_by(desc(Songs.views)).limit(10).all()
        return render_template('search.html', result = result, searched_for = user_search)       
    else:        
        return render_template('index.html')
