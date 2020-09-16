from detecto import core, utils, visualize
import matplotlib.pyplot as plt
import os
from datetime import datetime
import time

import shutil

import file_checks as fc


'''
# This shows an image from your training set. 
# Use to validate that paths are correct
image = utils.read_image(os.path.join(IMAGE_PATH, 'image0.jpg')) # image0.jpg is a name of an image in the training set, change accordingly
plt.imshow(image)
plt.show()
'''

IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'training', 'images'))
LABEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'training', 'labels'))
VAL_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'validation', 'images'))
VAL_LABEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'validation', 'labels'))
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'model'))
PATHS_GOOD = COUNT_EQUAL = ALL_FILES_PAIRED = VAL_PATHS_GOOD = VAL_COUNT_EQUAL = VAL_ALL_FILES_PAIRED = ALL_CLEAR False
CLASS_NAMES = ['bat','stumps']


print(f"[INFO] Checking testing dataset")
PATHS_GOOD = fc.check_dirs(IMAGE_PATH,LABEL_PATH)
COUNT_EQUAL = fc.file_count(IMAGE_PATH,LABEL_PATH)
ALL_FILES_PAIRED = fc.identify_non_paired_file(IMAGE_PATH,LABEL_PATH)

print(f"[INFO] Checking validation dataset")
VAL_PATHS_GOOD = fc.check_dirs(VAL_IMAGE_PATH, VAL_LABEL_PATH)
VAL_COUNT_EQUAL = fc.file_count(VAL_IMAGE_PATH, VAL_LABEL_PATH)
VAL_ALL_FILES_PAIRED = fc.identify_non_paired_file(VAL_IMAGE_PATH, VAL_LABEL_PATH)

ALL_CLEAR = PATHS_GOOD and COUNT_EQUAL and ALL_FILES_PAIRED and VAL_PATHS_GOOD and VAL_COUNT_EQUAL and VAL_ALL_FILES_PAIRED

'''
if ALL_CLEAR:
    
    
    print(f"[INFO] All file checks passed, beginning dataset loading !")
    # Images and XML files in separate folders
    dataset = core.Dataset(LABEL_PATH, IMAGE_PATH)
    
    # Validation dataset
    val_dataset = core.Dataset(VAL_LABEL_PATH, VAL_IMAGE_PATH)

    model = core.Model(CLASS_NAMES)
    TIME_START = datetime.now()
    print(f"[INFO] Training started at {TIME_START.strftime('%H:%M:%S')}")
    losses = model.fit(dataset, val_dataset, epochs=15,
                learning_rate=0.001, verbose=True)

    plt.plot(losses)
    plt.show()
    TIME_END = datetime.now()
    TRAINING_TIME = (TIME_END-TIME_START).total_seconds() / 60
    print(f"[INFO] Training finised at {TIME_END.strftime('%H:%M:%S')} and took {TRAINING_TIME} minutes")


    # Model generated successfully, save to disk 
    
    save_model(MODEL_PATH, model)
    save_class_names(MODEL_PATH, model)
    save_losses(MODEL_PATH, losses)
    zip_model_and_loss_and_class_names(MODEL_PATH)
'''
