# name-detection

## Installation requirements and installation guides:
Upon installation of Python 3, the required modules can be installed through pip package manager or [Anaconda](https://docs.anaconda.com/anaconda/install/index.html). If Python 2 is also installed on the device, then you need to specify `pip3` to make sure the packages are properly installed on your desired Python version (Python 3).

* [Python 3](https://www.python.org/downloads/)
* [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
* [Numpy](https://numpy.org/install/)
* [Transformers](https://huggingface.co/docs/transformers/installation)

## Input and Output

### Input

The input transcripts should be included in `./data` folder in the same directory as the code file.

### Output

Output files will be saved in `./output` folder in the same directory as the code file. `-out` will be added to the original file name to represent the processed text files.

## Running Instructions

The script can be run through the command line as followed.

```
python3 name_detection.py
```
