############################################
#	Program Name	:	Word Count
#	Description	:	This program scans thru a given directory for files and then computes word counts from all files in the input directory and then prints total word counts alphabetically along with the word.
#	Coder		:	Manoj Mohan
#	Create Date	:	05/07/2015
#	Mod Log		:
#
#
#
############################################
## Import libraries
import os, sys
from collections import Counter
import fileinput

### First argument is for Input directory to scan files
InputFilesDir = sys.argv[1]
### Second argument is for the output directory to write results file
OutputFile = sys.argv[2]
### List for storing all parsed words from all input files
WordList = []

### Main method to process input files to determine word counts
def main():
    #InputFilesDir is the directory path to scan for files
    FilesList = os.listdir(InputFilesDir)

    for File in FilesList:
        FileNamePath = os.path.join(InputFilesDir, File)

        # Check if file still exists or has been deleted by some other program
        if os.path.isdir(FileNamePath):
            continue

        # Check if the file has any data, more than zero bytes
        if os.path.getsize(FileNamePath) > 0:
            with open(FileNamePath) as FilePtr:
                for Line in FilePtr:
                    Words = Line.split() 
                    for word in Words:
                        WordList.append(word.lower())
            FilePtr.close()

### Method to write the word count results to results file.
def WriteResults():
    WriteFilePtr = open(OutputFile, "w")
    for item,cnt in sorted(Counter(WordList).items()):
        WriteFilePtr.write(str(item) + "\t" +  str(cnt) + "\n")
    WriteFilePtr.close()

### Code execution starts here
if __name__ == '__main__':
    main()
    WriteResults()
    print "WordCount program SUCCESS!"
