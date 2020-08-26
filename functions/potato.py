from detecto import core, utils, visualize
import matplotlib.pyplot as plt
import os

IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'images'))
LABEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'labels'))


'''image = utils.read_image(os.path.join(IMAGE_PATH, 'image0.jpg'))
plt.imshow(image)
plt.show()'''



# Images and XML files in separate folders
dataset = core.Dataset(LABEL_PATH, IMAGE_PATH)

image, target = dataset[0]
print(image, target)

model = core.Model(['bat', 'batter', 'pitch', 'field', 'player', 'scoreboard'])

model.fit(dataset)


# Specify the path to your image
image = utils.read_image(os.path.join(IMAGE_PATH, 'image0.jpg'))
predictions = model.predict(image)

# predictions format: (labels, boxes, scores)
labels, boxes, scores = predictions

print(labels) 
print(boxes)
print(scores)
