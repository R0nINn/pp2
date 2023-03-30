import pygame
import sys
import random

currently_playing = None

def play_a_dif_song ():
    global currently_playing , _songs 
    next_song = random.choice(_songs)
    while next_song == currently_playing:
        next_song = random.choice(_songs)
        currently_playing = next_song
        pygame.mixer.music.load(next_song)
        pygame.mixer.music.play()

pygame.init()


_songs = ['songs/1.mp3','songs/2.mp3','songs/3.mp3']

n = len(_songs)-1
cnt = 0
pygame.mixer.music.load(_songs[cnt])
pygame.mixer.music.play()

w,h = 800,600

surface = pygame.display.set_mode((w,h))
pygame.display.set_caption('Типо Spotify')
pygame.display.set_icon(pygame.image.load('spotify_icon.bmp'))

fps = pygame.time.Clock()

done = False
Flag_pause = False
Flag_next = False
Flag_prev = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                Flag_pause = not Flag_pause
                if Flag_pause:
                    pygame.mixer.music.pause()
                else :
                    pygame.mixer.music.unpause()
                    
            if event.key == pygame.K_RIGHT :
                Flag_next = not Flag_next                   
                if Flag_next:
                    if cnt < n:
                        pygame.mixer.music.load(_songs[cnt+1])
                        pygame.mixer.music.play()
                        cnt+=1
                    else :
                        pygame.mixer.music.load(_songs[cnt])
                        pygame.mixer.music.play()
                        cnt = 0
            elif event.key == pygame.K_LEFT :
                Flag_prev = not Flag_prev                   
                if Flag_prev:
                    if cnt == 0:
                        pygame.mixer.music.load(_songs[n])
                        pygame.mixer.music.play()
                        cnt = n
                    if cnt <= n and cnt > 0 :
                        pygame.mixer.music.load(_songs[cnt-1])
                        pygame.mixer.music.play()
                        cnt -=1
                    
                    
    fps.tick(60)
    pygame.display.flip()
    