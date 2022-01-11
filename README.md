# name-detection

## Installation requirements and installation guides

These instructions are for identifying names in your text and de-identifying the text. You will work mostly in the terminal with the exception of downloading Python directly from the Python website.

* Step 1: Download [Python 3](https://www.python.org/downloads/macos/), the code has been run and tested on version 3.9.1 so it is suggested this version is used. Follow instructions on installer to complete Python installation.
* Step 2: Open Terminal by typing “Terminal” in search bar.
* Step 3: Install **pandas** by typing the following command in the terminal. Note 'pandas' may have already been installed along with Python in which case you will recieve a message saying 'requirement already satisfied'. If you recieve this message, proceed onto Step 4.
  ```
  pip3 install pandas
  ```
* Step 4: Install **numpy** by typing the following command in the terminal. Note 'numpy' may have already been installed along with Python in which case you will recieve a message saying 'requirement already satisfied'. If you recieve this message, proceed onto Step 5.
  ```
  pip3 install numpy
  ```
* Step 5: Install **transformers** by typing the following command in the terminal. Note 'transformers' may have already been installed along with Python in which case you will recieve a message saying 'requirement already satisfied'. If you recieve this message, proceed onto Step 6.
  ```
  pip3 install transformers
  ```
* Step 6: Install **tensorflow** by typing the following command in the terminal. Note 'tensorflow' may have already been installed along with Python in which case you will recieve a message saying 'requirement already satisfied'. If you recieve this message, proceed onto Step 6.
  ```
  pip3 install tensorflow
  ```
  
## Folder Preparation
In order for the code to run:
* Input transcripts should be included in `./data` folder in the same directory as the code file.
* Output transcripts should be included in `./output` folder in the same directory as the code file.
* Check that these two folders are created prior to running the code. The data folder should have the files you intend to de-identify. The output folder would be empty.
* **Note.** If the repository folder is downloaded, this folder already satisfies the requirements above. 

## Running the code
With the terminal still open, navigate to the path where the code and data and output folders are located.
* Step 1: To check which directory you are currently in type in:
   ```
   pwd
   ```
   This will return your current direction path (e.g., /Users/janedoe/)
* Step 2: Assuming your code and necessary folders are in the folder called "name-detection" in the Desktop, change your directory to this folder by typing:
  ```
  cd /Users/janedoe/Desktop/name-detection
  ```
  This will direct you to your desired directory.
  
* Step 3: To check all the necessary files are in the folder, type in:
  ```
  ls
  ```
  You should see a list of all of files in the folder. This should include the .py code and the respective necessary folders in the directory. If you don't see this repeat Steps 1-3.
* Step 4: Run the code. Type in the command line:
  ```
  python3 name_detection.py
  ```
## Resulting Output
The code with beggining running. The transcripts will appear in the terminal as they are being de-identified. The sample transcripts will take approximately two minutes to complete.

#### Anonymized Transcripts

The anonymized transcripts output files will be saved in `./output` folder in the same directory as the code file. `-out` will be added to the original file name to represent the processed text files. Names are replaced with "name_#id" in the text files.

#### Name Keys

To allow the possibility for future analysis and retrieval of participant's background information, name id numbers and the associated names are saved in the same directory as the code file as `name_keys.csv`.
