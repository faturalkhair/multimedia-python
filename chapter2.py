from PIL import Image
from PIL import ImageFilter

# Memuat gambar
image = Image.open('gambar1.jpg')
# Menyimpan gambar
image.save('hasil_save.jpg')


# Crop gambar
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('hasil_crop.jpg')

# Resize gambar
resized_image = cropped_image.resize ((100,100))
resized_image.save('hasil_resize.jpg')

# Filter 
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('hasil_filter.jpg')
 