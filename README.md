 # motion-sensor

"Doorbell written in python. Application works with IPWebCam (Android application that runs server allowing for eg. fetch photo (.png) and informations about changes in the picture).

#### Setup

###### Commands below assumes that they are executed in root directory of repository

1. Install **python3**, **python3-pip**, and **cmake** (package manager depends on system/distribution you use).
    
2. Install **virtualenv**.
    ```bash
    python3 -m pip install virtualenv
    ```
    
3. Create virtual environment wherever you want (np. 'env')
    ```bash
    python3 -m virtualenv env
    ```
    
4. Start virtualenv
    Linux/MacOS
    ```bash
    source env/bin/activate
    ```
    
    Windows
    ```bash
    source env/Scripts/activate.bat
    ```
5. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Install IPWebcam on Android device

7. Start IPWebcam

8. Update configuration file (motionsensor/properties.json)
    * a change of 'ip_cam_addr' in mandatory.
    * add your own photos to folder defined by 'image_folder_location' and provide them to 'users'

9. Run montion-sensor
    ```bash
    python motionsensor/main.py
    ```

#### Useful commands
- exit venv
    ```bash
    deactivate
    ```
- save dependencies to requirements.txt (in root directory of repository)
    ```bash
    pip freeze > requirements.txt
    ```

# Test execution
Unit test framework: **pytest**

1. Install **motionsensor** as local package
    ```bash 
    pip install -e .
    ```

2. Start tests.
    ```bash 
    pytest tests
    ```

- Tests need to be executed in root folder of repository.
- All tests has to be be stored in 'tests'.
- Every test file and test function has to contain prefix 'test_'.
