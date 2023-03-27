import sys
import numpy as np
from PIL import Image


def bmp_to_array(filepath):
    with Image.open(filepath) as img:
        img_array = np.array(img)
    return img_array


def get_bmp_header(filepath):
    with open(filepath, 'rb') as f:
        # BMP header is 54 bytes
        bmp_header = f.read(54)
    return bmp_header


def RLE(type, img_array):
    rle = []

    if type == "satir":
        # Tüm satırlar
        for i in range(0, len(img_array)):
            pixel = img_array[i][0]
            count = 1
            compressed_line = []
            # Tek satır
            for j in range(1, len(img_array[0])):
                next_pixel = img_array[i][j]
                if (pixel == next_pixel).all():
                    count += 1
                else:
                    compressed_line.append(count)
                    compressed_line.append(pixel[1])
                    pixel = next_pixel
                    count = 1
            compressed_line.append(count)
            compressed_line.append(pixel[1])
            # print("LINE > ", compressed_line)

            rle.append(compressed_line)
    elif type == "sütun":
        # Tüm sütunlar
        for i in range(0, len(img_array[0])):
            pixel = img_array[0][i]
            count = 1
            compressed_line = []
            # Tek sütun
            for j in range(1, len(img_array)):
                next_pixel = img_array[j][i]
                if (pixel == next_pixel).all():
                    count += 1
                else:
                    compressed_line.append(count)
                    compressed_line.append(pixel[1])
                    pixel = next_pixel
                    count = 1
            compressed_line.append(count)
            compressed_line.append(pixel[1])
            # print("LINE > ", compressed_line)

            rle.append(compressed_line)
    elif type == "zigzag":

        lol = []
        for i in range(len(img_array)):
            for j in range(len(img_array[0])):
                if i % 2 == 0:
                    lol.append(img_array[j][i])
                else:
                    lol.append(img_array[len(img_array) - j - 1][i])
        # print(lol)
        pixel = lol[0]
        count = 1
        compressed_line = []
        for i in range(1, len(lol)):
            next_pixel = lol[i]
            if (pixel == next_pixel).all():
                count += 1
            else:
                compressed_line.append(count)
                compressed_line.append(pixel[1])
                pixel = next_pixel
                count = 1
            compressed_line.append(count)
            compressed_line.append(pixel[1])


        
        rle.append(compressed_line)
        # print("LINE > ", compressed_line)
    return rle




def get_length(arr):
    length = 0
    for i in range(len(arr)):
        length += len(arr[i])
    return length


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Yanlış argüman")
        print("Kullanım: python RLE.py [image_filepath]")
        quit()
    else:
        image_filepath = sys.argv[1]

    # Get BMP header
    header = get_bmp_header(image_filepath)

    # Get image array
    img_array = bmp_to_array(image_filepath)


    raw = img_array.shape[0] * img_array.shape[1]
    encoded_satir = RLE("satir", img_array)
    encoded_sutun = RLE("sütun", img_array)
    encoded_zigzag = RLE("zigzag", img_array)
    print("Length RAW:  ", raw)
    print("Length Encoded Satır:  ", get_length(encoded_satir))
    print("Length Encoded Sütun:  ", get_length(encoded_sutun))
    print("Length Encoded ZigZag: ", get_length(encoded_zigzag))





