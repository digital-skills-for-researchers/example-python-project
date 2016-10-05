#!python3.5
from pathlib import Path
import matplotlib.pyplot as pyplot
import os



# VARIABLES #############################################

source_folder = 'data'
output_folder = 'output'





# FUNCTIONS #############################################

'''
Converts a CSV file into a Python object.

@param csv_file: A CSV file to convert
@returns file_object: A Python object containing the extracted file data
'''
def convert_csv_to_object(csv_file):

    metadata = {} # metadata stored as a dictionary
    readings = [] # readings stored as a list

    for line in file:

        # split the line into a list at every comma
        row_data = line.split(',')

        # get any available metadata from that row
        key = row_data[0]
        value = row_data[1]

        if key:
            meta_value = { key: value }
            metadata.update(meta_value)
        
        # get any available reading data from that row
        time = row_data[3]
        voltage = row_data[4]

        if time and voltage:
            reading = {
                'time': time,
                'voltage': voltage
            }
            
            readings.append(reading)
    
    # create a python object using the information
    file_object = {
        'metadata': metadata,
        'readings': readings
    }    

    return file_object



'''
Creates a chart using matplotlib and saves it to
the output folder specified at the start of the script.

If a file with the same name already exists it will
be automatically overwritten.

@param file_object: A Python object representing the input data
@returns None
'''
def create_chart_from_data(file_object):

    x_data = []
    y_data = []

    for reading in file_object['readings']:
        
        time = reading['time']
        time = float(time) * 1000
        x_data.append(time)
        
        voltage = reading['voltage']
        y_data.append(voltage)

    pyplot.style.use('ggplot')

    pyplot.title("NLDL Data")
    pyplot.xlabel("Time (ms)")
    pyplot.ylabel("Voltage")

    pyplot.axvline(x=0, color='blue')

    pyplot.plot(x_data, y_data)
    
    output_file_path = 'output/' + 'test' + '.png'
    pyplot.savefig(output_file_path)




# SCRIPT ################################################


# Get a list of all CSV files in the source folder
source_path = Path(source_folder)
csv_files = source_path.glob('*.CSV')
csv_files = list(csv_files)

# Report number of CSV files to the user
number_of_files = len(csv_files)
print( number_of_files, 'CSV files found')

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each file
for file in csv_files:
    
    # open the file
    file = file.open()

    # convert it to a Python object
    file_object = convert_csv_to_object(file)

    # create and save a chart from the data
    create_chart_from_data(file_object)




# Give final feedback to the user
print('Processing Complete!')
print('You can find your charts in the', output_folder,'folder.')





