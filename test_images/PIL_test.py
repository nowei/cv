from PIL import Image
im = Image.open('lynnwood.jpg')
size = im.size
pix = im.load()
print(pix[1,1])
for x in range(size[0]):
    for y in range(size[1]):
        c = pix[x,y]
        pix[x,y] = (c[0],c[1],c[2]//2,255)
im.save('lynnhood.jpg')

