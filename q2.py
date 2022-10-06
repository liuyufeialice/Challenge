import numpy as np
import random

LENGTH = 100000
# here we generate 2 images: parasite and dye. Parasite is at least 25% of the image size. 
# 0.1% of chance, that dye will be more than 10% of parasite blob.
def generate_images():
    start_x,start_y,end_x,end_y = find_coordinates()
    parasite_image = np.full((LENGTH, LENGTH), 255, dtype=np.uint8)
    parasite_blob = np.full((abs(start_x-end_x),abs(start_y-end_y)), 0, dtype=np.uint8)
    parasite_image[start_x:end_x,start_y:end_y] = parasite_blob

    random_int = random.random()
    size_percentage = randomNumber(0,0.1)
    if random_int < 0.01:
        size_percentage = randomNumber(0.1,1)
    dye_image = np.full((LENGTH, LENGTH), 255, dtype=np.uint8)
    dye_end_x = int(size_percentage*abs(start_x-end_x))
    dye_end_y = int(size_percentage*abs(start_y-end_y))
    dye_blob = np.full((dye_end_x,dye_end_y), 0, dtype=np.uint8)
    dye_image[start_x:start_x+dye_end_x,start_y:start_y+dye_end_y] = dye_blob

    return [parasite_image, dye_image]

def find_coordinates():
    coord_x, coord_y = np.random.randint(0,LENGTH, (2,)) 
    candidates_x = [coord_x, LENGTH - coord_x]
    candidates_y = [coord_y, LENGTH - coord_y]
    for index_x, x in enumerate(candidates_x):
        for index_y, y in enumerate(candidates_y):
            print(x,y)
            print(x*y/(LENGTH * LENGTH))

            if x * y >= 0.25 * LENGTH * LENGTH:
                start_x = 0 if index_x == 0 else LENGTH
                start_y = 0 if index_y == 0 else LENGTH
                return [min(start_x, coord_x), min(start_y, coord_y),
                    max(start_x, coord_x), max(start_y, coord_y)]
    return [0,0,0,0]

def randomNumber(min, max):
    return random.random() * (max - min) + min


