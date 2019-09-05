from PIL import Image

# rgba are next to each other
# format: [R,G,B,A, R,G,B,A, R,G,B,A...]
def imageToRBGAArray(path_to_image, convert=False):
    im = Image.open(path_to_image)
    if convert and im.mode == 'RGB':
        im = im.convert('RGBA')
    width, height = im.size
    channels = len(im.getbands())
    pix = im.load()
    res = []
    for y in range(height):
        for x in range(width):
            res.extend(list(pix[x,y]))
            # print(pix[x,y])

    return res, width, height, im.mode

def RGBAArrayToImage(image, width, height, mode):
    im = Image.new(mode, (width, height))
    channels = len(mode)
    # print(channels)
    res = []
    for i in range(0, len(image), channels):
        res.append(tuple([image[i + j] for j in range(0, channels)]))
    im.putdata(res)
    return im

# ----------------------------------------------------

# each channel is separate, goes by each row, col
# format: [[[R,R,R...],[R,R,R...]...],
#          [[G,G,G...],[G,G,G...]...],
#          [[B,B,B...],[B,B,B...]...],
#          [[A,A,A...],[A,A,A...]...]]
def imageToRGBAMultiDim(path_to_image, convert=False):
    im = Image.open(path_to_image)
    if convert and im.mode == 'RGB':
        im = im.convert('RGBA')
    width, height = im.size
    channels = len(im.getbands())
    res = [[[0] * width for _ in range(height)] for i in range(channels)]
    pix = im.load()
    curr = 0
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                res[c][y][x] = pix[x,y][c]
    return res, width, height, im.mode

def RGBAMultiDimToImage(image, width, height, mode):
    im = Image.new(mode, (width, height))
    channels = len(mode)
    res = [[] for _ in range(channels)]
    for i in range(channels):
        for j in range(len(image[i])):
            res[i].extend(image[i][j])
    res = list(zip(*res))
    im.putdata(res)
    return im


# ----------------------------------------------------

# each channel is separate, goes by each row
# format: [[R,R,R,R,R,R...],
#          [G,G,G,G,G,G...],
#          [B,B,B,B,B,B...],
#          [A,A,A,A,A,A...]]
def imageToRGBASingleArrs(path_to_image, convert=False):
    im = Image.open(path_to_image)
    if convert and im.mode == 'RGB':
        im = im.convert('RGBA')
    width, height = im.size
    channels = len(im.getbands())
    res = [list(i) for i in zip(*im.getdata())]
    # res = [[[0] * (width * height)] for i in range(channels)]
    # pix = im.load()
    # curr = 0
    # for y in range(height):
    #     for x in range(width):
    #         curr = y * width + x
    #         for c in channels:
    #             res[c][curr] = pix[x,y][c]
    return res, width, height, im.mode

def RGBASingleArrsToImage(image, width, height, mode):
    im = Image.new(mode, (width, height))
    # channels = len(mode)
    im.putdata(list(zip(*image)))
    return im

# ----------------------------------------------------

# Everything is together, but R is first, then G, B,...
# format [R,R,R,...,
#         G,G,G,...,
#         B,B,B,...,
#         A,A,A,...]
def imageToSingleArr(path_to_image, convert=False):
    im = Image.open(path_to_image)
    if convert and im.mode == 'RGB':
        im = im.convert('RGBA')
    width, height = im.size
    channels = len(im.getbands())
    res = [0] * (height * width * channels)
    pix = im.load()
    curr = 0
    for c in range(channels):
        for y in range(height):
            for x in range(width):
                curr = (c * height + y) * width + x
                res[curr] = pix[x,y][c]
    return res, width, height, im.mode

def singleArrToImage(image, width, height, mode):
    im = Image.new(mode, (width, height))
    res = [[] for _ in range(width * height)] 
    channels = len(mode)
    curr = 0
    for y in range(height): 
        for x in range(width):
            curr = y * width + x
            for i in range(channels):
                res[curr].append(image[i * width * height + curr])
            res[curr] = tuple(res[curr])
    im.putdata(res)
    return im

# ----------------------------------------------------

# rgba are next to each other
# format: [[R,G,B,A], [R,G,B,A], [R,G,B,A]...]
def imageToRGBALists(path_to_image, convert=False):
    im = Image.open(path_to_image)
    if convert and im.mode == 'RGB':
        im = im.convert('RGBA')
    width, height = im.size
    channels = len(im.getbands())
    pix = im.load()
    res = [None] * (width * height)
    for y in range(height):
        for x in range(width):
            res[y * width + x] = list(pix[x,y])
    return res, width, height, im.mode

def RGBAListToImage(image, width, height, mode):
    im = Image.new(mode, (width, height))
    res = [None] * (width * height)
    for y in range(height):
        for x in range(width):
            res[y * width + x] = tuple(image[y * width + x])
    im.putdata(res)
    return im