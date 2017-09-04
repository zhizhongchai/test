import ctypes

from PIL import Image, ImageDraw
import numpy as np
import os


def array_to_image(a, name):
    r = Image.fromarray(a[:, :, 0])
    g = Image.fromarray(a[:, :, 1])
    b = Image.fromarray(a[:, :, 2])
    image = Image.merge("RGB", (r, g, b))
    image.save('logs3/' + str(name) + '.png')


def condition1(data, i, j, scale):
    for x in range(1, 4):
        scale = int(scale / x)
        # print(scale)
        if (data[i - scale, j - scale] == 0):
            return False
        if (data[i - scale, j + scale] == 0):
            return False
        if (data[i + scale, j - scale] == 0):
            return False
        if (data[i + scale, j + scale] == 0):
            return False
    return True


def condition2(data, i, j, scale):
    center = data[i - scale:i + scale, j - scale: j + scale]
    patch = data[i - 40:i + 39, j - 40: j + 39]
    if (np.mean(center) > 240):
        return False
    if (np.mean(patch) > 230):
        return False

    return True


def condition3(data, i, j):
    center = data[i - 40:i + 39, j - 40: j + 39]
    if (np.mean(center) / 255 > 0.5):
        return True
    return False


# image = Image.open('5801image.png')
# label = Image.open('5801label.png')
#
# lData = np.array(label)
# mData = np.array(image)



num = 0

# for i in range(26):
#     for j in range(26):
#         if (lData[i * 79 + 40, j * 79 + 40] == 255):
#             if (condition(lData, i * 79 + 40, j * 79 + 40,28)):
#                 data = mData[i * 79:i * 79 + 79, j * 79:j * 79 + 79]
#                 num = num + 1
#                 drawObject.rectangle((j * 79, i * 79, j * 79 + 79, i * 79 + 79), outline='blue')
#
# image.show()
# image.save('1.png')
# print(num)

filepath = 'cancerpng/'
labelpath = 'label/'

pathDir = os.listdir(filepath)
for file in pathDir:

    image = Image.open(filepath + file)
    label = Image.open(labelpath + file)
    lData = np.array(label)
    mData = np.array(image)
    drawObject = ImageDraw.Draw(image)

    i = j = 0
    while (i < 246):
        j = 0
        while (j < 246):

            if (lData[i * 8 + 40, j * 8 + 40] != 255):
                j = j + 1
            elif (lData[i * 8 + 40, j * 8 + 40] == 255):
                # if (condition1(lData, i * 8 + 40, j * 8 + 40, 28)):
                if (condition3(lData, i * 8 + 40, j * 8 + 40)):
                    # print(np.mean(mData[i * 8 + 40, j * 8 + 40], axis=0))
                    if (condition2(mData, i * 8 + 40, j * 8 + 40, 4)):
                        # if (i >= 0):
                        data = mData[i * 8:i * 8 + 79, j * 8:j * 8 + 79]
                        num = num + 1
                        # array_to_image(data, num)
                        drawObject.rectangle((j * 8, i * 8, j * 8 + 79, i * 8 + 79), outline='blue')
                    j = j + 9
                else:
                    j = j + 1
        i = i + 9
    image.save('cancerlabel4/' + file)
print(num)



# i = 0
# j = 0
# while (i < 238):
#     j = 0
#     i = i + 10
#     while (j < 238):
#         if (lData[i * 8 + 75, j * 8 + 75] != 255):
#             j = j + 1
#         elif (lData[i * 8 + 75, j * 8 + 75] == 255):
#             if (condition(lData, i * 8 + 75, j * 8 + 75, 50)):
#                 data = mData[i * 8:i * 8 + 151, j * 8:j * 8 + 151]
#                 num = num + 1
#                 # print(num)
#                 # array_to_image(data, num)
#                 drawObject.rectangle((j * 8, i * 8, j * 8 + 151, i * 8 + 151), outline='blue')
#                 j = j + 18
#             else:
#                 j = j + 1
# label.show()
# image.save('4.png')
# print(num)




# filepath = 'cancerpng/'
# labelpath = 'label/'
#
# pathDir = os.listdir(filepath)
# for file in pathDir:
#
#     image = Image.open(filepath + file)
#     label = Image.open(labelpath + file)
#     lData = np.array(label)
#     mData = np.array(image)
#     drawObject = ImageDraw.Draw(image)
#
#     i = 0
#     j = 0
#     while (i < 492):
#         j = 0
#         i = i + 19
#         while (j < 492):
#             if (lData[i * 4 + 40, j * 4 + 40] != 255):
#                 j = j + 1
#             elif (lData[i * 4 + 40, j * 4 + 40] == 255):
#                 if (condition1(lData, i * 4 + 40, j * 4 + 40, 28)):
#                     # print(np.mean(mData[i * 8 + 40, j * 8 + 40], axis=0))
#                     if (condition2(mData, i * 4 + 40, j * 4 + 40, 4)):
#                         # if (i >= 0):
#                         data = mData[i * 4:i * 4 + 79, j * 4:j * 4 + 79]
#                         num = num + 1
#                         # array_to_image(data, num)
#                         drawObject.rectangle((j * 4, i * 4, j * 4 + 79, i * 4 + 79), outline='blue')
#                     j = j + 19
#                 else:
#                     j = j + 1
#
#     image.save('cancerlabel1/' + file)
# print(num)
