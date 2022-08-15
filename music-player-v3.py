import random
import pygame as pg

from tkinter import *
import tkinter.font as font
import os


class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        # draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))


#creating the root window
pg.mixer.pre_init(44100, -16, 2, 2048)
pg.init()
screen = pg.display.set_mode((160, 160))
pg.display.set_caption('MP3 Player Premiere')

# Load button images
start_img = pg.image.load(r'C:\Users\Huawei\PycharmProjects\Customized_Music_Player\play_button.png').convert_alpha()
start_button = Button(28,20, start_img, 0.8)

# A list of the music file paths.
# SONGS = ['file1.ogg', 'file2.ogg', 'file3.ogg']
# Changing Directory for fetching Songs
os.chdir("D:/melody/")
# Fetching Songs
SONGS = os.listdir()

# Here we create a custom event type (it's just an int).
SONG_FINISHED = pg.USEREVENT + 1
# When a song is finished, pygame will add the
# SONG_FINISHED event to the event queue.
pg.mixer.music.set_endevent(SONG_FINISHED)
# Load and play the first song.
pg.mixer.music.load(random.choice(SONGS))
pg.mixer.music.play(0)

def pause():
    pg.mixer.music.pause()

def resume():
    pg.mixer.music.unpause()

def main():
    clock = pg.time.Clock()
    song_idx = 0  # The index of the current song.
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                # Press right arrow key to increment the
                # song index. Modulo is needed to keep
                # the index in the correct range.
                if event.key == pg.K_RIGHT:
                    print('Next song.')
                    song_idx += 1
                    song_idx %= len(SONGS)
                    pg.mixer.music.load(SONGS[song_idx])
                    pg.mixer.music.play(0)
            # When a song ends the SONG_FINISHED event is emitted.
            # Then just pick a random song and play it.
            elif event.type == SONG_FINISHED:
                print('Song finished. Playing random song.')
                print('buffering...')
                pg.time.wait(10000)
                pg.mixer.music.load(random.choice(SONGS))
                pg.mixer.music.play(0)

        screen.fill((202, 248, 221))
        start_button.draw()

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()