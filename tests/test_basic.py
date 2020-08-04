def test_check_python_version():
    '''Package Check :: Python version :: Should have Python version >= 3.6'''
    import sys
    PYTHON_VERSION = float(sys.version[:3])
    PYTHON_VERSION_REC = 3.6
    VERSION_OK = PYTHON_VERSION >= PYTHON_VERSION_REC and True or False
    assert VERSION_OK == True, f"Incorrect Python version. Version {PYTHON_VERSION} is installed but {PYTHON_VERSION_REC} is required"
    
    
def test_check_opencv():
    '''Package Check :: Open CV :: Should have OpenCV version >= 4.2'''
    import cv2 as cv
    OPENCV_VERSION = float(cv.__version__[:3])
    OPENCV_VERSION_REC = 4.2
    VERSION_OK = OPENCV_VERSION >= OPENCV_VERSION_REC and True or False
    assert VERSION_OK == True, f"Incorrect OpenCV version. {OPENCV_VERSION} is installed but {OPENCV_VERSION_REC} is required"

def test_check_numpy():
    '''Package Check :: Numpy :: Should have Numpy version >= 1.1'''
    import numpy as np
    NP_VERSION = float(np.__version__[:3])
    NP_VERSION_REC = 1.1
    VERSION_OK = NP_VERSION >= NP_VERSION_REC and True or False
    assert VERSION_OK == True, f"Incorrect numpy version. {NP_VERSION} is installed but {NP_VERSION_REC} is required"

def test_check_progress():
    '''Package Check :: Progress :: Should have Progress version >= 1.5'''
    import progress
    PGS_VERSION = float(progress.__version__[:3])
    PGS_VERSION_REC = 1.5
    VERSION_OK = PGS_VERSION >= PGS_VERSION_REC and True or False
    assert VERSION_OK == True, f"Incorrect numpy version. {PGS_VERSION} is installed but {PGS_VERSION_REC} is required"

def test_check_matplotlib():
    '''Package Check :: Matplotlib :: Should have Matplotlib version >= 3.0'''
    import matplotlib as plt
    PLT_VERSION = float(plt.__version__[:3])
    PLT_VERSION_REC = 3.2
    VERSION_OK = PLT_VERSION >= PLT_VERSION_REC and True or False
    assert VERSION_OK == True, f"Incorrect matplotlib version. {PLT_VERSION} is installed but {PLT_VERSION} is required"

