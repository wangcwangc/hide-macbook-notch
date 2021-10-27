import sys
import getopt
from PIL import Image
import numpy as np

if __name__ == '__main__':
    input_file = ''
    output_path = ''
    percent = 0.023
    pixel = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:p:")
    except getopt.GetoptError:
        print("-i input_images -o output_path")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("-i input_images -o output_path")
        elif opt == "-i":
            input_file = arg
        elif opt == "-o":
            output_path = arg
        elif opt == "-p":
            pixel = int(arg)
    print("image : " + input_file)
    print("output path : " + output_path)
    image = Image.open(input_file)
    arr = np.array(image)
    if pixel == 0:
        pixel = len(arr) * percent
    for i in range(int(pixel)):
        temp = []
        for j in range(len(arr[0])):
            temp.insert(0, [0, 0, 0])
        arr = np.r_[[temp], arr]
    new_image = Image.fromarray(np.uint8(arr))
    new_image.save(output_path + '/new.jpg')
    print("success to save : " + output_path + "/new.jpg")
