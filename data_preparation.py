import requests #Module for getting image from the Internet
from PIL import Image
import numpy as np
import random
import os
import pickle

file_name = "Mars_MGS_MOLA_DEM.jpg"

# Check if the file exists or not
if os.path.isfile(file_name) == False:
    response = requests.get("http://planetpixelemporium.com/download/download.php?5672/mars_12k_topo.jpg")
    with open(file_name, "wb") as file: #Create a file with the name above and save the content of response to it
        file.write(response.content)

img = Image.open(file_name) #Open our saved file above
img = img.convert("L") #Convert to one channel grey image
img_array = np.asarray(img)  #Convert the image to an array
img_array = img_array.astype('int32')

img_size = [15,20,25,30,50,75,100]

x_max, y_max = img_array.shape

# arrays[size] stores the data of images having specific size
arrays = {}
data = {}

#Bin information
num_bins = 16
bin_size = 0.5

for size in img_size:
    arrays[size] = []
    for i in range(0, x_max - size + 1, size//5):
        for j in range(0, y_max - size + 1, size//5):
            section = img_array[i:i + size, j:j + size]
            arrays[size].append((section, np.std(section)))

for size in img_size:
    tmp_data = {}

    i = bin_size

    while i <= num_bins * bin_size:

        #Standard deviation filtering
        tmp_data[(i-bin_size,i)] = [arr[0] for arr in arrays[size] if arr[1] < i]

        #Randomize our data before writing it to a txt file
        random.shuffle(tmp_data[(i-bin_size,i)])

        #Save only 100 random images for analysis process
        tmp_data[(i-bin_size,i)] = tmp_data[(i-bin_size,i)][0:100]

        i += bin_size

    data[size] = tmp_data


#Path for storing our analysis results
path = "Analysis Results"
# Make folder if path does not exist
if os.path.exists(path) == False:
    os.mkdir(path)
