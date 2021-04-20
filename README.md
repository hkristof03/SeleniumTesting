# Selenium examples in Python
> Playing with the Selenium web application testing framework. The configuration file for the test methods describes the
>inputs for them as key-value pairs, with the expected outputs as well.

## Motivation

A few Selenium examples are demonstrated for Software Testing master course. The aim of the project is to try out Selenium 
capabilities on a web page which was specifically developed for this purpose: http://the-internet.herokuapp.com/

## Installation

Install [Anaconda](https://docs.anaconda.com/anaconda/install/) from the official page. Clone the project. Open an Anaconda terminal and create a new
virtual environment from the supplied config file:
```sh
conda create -n SeleniumTesting python=3.8 anaconda
conda activate SeleniumTesting
pip install selenium
```

## Usage example
```sh
pytest test_selenium.py -ssv --cov
```
Or
```sh
python -m unittest test_selenium.py
```

Project Organization
------------

    ├── README.md                       <- The top-level README for people who want to use this project.
    ├── config
    │   ├── test_config.yaml            <- Defines the inputs and outputs for the test methods.
    ├── chrome_driver
    │   ├── chrome_driver.exe           <- Driver of Chrome browser to run the tests.
    ├── data_test
    │   ├── file_upload_test.txt        <- A file with some content to test file upload.  
    ├── cookie.py                       <- Page object to manipulate cookies.
    ├── drag_and_drop.py                <- Page object to test drag and drop.
    ├── drag_and_dropy_javascript.py    <- Javascript defined in a Python string to test drag and drop.
    ├── page_base.py                    <- Page object to manipulate cookies.
    ├── page_dropdown.py                <- Page object to test dropdown feature.
    ├── page_file_upload.py             <- Page object to test file uploading.
    ├── page_hover.py                   <- Page object to test hover feature.
    ├── page_log_in.py                  <- Page object to test log in feature.
    ├── page_main.py                    <- Page object for the main page.
    ├── page_secure_download.py         <- Page object to manipulate cookies.
    ├── page_sign_in.py                 <- Page object to test sign in feature.
    ├── test_selenium.py                <- Unit testing methods.
    ├── utilities.py                    <- Utility functions.
--------

## Useful resources
[Selenium documentation for multiple languages](https://www.selenium.dev/documentation/en/getting_started/)  
[Selenium documentation for Python](https://selenium-python.readthedocs.io/)  
[Page Object Pattern](https://www.pluralsight.com/guides/getting-started-with-page-object-pattern-for-your-selenium-tests)  
[16 Selenium Best Practices](https://www.lambdatest.com/blog/selenium-best-practices-for-web-testing/)  


