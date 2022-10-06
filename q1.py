import numpy as np

# For both image types, I'd store them using lossless compression. 
# Without compression, it would take 10^5 * 10^5 bits storage because each pixel is a binary with a size of a bit.
# With lossless compression, the first number represents the number of pixels, the second number the color of the pixel.
# For example, data 0 0 0 0 0 0 1 1. It would be represented as 6 0 2 1. 
# Worse case 26 * 10^5 bytes. Worst case is every line there is more than one black pixel. 
# It would look like a repeated of X 0 Y 1 for 10^5 times. Each number is a char taking a byte, so 0 and 1 are 2 bytes. There are 4 spaces taking 4 bytes. 
# The largest number of X would be less than 10^10 so X or Y could take up to 10 bytes.  
# Here uses 0 to represent black, 1 to represent white.
def store_image(image_array, filename):
    compressed_array = []
    previous_color = -1
    consecutive_count = 0
    for index, color in enumerate(image_array):
        color = 1 if color > 0 else 0

        if previous_color < 0:
            consecutive_count += 1
            previous_color = color
            continue

        if color == previous_color:
            consecutive_count += 1
        else:
            compressed_array.append(consecutive_count)
            compressed_array.append(previous_color)
            consecutive_count = 1

        if index == len(image_array) - 1:
            compressed_array.append(consecutive_count)
            compressed_array.append(color)

        previous_color = color

    output = ' '.join(map(str, compressed_array))

    with open(filename, "w") as f:
        f.write(output)