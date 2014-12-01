ISS-Data-Validator
==================

Validates a csv file to make sure that it does not contain any sort of malformed data.  It will attempt to fix all problems with the file, and list all of the things that it can not fix for the user to manually fix.  

To run it, download a copy of the data from the Google Classroom, and export it as a CSV file.  Then open up a terminal and run
```
python Validator.py [filename.csv]
```
This will list all the problems, and if there are none, you can have it print out the parsed file to the terminal.  
