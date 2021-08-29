import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter


def color_extractor(number, picture):

    image = cv.imread(picture)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    clt = KMeans(n_clusters=number)
    clt.fit(image.reshape(-1, 3))

    n_pixels = len(clt.labels_)
    counter = Counter(clt.labels_)  # count how many pixels per cluster
    percent = {}
    for i in counter:
        percent[i] = np.round(counter[i] / n_pixels, 2)

    # for logging purposes
    # print(percent)
    # print(clt.cluster_centers_)

    for n in range(len(percent)):
        percent['#%02x%02x%02x' % tuple(clt.cluster_centers_[n, :].astype(int))] = percent.pop(n)
        percent = dict(sorted(percent.items(), key=lambda item: item[1], reverse=True))
    return percent.items()
