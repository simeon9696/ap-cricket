from detecto import core, utils, visualize
import matplotlib.pyplot as plt
import os


# Directory at which the model is stored
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'model','model_weights.pth'))
IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'validation','images'))
CLASS_NAMES_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'model','class_names.txt'))
CLASS_NAMES =  open(CLASS_NAMES_PATH, "r").readline().split(',')

# Use the saved model to detect objects in images
model = core.Model.load(MODEL_PATH, CLASS_NAMES)

# Specify the path to your image
image = utils.read_image(os.path.join(IMAGE_PATH, 'image-178.jpg'))
predictions = model.predict(image)

# predictions format: (labels, boxes, scores)
labels, boxes, scores = predictions

print(labels) 
print(boxes)
print(scores)
visualize.show_labeled_image(image, boxes, labels)