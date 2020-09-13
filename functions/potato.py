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
index = 0
for i in dataset:
    index = index + 1
    image,target = i
    print(index)
    print(image,target)

model = core.Model(['bat', 'batter', 'pitch', 'field', 'player', 'scoreboard', 'stumps'])

model.fit(dataset)


# Specify the path to your image
image = utils.read_image(os.path.join(IMAGE_PATH, 'image-3361.jpg'))
predictions = model.predict(image)

# predictions format: (labels, boxes, scores)
labels, boxes, scores = predictions

print(labels) 
print(boxes)
print(scores)
