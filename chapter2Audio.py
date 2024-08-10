from pydub import AudioSegment

# memuat file audio 
audio = AudioSegment.from_file('premanPensiun.mp3')

# Menyimpan file audio
audio.export('hasil_audio.mp3', format='mp3')

# Potong audio 
clipped_audio = audio[:10000] #untuk 10 detik pertama
clipped_audio.export('hasil_clippedAudio.mp3', format='mp3')

# Menggabug 2file audio
combined_audio = audio + clipped_audio
combined_audio.export('hasil_combinedAudio.mp3', format='mp3')

# Mengonversi file audio ke format lain
audio.export('hasil_format.wav', format='wav')

# Pengaturan volume
louder_audio = audio - 20 # nambah 10dB

