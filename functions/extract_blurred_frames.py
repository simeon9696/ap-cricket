import cv2 as cv
import os
import shutil
from progress.bar import ChargingBar


def create_dirs():
    # Create blurry and non-blurry image paths if they don't exist. Otherwise delete them
    blurry = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','images' ,'blurry'))
    non_blurry = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images', 'non_blurry'))
    if not os.path.exists(blurry) or not os.path.exists(non_blurry):
        # If it doesn't exist make it
        os.mkdir(blurry)
        os.mkdir(non_blurry)
    else:
        # Otherwise delete the folder and all of it's contents
        print("[INFO] Clearing old blurry and non_blurry folder")
        shutil.rmtree(blurry)
        shutil.rmtree(non_blurry)
        # Then re-create an empty folder
        os.mkdir(blurry)
        os.mkdir(non_blurry)
    return blurry, non_blurry

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv.Laplacian(image, cv.CV_64F).var()



blurry_path, non_blurry_path = create_dirs()
path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images'))
image_paths = [os.path.join(path, fn) for fn in next(os.walk(path))[2]]


THRESHOLD = 200
NUMBER_OF_IMAGES = len(image_paths)
# loop over the input images
with ChargingBar(f'[INFO] Separating {NUMBER_OF_IMAGES} images into blurry and non-blurry with a threshold of {THRESHOLD}', max=NUMBER_OF_IMAGES) as bar:
    for imagePath in image_paths:
        # load the image, convert it to grayscale, and compute the
        # focus measure of the image using the Variance of Laplacian
        # method
        image = cv.imread(imagePath)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        
        
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        if fm < THRESHOLD:
            text = "Blurry"
            # Copy image to blurry folder
            shutil.copy2(imagePath, blurry_path)
        else:
            text = "Not Blurry"
            # Copy image to bob_blurry folder
            shutil.copy2(imagePath, non_blurry_path)

        # Advance progress bar
        bar.next()

        """       
        # Uncomment this block if you want to see the image and fm value    
        cv.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
            cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        cv.imshow("Image", image)
        key = cv.waitKey(0)
        """
