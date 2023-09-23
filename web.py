import streamlit as st

st.set_page_config(page_title="spotify",page_icon="im.png",layout="wide")

import json
from streamlit_lottie import st_lottie

def load_lottiefile(filepath:str):
    with open(filepath,'r') as f:
        return json.load(f)

l=load_lottiefile("m.json")

import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

Client_id="0a6f8deecda04e89b5a5cd8556a80b78"
Client_secret="7dbb11fad22d416c893c5d48cf135085"

client_credentials_manager=SpotifyClientCredentials(client_id=Client_id, client_secret=Client_secret)
sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def cover(song_name,artist_name):

    search_query=f"track:{song_name} artist:{artist_name}"
    r=sp.search(q=search_query,type="track")

    if r and r["tracks"]["items"]:
        track=r["tracks"]["items"][0]
        album_cover= track["album"]["images"][0]["url"]
        print(album_cover)
        return album_cover
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
    

def recommend(song):

    idx=music[music['song']==song].index[0]
    d=sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])
    recommend_music_names=[]
    recommend_music_posters=[]
    for i in d[1:7]:
        artist=music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommend_music_posters.append(cover(music.iloc[i[0]].song,artist))
        recommend_music_names.append(music.iloc[i[0]].song)
    return recommend_music_posters,recommend_music_names

with st.container():
    st.header('Music Recommendation System')
    st.subheader('Listen up your Heart.........')
    st_lottie(
        l,
        speed=1,
        quality="low",
        height=150,
        width=150

    )
    
menu= """

<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(menu,unsafe_allow_html=True)

music=pickle.load(open('df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

song_list=music['song'].values
selected_song=st.selectbox(
    "Type or select a song from the dropdown",song_list

)

if st.button('Show Song Recommendation',):
    recommend_music_posters,recommend_music_names=recommend(selected_song)
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
        st.text(recommend_music_names[0])
        st.image(recommend_music_posters[0])

    with c2:
        st.text(recommend_music_names[1])
        st.image(recommend_music_posters[1])

    with c3:
        st.text(recommend_music_names[2])
        st.image(recommend_music_posters[2])

    with c4:
        st.text(recommend_music_names[3])
        st.image(recommend_music_posters[3])  

    with c5:
        st.text(recommend_music_names[4])
        st.image(recommend_music_posters[4])      




