import numpy as np

LENGTH = 100000
# To scan for cancer, read the images, then compare pixel by pixel to see how many black spaces
# In here use 0 to represent black, 1 to represent white.
# Add parasite image array and dye image array together. If black portion is overlayed, then sum of the pixels should be 0, otherwise greater than 0.
# Count how many black pixels are at the same place, if it is more than 10% of parasite size, then it has cancer.
def uncompress_image(compressed_image):
    uncompressed_image_array = []
    tuple_array = np.array_split(compressed_image, len(compressed_image)/2)
    for occurrance, color in tuple_array:
        uncompressed_image_array += (int(occurrance)*[int(color)])
    return np.array(uncompressed_image_array).reshape(LENGTH, LENGTH)

def scan_cancer(parasite_image, dye_image):
    parasite_sum = LENGTH * LENGTH - np.sum(parasite_image)
    comparison = dye_image+parasite_image
    comparison = comparison == 0
    return 100 * np.sum(comparison) / parasite_sum > 10

def read_image(filename):
    with open(filename) as f:
        contents = f.read()
        compressed_image_array = contents.split(" ")
        return uncompress_image(compressed_image_array)
 
parasite = read_image("output.txt")
dye = read_image("output.txt")
result = scan_cancer(parasite, dye)