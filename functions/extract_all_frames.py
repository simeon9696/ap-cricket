import cv2 as cv
import os
import shutil
from progress.bar import ChargingBar
import time
# Opens the Video file


def with_opencv(filename):
    import cv2
    video = cv2.VideoCapture(filename)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    return frame_count
    
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
        print("[INFO] Clearing old images folder")
        shutil.rmtree(processed_dir)
        # Then re-create an empty folder
        os.mkdir(processed_dir)


    total_frames = 0
    for video in paths:
        total_frames += int(with_opencv(video))

    
    with ChargingBar('[INFO] Splitting videos into images', max=total_frames) as bar:
       
        i=1
        for video in paths:
            cap= cv.VideoCapture(video)
            
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == False:
                    break
                cv.imwrite((os.path.join(processed_dir,f'image-{i}.jpg')),frame)
                
                i+=1
                bar.next()
            cap.release()
            cv.destroyAllWindows()   
            
        # bar.finish()

    print(f"[INFO] Successfully split {len(paths)} videos into {total_frames} images in {processed_dir}")





except Exception as Argument:
    print(Argument)
    






