# source: //github.com/mushahidq/py_colour_identifier/blob/main/colour_identifier.ipynb

# Import libraries
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from collections import Counter

#Display the output of matplotlib inline
#%matplotlib inline

# Reading Images
def get_img(img_path):
    img = cv2.imread(img_path)
    #Convert the image to original colors i.e. RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

#Define the HEX values of colours
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

#Returns the colours in the image
def get_colours(img_path, no_of_colours, show_chart):
    img = get_img(img_path)
    #Reduce image size to reduce the execution time
    mod_img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
    #Reduce the input to two dimensions for KMeans
    mod_img = mod_img.reshape(mod_img.shape[0]*mod_img.shape[1], 3)

    #Define the clusters
    clf = KMeans(n_clusters = no_of_colours, n_init = no_of_colours)
    labels = clf.fit_predict(mod_img)

    counts = Counter(labels)
    counts = dict(sorted(counts.items()))

    center_colours = clf.cluster_centers_
    ordered_colours = [center_colours[i] for i in counts.keys()]
    hex_colours = [RGB2HEX(ordered_colours[i]) for i in counts.keys()]
    rgb_colours = [ordered_colours[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize=(8, 6))
        plt.pie(counts.values(), labels=hex_colours, colors=hex_colours)
        plt.show()
        return
    else:
        return hex_colours
