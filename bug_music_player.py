# importing libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import random
from mutagen.mp3 import MP3


# add many songs to the playlist
def addsongs():
    # a list of songs is returned
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song",
                                            filetypes=(("mp3 Files", "*.mp3"),))
    # loop through everyitem in the list
    for s in temp_song:
        s = s.replace("D:/melody/", "")
        songs_list.insert(END, s)


def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])


def Play():
    song = songs_list.get(ACTIVE)
    song = f'D:/melody/{song}'
    mixer.music.load(song)
    mixer.music.play()


# to pause the song
def Pause():
    mixer.music.pause()


# to stop the  song
def Stop():
    # when VarInt value == 0, the successive function call
    # from Shuffle() will be null.
    root.setvar(name="int",value=0)
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)


# to resume the song
def Resume():
    mixer.music.unpause()


# Function to navigate from the current song
def Previous():
    # to get the selected song index
    previous_one = songs_list.curselection()
    # to get the previous song index
    previous_one = previous_one[0] - 1
    # to get the previous song
    temp2 = songs_list.get(previous_one)
    temp2 = f'D:/melody/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate new song
    songs_list.activate(previous_one)
    # set the next song
    songs_list.selection_set(previous_one)


def Next():
    # to get the selected song index
    next_one = songs_list.curselection()
    # to get the next song index
    next_one = next_one[0] + 1
    # to get the next song
    temp = songs_list.get(next_one)
    temp = f'D:/melody/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate newsong
    songs_list.activate(next_one)
    # set the next song
    songs_list.selection_set(next_one)


# ingenious recursive function
'''
def change(a=0):
    color_label.config(bg = "blue" if a & 1 else "purple")
    color_label.after(400,change, a ^ 1 )
'''


# a milestone of selective repetitive function :)
def Shuffle(counter=0):
    sync = root.getvar(name="int")
    if counter and counter == sync:
        root.setvar(name="int",value=sync+1)
        song = songs_list.get(random.randint(0, songs_list.size() - 1))
        song = f'D:/melody/{song}'
        mixer.music.load(song)
        mixer.music.play()
        audio = MP3(song)
        print(audio.info.length)
        delay = 10  # seconds
        root.after((int(audio.info.length) + delay) * 1000, Shuffle,counter+1)
        print("int variable is ",root.getvar(name="int"))
    elif counter == 0:
        root.setvar(name="int", value=1)
        song = songs_list.get(random.randint(0, songs_list.size() - 1))
        song = f'D:/melody/{song}'
        mixer.music.load(song)
        mixer.music.play()
        audio = MP3(song)
        print(audio.info.length)
        delay = 10  # seconds
        root.after((int(audio.info.length) + delay) * 1000, Shuffle, counter + 1)
        print("first int variable is ", root.getvar(name="int"))



# creating the root window
root = Tk()
root.title('Music player Pro App ')
# initialize mixer
mixer.init()

# create the listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=54,
                     selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

# font is defined which is to be used for the button font
defined_font = font.Font(family='Helvetica')

# play button
play_button = Button(root, text="Play", width=7, command=Play)
play_button['font'] = defined_font
play_button.grid(row=1, column=0)

# pause button
pause_button = Button(root, text="Pause", width=7, command=Pause)
pause_button['font'] = defined_font
pause_button.grid(row=1, column=1)

# stop button
stop_button = Button(root, text="Stop", width=7, command=Stop)
stop_button['font'] = defined_font
stop_button.grid(row=1, column=2)

# resume button
Resume_button = Button(root, text="Resume", width=7, command=Resume)
Resume_button['font'] = defined_font
Resume_button.grid(row=1, column=3)

# previous button
previous_button = Button(root, text="Prev", width=7, command=Previous)
previous_button['font'] = defined_font
previous_button.grid(row=1, column=4)

# nextbutton
next_button = Button(root, text="Next", width=7, command=Next)
next_button['font'] = defined_font
next_button.grid(row=1, column=5)

# shuffle button
shuffle_button = Button(root, text="Shuffle", width=7, command=Shuffle)
shuffle_button['font'] = defined_font
shuffle_button.grid(row=1, column=6)

# menu
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

# Tkinter variables
intvar = IntVar(root, name="int")
root.setvar(name="int", value=0)
print("value of IntVar() ", root.getvar(name="int"))



mainloop()
