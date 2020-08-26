from detecto import core, utils, visualize
import matplotlib.pyplot as plt
from detecto.utils import read_image

import os

IMAGE_PATH = os.path.join('C:/Users/julis/Documents/ap-cricket/functions/images')
LABEL_PATH = os.path.join('C:/Users/julis/Documents/ap-cricket/functions/labels')

'''
image = read_image(os.path.join(IMAGE_PATH, 'image0.jpg'))
plt.imshow(image)
plt.show()
'''

# Images and XML files in separate folders
dataset = core.Dataset(r"C:/Users/julis/Documents/ap-cricket/functions/labels/", r"C:/Users/julis/Documents/ap-cricket/functions/images/")

image, target = dataset[0]
print(image, target)

model = core.Model(['bat', 'batter', 'pitch', 'field', 'player', 'scoreboard'])

model.fit(dataset)


# Specify the path to your image
image = utils.read_image('C:/Users/julis/Documents/ap-cricket/functions/images/image0.jpg')
predictions = model.predict(image)

# predictions format: (labels, boxes, scores)
labels, boxes, scores = predictions

print(labels) 
print(boxes)
print(scores)
