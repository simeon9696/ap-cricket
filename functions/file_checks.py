import os
import shutil

#########################################################
# Determine if paths for images and labels for training #
# and validation datasets are valid. Throw exception if #
# they are not and return False for unsuccessful status #
#########################################################
def check_dirs(IMAGE_PATH, LABEL_PATH):

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
            print(f"[SUCCESS] Images and labels found")
    except Exception as error:
        PATHS_GOOD = False
        print(f"\x1b[6;37;41m[ERROR] {error}\x1b[0m")
    return PATHS_GOOD


#########################################################
# Count the number of images and labels.If they don't   #
# match, throw an error                                 #
#########################################################
def file_count(IMAGE_PATH,LABEL_PATH):

    IMAGES_COUNT =  len(next(os.walk(IMAGE_PATH))[2])
    LABELS_COUNT =  len(next(os.walk(LABEL_PATH))[2])
    COUNT_EQUAL = False
    try:
        if not(IMAGES_COUNT == LABELS_COUNT):
            MESSAGE = f"File count mismatch. {IMAGES_COUNT} images and {LABELS_COUNT} labels. These counts should match"
            
            raise Exception(MESSAGE)
        else:
            print(f"[SUCCESS] Equal number of image and label files")
            COUNT_EQUAL = True
    except Exception as error:
        print(f"\x1b[6;37;41m[ERROR] {error}\x1b[0m")
    return  COUNT_EQUAL

#########################################################
# Determine if each filename in images/ has a matching  #
# filename in labels/                                   #
#########################################################
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
        print(f"[SUCCESS] All image files have a corresponding label file")
    else:
        print("[INFO] These file names don't exist as a pair i.e they do not have a corresponding label file for the image file or vice versa")
        print(NON_PARIED_FILES)

    return ALL_FILES_PAIRED


#########################################################
# Save the trained model weights as .pth in the         #
# directory specified                                   #
#########################################################
def save_model(MODEL_PATH, MODEL):
    MODEL_NAME = 'model_weights.pth'

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

    MODEL.save(os.path.join(MODEL_PATH, 'model_weights.pth'))
    print(f"[INFO] Saved model '{MODEL_NAME }' in {MODEL_PATH}")
    return
    
#########################################################
# Save the user supplied class names in the directory   #
# specified                                             #
#########################################################
def save_class_names(MODEL_PATH, CLASS_NAMES):
    CLASS_NAME_PATH = os.path.join(MODEL_PATH, 'class_names.txt')

    class_name_file = open(CLASS_NAME_PATH,"w") 
    class_name_file.write(', '.join(CLASS_NAMES))
    print(f"[INFO] Class names written to {CLASS_NAME_PATH}")
    return

#########################################################
# Convert the list of losses to string and write to file#
# in directory supplied                                 #
#########################################################
def save_losses(MODEL_PATH, losses):
    LOSSES_PATH = os.path.join(MODEL_PATH, 'losses.txt')

    loss_file = open(LOSSES_PATH,"w") 
    loss_file.write(str(losses))
    print(f"[INFO] Loss data written to to {LOSSES_PATH}")
    return

#########################################################
# Zip contents of directory supplied and store at in    #
# current working directory                             #
#########################################################
def zip_model_and_loss_and_class_names(MODEL_PATH):
    shutil.make_archive('modeldata', 'zip', MODEL_PATH)
    return