# Example Python Project

This program reads data representing voltage over time from a set of CSV files. The output of the program is a chart which visually shows the voltage over time for the set of experiments.



## NLDL Project

The sample data set for this course is the NLDL Data set from F. Kubke. The full data set is over 200 files, but only 5 have been included in this project as sample data.

NLDL stands for "Nucleus Laminaris Delay Lines". The data in each file describes the voltage over time at a specific location in the brain of a finch.

In simple terms an electrical stimulation was applied at the point where sound enters the brain, and then electrodes measured the voltage over time at a range of locations.

By measuring the time delay from stimulation to peak voltage for each data file, we can obtain secondary data which can be combined to determine whether the stimulation came from the left ear or right ear.

The plotted data from each file is expected to produce a waveform.



## Running the Program

This project contains a Python script which processes all CSV files in a given folder, and also a set of Jupyter Notebooks pages which help explain some of the data processing.

The output of the program is a chart image which displays the time series data from each CSV file as a different colour line.


### Processing the Sample Data

The Python script must be run from the command line.

1. Open your command line to the `sample-python-project` folder.
2. Enter the following command and press Enter:
  `python nldl.py`

The program should create an image called `test.png` in the `output` folder.


### Processing Your Own Data

Ensure you have run the program using the sample data first, so you can be sure there are no errors with the program or your Python installation.

See the **Data Structure** section below for information on how your CSV files must be formatted.

1. Create a new folder called `my_data` in the `sample-python-project` folder.
2. Copy your CSV files to the `my_data` folder.
3. Open the file `nldl.py` in a code editor.
4. Modify the `source_folder` setting at the top of the file to use one of your data files:
  ```
  source_folder = 'my_data'
  ```
5. Save your changes.
6. Open your command line to the `sample-python-project` folder.
7. Enter the following command and press Enter:
  `python nldl.py`

The program should create an image called `test.png` in the `output` folder.




## Data Structure

This program assumes that the source folder contains CSV files in the following format:

- **Column 1 and Column 2** contain metadata labels and their matching metadata values respectively.
- **Column 4 and Column 5** contain time readings (milliseconds) and voltage readings respectively.

Column 3 is unused.

**Note:** The file extension must be ".CSV" in capital letters.


