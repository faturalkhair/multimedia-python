from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Memuat file video
video = VideoFileClip('videoPendek.mp4')

# Menyimpan file video
video.write_videofile('hasilVideo.mp4')


#Memotong durasi video mejadi 10 detik pertama
short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('hasilPotonganVideoMenjadi10Detik.mp4')

#menggabungkan 2 video menjadi 1
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('menggabungVideo.mp4')


#membalikkan video/reverse dari belakang ke depan
reversed_video = short_video.fx(vfx.time_mirror)  
# Membalikkan video
reversed_video.write_videofile('hasilReverseVideo.mp4')


#mempercepat kecepatan video menjadi 2x
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('hasil_Mempercepat2x.mp4')




#-----------------------------------------------------------------------#

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Multimedia")

# Menjalankan loop acara Tkinter



# Memuat gambar menggunakan Pillow
image = Image.open('gambar1.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

root.mainloop()