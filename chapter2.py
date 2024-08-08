from PIL import Image

# Memuat gambar
image = Image.open('owi.jpg')

# Menyimpan gambar
image.save('result.jpg')