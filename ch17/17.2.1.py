from PIL import Image

cat_im = Image.open('zophie.png')
print(cat_im.size)

width, height = cat_im.size

print(width, height)
print(cat_im.filename)
print(cat_im.format)
print(cat_im.format_description)

cat_im.save('zophie.jpg')

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')

im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')