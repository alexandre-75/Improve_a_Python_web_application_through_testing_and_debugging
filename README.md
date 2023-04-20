<p align="center">
  <img src="picture\16007798203635_P9.png" alt="logo" />
</p>

## The Project

- using the **Flask framework**
- using the **Locust plateforme**
- use of the Python test framework : **Pytest**
- Implement a Python **test** suite.
- Handle errors and exceptions in Python.
- Debug the code of a Python application.

## Context 

- Güdlft, a company that created a digital platform to coordinate competitions in North America and Australia.
- Güdlft began by organizing competitions for local clubs.
- Güdlft has grown in popularity and exclusively hosts competitions for fitness companies.
- create a simpler and less expensive version of their current platform for regional organizers.
- I am in charge of fixing the bugs of phase 1 and adding the expected functionality of phase 2.
- Each **correction / addition is on a branch**, and is supported by a test suite via Pytest and Locust.

## Database

- The app is powered by JSON files. 
- This is to get around having a DB until we actually need one. 

##  Project download

_Tested on Windows 10, Python 3.10.6._

[Technical Specifications ( french )](http://course.oc-static.com/projects/Python+FR/P9+Python+Testing+FR/Spe%CC%81cifications+fonctionnelles.pdf)

[Link I have folk for the project](https://github.com/OpenClassrooms-Student-Center/Python_Testing)


####  1. project recovery

    $ git clone https://github.com/alexandre-75/Improve_a_Python_web_application_through_testing_and_debugging.git

####  2. Creating a virtual environment

    python<version> -m venv nom_env_virtuel

    Activate the environment  `mon_env_virtuel\Scripts\activate` (Windows)

####  3. Installing packages
    pip<version> install -r requirements.txt

## Start the program

- ***Run the server*** by executing the command :
  ```
  set FLASK_APP=server.py

  flask run 
  ```

- Open your favorite browser and navigate to the ***local development server*** at :
  ```
  http://127.0.0.1:5000/
  ```
    
## Reports
#### 1. Locust

- Locust is an open-source Python load testing platform.
- It simulates users to test the resilience and performance of a web application.
- [See complete report](https://github.com/alexandre-75/Improve_a_Python_web_application_through_testing_and_debugging/blob/master/picture/rapport/locust.pdf)
<p align="center"><img src="https://github.com/alexandre-75/Improve_a_Python_web_application_through_testing_and_debugging/blob/master/picture/rapport/Capture%20d%E2%80%99%C3%A9cran%202023-04-20%20084130.jpg?raw=true" alt="rapport_locust" /></p>

###### to start the server : 
```
patch/tests/performance_tests/ 
```
- run the **locust** command in the terminal
- Go to the address **http://localhost:8089**
- enter **http://127.0.0.1:5000/** for -host-
- do not forget to activate the Flask server

#### 2. Coverage

- measures code coverage when running unit tests.
- it provides statistics on the percentage of code executed during tests.
- it runs with the command:

```
coverage run -m pytest tests
coverage report
```

<p align="center"><img src="https://github.com/alexandre-75/Improve_a_Python_web_application_through_testing_and_debugging/blob/master/picture/rapport/Capture%20d%E2%80%99%C3%A9cran%202023-04-20%20084339.jpg?raw=true" /></p>

#### 3. Pytest

- pytest is an open-source testing framework for Python

To perform all the unit and integration tests, enter the command:
```
pytest tests
```
<p align="center"><img src="https://github.com/alexandre-75/Improve_a_Python_web_application_through_testing_and_debugging/blob/master/picture/rapport/Capture%20d%E2%80%99%C3%A9cran%202023-04-20%20083523.jpg?raw=true" /></p>