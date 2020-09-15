from detecto import core, utils, visualize
import matplotlib.pyplot as plt
import os
from datetime import datetime
import time

import shutil

def check_dirs(IMAGE_PATH, LABEL_PATH):
    # Create blurry and non-blurry image paths if they don't exist. Otherwise delete them
    PATHS_GOOD = False

    try:
        
        if not os.path.exists(IMAGE_PATH):
            MESSAGE = f"{IMAGE_PATH} not found"
            raise Exception (MESSAGE)
        elif not os.path.exists(LABEL_PATH):
            MESSAGE = f"{LABEL_PATH} not found"
            raise Exception (MESSAGE)
        else:
            PATHS_GOOD = True
            print(f"\x1b[6;37;42m[SUCCESS] Training images and labels found !\x1b[0m")
    except Exception as error:
        PATHS_GOOD = False
        print(f"\x1b[6;37;41m[ERROR] {error}\x1b[0m")
    
    
    return PATHS_GOOD

def file_count(IMAGE_PATH,LABEL_PATH):

    IMAGES_COUNT =  len(next(os.walk(IMAGE_PATH))[2])
    LABELS_COUNT =  len(next(os.walk(LABEL_PATH))[2])
    COUNT_EQUAL = False
    try:
        if not(IMAGES_COUNT == LABELS_COUNT):
            MESSAGE = f"File count mismatch. {IMAGES_COUNT} images and {LABELS_COUNT} labels. These counts should match"
            
            raise Exception(MESSAGE)
        else:
            print(f"\x1b[6;37;42m[SUCCESS] Equal number of image and label files !\x1b[0m")
            COUNT_EQUAL = True
    except Exception as error:
        print(f"\x1b[6;37;41m[ERROR] {error}\x1b[0m")


    return  COUNT_EQUAL


def identify_non_paired_file(IMAGE_PATH, LABEL_PATH):
    IMAGE_NAMES =   next(os.walk(IMAGE_PATH))[2]
    LABEL_NAMES =   next(os.walk(LABEL_PATH))[2]
    IMAGE_NAMES_EXTENSION_STRIPPED = [os.path.splitext(x)[0] for x in IMAGE_NAMES]
    LABEL_NAMES_EXTENSION_STRIPPED = [os.path.splitext(x)[0] for x in LABEL_NAMES]
    ALL_FILES_PAIRED = False

    # Find names that only appear in either IMAGE_NAMES only or LABEL_NAMES only
    NON_PARIED_FILES = list(set(IMAGE_NAMES_EXTENSION_STRIPPED) 
                            - set(LABEL_NAMES_EXTENSION_STRIPPED ))

    if not NON_PARIED_FILES:
        ALL_FILES_PAIRED = True
        print(f"\x1b[6;37;42m[SUCCESS] All image files have a corresponding label file !\x1b[0m")
    else:
        print("[INFO] These file names don't exist as a pair i.e they do not have a corresponding label file for the image file or vice versa")
        print(NON_PARIED_FILES)

    return ALL_FILES_PAIRED

def save_model(MODEL_PATH, MODEL):
    print(f"\x1b[6;37;42m[SUCCESS] Model trained successfully!\x1b[0m")
    if not os.path.exists(MODEL_PATH):
        # If it doesn't exist make it
        os.mkdir(MODEL_PATH)

        print(f"[INFO] Creating directory to save model in {MODEL_PATH}")
    else:
        # Otherwise delete the folder and all of it's contents
        print(f"[INFO] Removing {MODEL_PATH}")
        shutil.rmtree(MODEL_PATH)
        # Then re-create an empty folder
        
        print(f"[INFO] Creating directory to save model in {MODEL_PATH}")
        os.mkdir(MODEL_PATH)

    
    print(f"[INFO] Saving model in {MODEL_PATH}")
    MODEL.save(os.path.join(MODEL_PATH, 'model_weights.pth'))
    return
    
def save_class_names(MODEL_PATH,model):
    CLASS_NAME_PATH = os.path.join(MODEL_PATH, 'class_names.txt')
    print(f"[INFO] Writing class names to {CLASS_NAME_PATH}")
    
    class_name_file = open(CLASS_NAME_PATH,"w") 
    class_name_file.write(', '.join(CLASS_NAMES))
    return

def zip_model_and_class_names(MODEL_PATH):
    shutil.make_archive('model_data', 'zip', MODEL_PATH)
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
PATHS_GOOD = COUNT_EQUAL = ALL_FILES_PAIRED = False
CLASS_NAMES = ['bat','stumps']


PATHS_GOOD = check_dirs(IMAGE_PATH,LABEL_PATH)
COUNT_EQUAL = file_count(IMAGE_PATH,LABEL_PATH)
ALL_FILES_PAIRED = identify_non_paired_file(IMAGE_PATH,LABEL_PATH)

if PATHS_GOOD and COUNT_EQUAL and ALL_FILES_PAIRED: 
    
    
    print(f"[INFO] All file checks passed, beginning dataset loading !")
    # Images and XML files in separate folders
    dataset = core.Dataset(LABEL_PATH, IMAGE_PATH)
    
    # Validation dataset
    val_dataset = core.Dataset(VAL_IMAGE_PATH, VAL_LABEL_PATH)

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
    zip_model_and_class_names(MODEL_PATH)