import os
from pygame import mixer
import pygame

#Create Playlist
def playlist():
    songs = []
    mixer.init()
    pygame.init()
    set_path = r'C:\Users\DeptAdmin\Music\EAPlayer' #Set music path
    os.chdir(set_path) #Change dir to music path
    musics = os.listdir()
    #Getting music paths
    for music in musics:
        music_path = os.path.abspath(music)
        music_path.replace("\\","\'\\'\'")
        songs.append(music_path) #this contains the music absolute path in windows directory path format
    return songs

def playsong(songlist): #song list should be a list
    #load the first song in the list
    total_song = len(songlist)
    for song in songlist:
        #Get the index of the songs
        index_val = songlist.index(song)
        #load the index value to mixer.load()
        mixer.music.load(song)
        mixer.music.play()
        while pygame.mixer.music.get_busy():
            print(song, "Playing...", end='\r')
            pygame.time.Clock().tick()
        
playsong(playlist())
