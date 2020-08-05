# ap-cricket
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


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

## Usage
From the root directory of the project ```python main.py```

## Testing Command
From the tests directory  ```pytest --mocha```  
This will run all tests in the tests folder. Follow the naming convention when creating tests i.e. ```test_<your_name_here>```. This allows the test runner to automatically detect test files and run them. The output should look like below:
```
=========================================== test session starts ===========================================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: C:\Users\julis\Documents\ap-cricket\tests
plugins: mocha-0.4.0
collected 4 items

Package Check :: test_basic.py
    Python version
        ✓ Should have Python version >= 3.6
    Open CV
        ✓ Should have OpenCV version >= 4.2
    Numpy
        ✓ Should have Numpy version >= 1.1
    Matplotlib
        ✓ Should have Matplotlib version >= 3.0
                                         [100%]
============================================ 4 passed in 0.42s ============================================
```