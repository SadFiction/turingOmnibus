import matplotlib.pyplot as plt;
import numpy as np;

plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots()


def generate_bitmap(side_len:int) -> list:
    bitmap = []
    for i in range(0,side_len):
        bitmap.append([])
        for j in range(0,side_len):
            bitmap[i].append(0)
    return bitmap


def produce_wallpaper(side_len: int, resolution: int) -> list:
    bitmap = generate_bitmap(side_len=side_len)
    for i in range(1, resolution):
        
        for j in range(1, resolution):
            x = i*side_len/resolution
            y = j*side_len/resolution
            c = int(x*x + y*y)

            if c%2 == 0:
                bitmap[int(x)][int(y)] = 8.
            elif c%3 == 0:
                bitmap[int(x)][int(y)] = 4.
            else: 
                bitmap[int(x)][int(y)] = 0.
    return bitmap

length = int(input("Enter legth of side of wallpaper: "))
resolution = int(input("Enter resolution of wallpaper: "))
colourmap = "inferno"

#using ratios of length and resolution give similar patterns, for example the ratio of len:res of 4:5 gives a pattern that is repeatable and infinitly scalable, so does 1:1

data = np.array(produce_wallpaper(side_len=length, resolution=resolution))

plt.imshow(X=data, cmap=colourmap)
plt.show()

fig.savefig(f"wallpaper res={resolution}len={length}, colour={colourmap}.png")


