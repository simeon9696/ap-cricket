# ap-cricket

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This repository is repsonsible for splitting a group of videos into images and then categorizing those images into blurry or not blurry by calculating the variation of the Laplacian.

## Getting Started

This project is built with Python v3.8.3 and uses the following dependancies. Please install the pacakages below before attempting to run any of the code in this respository.

- OpenCV  
    `pip install opencv-python`  
- Numpy  
    `pip install numpy`  
- Matplotlib  
    `pip install matplotlib`  
- Progress  
    `pip install progress`  
- Pytest-Mocha  
    `pip install pytest-mocha`
- PyTorch  
    `torch==1.4.0 torchvision==0.5.0`
- Detecto  
    `pip install detecto`

## Extracting frames from video

- Place videos in the `videos` folder
- Run `extract_all_frames.py`
- Run `extract_blurred_frames.py`
- Results will be in the `images` folder

## Training object detection model

- Label images using labelImg
- Put images for training dataset into training/images
- Put labels for training dataset into training/labels
- Put images for validation dataset into validation/images
- Put labels for validation dataset into validation/labels
- Run `train_obj_model.py`

## Using the model

- Put testing images into testing/
- Change filename so that it corresponds to image name in `obj_detection.py`
- Run `obj_detection.py`

## Testing Command

From the tests directory  ```pytest --mocha```  
This will run all tests in the tests folder. Follow the naming convention when creating tests i.e. ```test_<your_name_here>```. This allows the test runner to automatically detect test files and run them. The output should look like below:

```text
=========================================== test session starts ===========================================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: C:\Users\<YOUR_USERNAME>\Documents\ap-cricket\tests
plugins: mocha-0.4.0
collected 5 items

Package Check :: test_basic.py
    Python version
        ✓ Should have Python version >= 3.8
    Open CV
        ✓ Should have OpenCV version >= 4.2
    Numpy
        ✓ Should have Numpy version >= 1.1
    Progress
        ✓ Should have Progress version >= 1.5
    Matplotlib
        ✓ Should have Matplotlib version >= 3.0
                                         [100%]
============================================ 4 passed in 0.42s ============================================
```
