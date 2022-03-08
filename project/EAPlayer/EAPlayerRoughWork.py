#https://towardsdatascience.com/how-to-build-an-mp3-music-player-with-python-619e0c0dcee2 
#https://www.youtube.com/watch?v=88IJCBKlAPA 
#Pip install virtualenv: To create a virtual envrioment to work
#pip instal pygame
"""
from tkinter.constants import SINGLE
import pygame #Used for developing games
import tkinter #Used to develope GUI buttons
from tkinter.filedialog import askdirectory #Allows for selection of directory
import os #Directory navigation

music_player = tkinter.Tk()
music_player.title("Love music")
music_player.geometry("450x350")

directory = askdirectory() # Get the path of the directory of the music
os.chdir(directory) #change the path to the the music directory
song_list = os.listdir()
print(os.listdir()) #List all the song in the list.

play_list = tkinter.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=SINGLE) # Setting our playlist to work

for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos +=1

pygame.init()
pygame.mixer.init()


#Declaring the play function
def play():
    pygame.mixer.music.load(play_list.get(tkinter.ACTIVE))
    var.set()
"""

from tkinter import *
import pygame

EAPlayer = Tk()
EAPlayer.title("EAPlayer")
EAPlayer.geometry("500x300")

#initializing the pygame
pygame.mixer.init()

#Create a playlist
playlist = Listbox(EAPlayer, bg="black", fg="green", width=60)
playlist.pack(pady=20)

#Define button images player buttons
play_btn_img = PhotoImage(file='C:/Users/DeptAdmin/Documents/codeEnv/pythonProject/project/EAPlayer/img/playicon.png')
#pause_bth_img = PhotoImage(file='C:/Users/DeptAdmin/Documents/codeEnv/pythonProject/project/EAPlayer/img/pauseicon.png')
forward_bth_img =PhotoImage(file="C:/Users/DeptAdmin/Documents/codeEnv/pythonProject/project/EAPlayer/img/forward.png") 
backward_bth_img = PhotoImage(file="C:/Users/DeptAdmin/Documents/codeEnv/pythonProject/project/EAPlayer/img/forward.png")
stop_btn_img = PhotoImage(file="C:/Users/DeptAdmin/Documents/codeEnv/pythonProject/project/EAPlayer/img/stop.png")

#Create player frame
control_frame =Frame(EAPlayer)
control_frame.pack()

#creating player control buttons
play_btn = Button(control_frame, image=play_btn_img, border=0)
#pause_btn = Button(control_frame, image=pause_bth_img, border=0)
forward_btn = Button(control_frame, image=forward_bth_img, border=0)
backward_btn = Button(control_frame, image=backward_bth_img, border=0)
stop_btn = Button(control_frame, image=stop_btn_img, border=0)

play_btn.grid(row=0, column=0)
#pause_btn.grid(row=0, column=1)
forward_btn.grid(row=0, column=1)
backward_btn.grid(row=0, column=2)
stop_btn.grid(row=0, column=3)


EAPlayer.mainloop()