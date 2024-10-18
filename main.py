import tp_image_oo as oo

image = oo.MyImage()
image.load("data/ski.jpg")
image.get_chanel(2)
# image.transpose()
image.crop(100,200,300,400)
print(image.lum())
image.auto_lum_contrast()
image.reduce(2)
image.save("data/out.jpg")
image.show()