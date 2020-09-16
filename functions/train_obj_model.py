from detecto import core, utils, visualize
import matplotlib.pyplot as plt
from datetime import datetime
import shutil
import time
import os

import file_checks as fc


'''
# This shows an image from your training set. 
# Use to validate that paths are correct
image = utils.read_image(os.path.join(IMAGE_PATH, 'image0.jpg')) # image0.jpg is a name of an image in the training set, change accordingly
plt.imshow(image)
plt.show()
'''
# The path to training images
IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'training', 'images'))

# The path to training LABELS
LABEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'training', 'labels'))

# The path to validation images
VAL_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'validation', 'images'))

# The path to validation LABELS
VAL_LABEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'validation', 'labels'))

# The path you want the model, loss information and class names to be stored
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'model'))

# All the class names that are present in the labels
CLASS_NAMES = ['bat','stumps']




ALL_CLEAR=[
    fc.check_dirs(IMAGE_PATH,LABEL_PATH),
    fc.file_count(IMAGE_PATH,LABEL_PATH),
    fc.identify_non_paired_file(IMAGE_PATH,LABEL_PATH),
    fc.check_dirs(VAL_IMAGE_PATH, VAL_LABEL_PATH),
    fc.file_count(VAL_IMAGE_PATH, VAL_LABEL_PATH),
    fc.identify_non_paired_file(VAL_IMAGE_PATH, VAL_LABEL_PATH),
]

if all(ALL_CLEAR):
    
    print(f"[INFO] All file checks passed, beginning dataset loading")
    # Images and XML files in separate folders
    dataset = core.Dataset(LABEL_PATH, IMAGE_PATH)
    
    # Validation dataset
    val_dataset = core.Dataset(VAL_LABEL_PATH, VAL_IMAGE_PATH)

    # Give model all class names that are present in labels
    model = core.Model(CLASS_NAMES)

    # Log time training began
    TIME_START = datetime.now()
    print(f"[INFO] Training started at {TIME_START.strftime('%H:%M:%S')}")

    # Start training with defined parameters
    # verbose= true prints the current epoch and loss after each epoch
    losses = model.fit(dataset, val_dataset, epochs=1,
                learning_rate=0.001, verbose=True)



    # Log time training complet
    TIME_END = datetime.now()
    TRAINING_TIME = (TIME_END-TIME_START).total_seconds() / 60
    print(f"[INFO] Training finised at {TIME_END.strftime('%H:%M:%S')} and took {TRAINING_TIME} minutes")

    # Plot the losses vs epoch after training has completed
    # Note this blocks the thread. If you don't want to see the plot comment 
    # the two lines below out
    # plt.plot(losses)
    # plt.show()

    # Model generated successfully, save to disk 
    print(f"[SUCCESS] Model trained successfully!")
    save_model(MODEL_PATH, model)
    save_class_names(MODEL_PATH, CLASS_NAMES)
    save_losses(MODEL_PATH, losses)
    zip_model_and_loss_and_class_names(MODEL_PATH)
else:
    print(f"\x1b[6;37;41m[ERROR] File checks failed. There is likely additional logging above\x1b[0m")

