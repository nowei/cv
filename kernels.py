import math
def create_gaussian(sigma):
    # needs 6 * sigma - 1 values
    size = 2 * math.ceil(3 * sigma) + 1
    a = [[0] * size for _ in range(size)]
    TWO_SIG2 = 2 * sigma ** 2
    COEFF = 1 / (math.pi * TWO_SIG2)
    s = 0
    for x in range(-size // 2, size // 2 + 1):
        for y in range(-size // 2, size // 2 + 1):
            a[x + size // 2][y + size // 2] = COEFF * math.e ** -((x ** 2 + y ** 2)/TWO_SIG2)
            s += a[x + size // 2][y + size // 2]
    for x in range(size):
        for y in range(size):
            a[x][y] /= s
    return a

# For the purpose of testing convolution
def create_identity(width):
    size = 2 * width + 1
    a = [[0] * size for _ in range(size)]
    a[size//2][size//2] = 1
    for l in a:
        print(l)
    return a

if __name__ == "__main__":
    create_gaussian(0.5)
    create_identity(3)