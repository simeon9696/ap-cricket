import cv2 as cv
import os
import shutil
# Opens the Video file


try:
    # Get absolute path to folder with videos
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'videos'))
    print(f"[INFO] Looking in {path} for videos...")

    # Get the absolute path to each video in the folder
    paths = [os.path.join(path, fn) for fn in next(os.walk(path))[2]]

    # Assert error and break execution if the directory is present but has no files
    assert( (not paths) == False), "[ERROR] Directory has no files"

    # Print the number of videos
    print(f"[INFO] Found {len(paths)} videos!")

    # Create directory 'images' to place generated frames
    processed_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images'))
    if not os.path.exists(processed_dir):
        # If it doesn't exist make it
        os.mkdir(processed_dir)
    else:
        # Otherwise delete the folder and all of it's contents
        shutil.rmtree(processed_dir)
        # Then re-create an empty folder
        os.mkdir(processed_dir)

    # yay
    i=0
    for video in paths:
        cap= cv.VideoCapture(video)
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            cv.imwrite((os.path.join(processed_dir,f'Image-{i}.jpg')),frame)
            i+=1
        
        cap.release()
        cv.destroyAllWindows()
        pass
except Exception as Argument:
    print(Argument)
    






