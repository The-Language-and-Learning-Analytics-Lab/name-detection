# name-detection

## Installation requirements and installation guides

Upon installation of Python 3, the required modules can be installed through pip package manager or [Anaconda](https://docs.anaconda.com/anaconda/install/index.html). If Python 2 is also installed on the device, then you need to specify `pip3` to make sure the packages are properly installed on your desired Python version (Python 3).

* [Python 3](https://www.python.org/downloads/)
* [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
* [Numpy](https://numpy.org/install/)
* [Transformers](https://huggingface.co/docs/transformers/installation)


### Installing through Anaconda

Anaconda is a python environment manager through which you can create, activate, and deactivate different python versions and environments. Anaconda is available in two versions, command line and graphical interface. The graphical version is installed through [here](https://www.anaconda.com/products/individual). More documentations on installation and package managing can be found on [Anaconda website](https://docs.anaconda.com/anaconda/). However the main steps to follow is described here:

* Step 1: Downloading [Anaconda graphical installer](https://www.anaconda.com/products/individual), [doc](https://docs.anaconda.com/anaconda/install/)
* Step 2: Launch Anaconda-Navigator, [doc](https://docs.anaconda.com/anaconda/user-guide/getting-started/)
* Step 3: Create a python3 environment, [doc](https://docs.anaconda.com/anaconda/navigator/tutorials/create-python35-environment/), manage an environment, [doc](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/)
* Step 4: Installing the required packages on the environemt just created, [doc](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/) ([Here](https://docs.anaconda.com/anaconda/navigator/tutorials/pandas/) is an example of creating an environment and installing Pandas package on it)
* Step 5: Launch a python IDE (Jupyter notebook, Spyder, or Pycharm) through Anaconda Navigator homepage.
* Step 6: Open the code file through the python IDE and run the code in that environment.

### Installing through Python

While Anaconda offers an easier way for begginers to interact with python and create, and manage environments, python can also be installed through the [python website](https://www.python.org/downloads/).

## Input and Output

### Input

The input transcripts should be included in `./data` folder in the same directory as the code file.

### Output

#### Anonymized Transcripts

The anonymized transcripts output files will be saved in `./output` folder in the same directory as the code file. `-out` will be added to the original file name to represent the processed text files. Names are replaced with "name_#id" in the text files.

#### Name Keys

To allow the possibility for future analysis and retrieval of participant's background information, name id numbers and the associated names are saved in the same directory as the code file as `name_keys.csv`.

## Running Instructions

Step 1: Open Terminal by typing “Terminal” in search bar

Step 2: Type in the command line window:

```
python3 name_detection.py
```
