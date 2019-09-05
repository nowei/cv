def convolution(kernel, original):
    return convolution_simple(kernel, original)
    # if len(original) < len(kernel) or len(original[0]) < len(kernel[0]):
    #     return convolution_simple(kernel, original)
    # return convolution_v1(kernel, original)

# decent parallelization
def convolve(kernel, x, y, original):
    size = len(kernel)
    # start_y = max(0, y - size // 2)
    # end_y = min(len(original), y + size // 2)
    # start_x = max(0, x - size // 2)
    # end_x = min(len(original[0]), x + size // 2)
    half = size // 2
    init_x = max(0, x - half) - x
    init_y = max(0, y - half) - y
    end_x = min(len(original[0]), x + half) - x
    end_y = min(len(original), y + half) - y
    s = 0

    # print(init_y, end_y, init_x, end_x)
    for j in range(init_y, end_y):
        for i in range(init_x, end_x):
            s += original[y + j][x + i] * kernel[j + half][i + half]
            # print(original, y+j, x+i, j, i)
    return s

def convolution_simple(kernel, original):
    a = [[0] * len(original[0]) for _ in range(len(original))]
    for row in range(len(original)):
        for col in range(len(original[0])):
            a[row][col] = convolve(kernel, col, row, original)
    return a

# def convolution_v1(kernel, original):
#     a = [[0] * len(original[0]) for _ in range(len(original))]
