# Task1.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: John Fay (jpfay@duke.edu)
# Created on: Oct 2012

# Copy and paste a line of data as the startLine variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split("\t")

# Assign variables to specfic items in the list
recordID = lineData[0]              # ARGOS tracking record ID
obsDateTime = lineData[2]           # Observation date and time (combined)
obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
obsLC = lineData[3]                 # Observation Location Class
obsLat = lineData[5]                # Observation Latitude
obsLon = lineData[6]                # Observation Longitude

# Print information to the user
print "According to record " + recordID, 
print "Sara was seen at " + obsLat + " d LAT; " + obsLat + " d LON on " + obsDate



# Task2.py
#
# Description: Reads in ARGOS data file and parses a line of ARGOS tracking data 
#
# Created by: John Fay (jpfay@duke.edu)
# Created on: Oct 2012

# Create a variable pointing to the file with no header
fileName = "V:\\Scripting3\\SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineString = fileObj.readline()

# Close the file object
fileObj.close()

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split("\t")

# Assign variables to specfic items in the list
recordID = lineData[0]              # ARGOS tracking record ID
obsDateTime = lineData[2]           # Observation date and time (combined)
obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
obsLC = lineData[3]                 # Observation Location Class
obsLat = lineData[5]                # Observation Latitude
obsLon = lineData[6]                # Observation Longitude

# Print information to the user
print "According to record " + recordID, 
print "Sara was seen at " + obsLat + " d LAT; " + obsLat + " d LON on " + obsDate


# Task3.py
#
# Description: Reads in ARGOS data and displays information to the user
#
# Created by: John Fay (jpfay@duke.edu)
# Created on: Oct 2012

# Create a variable pointing to the file with no header
fileName = "V:\\Scripting3\\SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineString = fileObj.readline()

# Use a while loop to read each line, one at a time, until the end of the file is reached
while lineString:

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    # Print information to the user
    print "According to record " + recordID, 
    print "Sara was seen at " + obsLat + " d LAT; " + obsLat + " d LON on " + obsDate

    # Read in the next line
    lineString = fileObj.readline()
    
# Close the file object
fileObj.close()