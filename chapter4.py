import pygame

import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

#MENGENALI PYGAME
pygame.init()

#MENGINISIALISASI MIXER 
pygame.mixer.init()

#MENGATUR LAYARNYA (UKURAN JUGA)
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("GAME SEDERHANA")

#MEMASUKKAN GAMBARNYA UHUYY
image = pygame.image.load('gambar1.jpg')

#MUUUSIKK
sound = pygame.mixer.Sound('result.wav')

#PLAY MUSIKNYAAA
sound.play()


#VARIABEL BENG INI
x=0
# Loop utama permainan dengan animasi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#NA PERBAIKI POSISINYA
    x += 5
    if x > 800:
        x = 0

#KASI MASUK GAMBAR DI POSISI BARU 
    screen.fill((0, 0, 0))   
    screen.blit(image, (x, 100))

#NA PERBARUI TAMPILANNYA
    pygame.display.flip()

#KALO SELESAIMI DITUTUPKI
pygame.quit()


#--------------------------------------------#


#BIKIN JENDELA TKINTER
root = tk.Tk()
root.title("PLAY MUSIX")

#FUNGSI UNTUK MEMUTAR MUSIK
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

#TOMBOL PLAYNYA INI
play_button = tk.Button(root, text="MULAY", command=play_music)
play_button.pack()

#KASI JALAN ANU NYA
root.mainloop()