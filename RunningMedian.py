############################################
#	Program Name	:	Running Median
#	Description	:	This program scans thru a given directory for files and then words in each line to compute median count cumulatively of the words until that line from the start.
#	Coder		:	Manoj Mohan
#	Create Date	:	05/08/2015
#	Mod Log		:
#
#
#
############################################
## Import OS libraries
import os, sys
from collections import Counter
import numpy

### First argument is for Input directory to scan files
InputFilesDir = sys.argv[1]
### Second argument is for the output directory to write results file
OutputFile = sys.argv[2]
MedianList = []

def main():
    #InputFilesDir is the directory path to scan for files
    FilesList = os.listdir(InputFilesDir)

    ### This is the consolidated file with text from all input files. This step is to prevent Dirty reads because of someone trying to modify an input file while this program is running. 
    MedianFileName = "med_summary_file.txt"
    MedianFileNamePath = os.path.join(InputFilesDir, MedianFileName)
    MedianFilePtr = open(MedianFileNamePath, "w")

    ### Sort the list of files and then process one file at a time in loop. Concatenate the output of all input files into one file.
    for File in sorted(FilesList):
        FileNamePath = os.path.join(InputFilesDir, File)
        with open(FileNamePath) as FilePtr:
            MedianFilePtr.write(FilePtr.read())
        FilePtr.close()
    MedianFilePtr.close()

    MedianFilePtr = open(MedianFileNamePath, "r")
    with open(MedianFileNamePath) as MedianFilePtr:
        for Line in MedianFilePtr:
            WordCntPerLine = len(Line.split())
            MedianList.append(WordCntPerLine)
    MedianFilePtr.close()

    ### Remove the interim consolidated file. This interim file ensures that if any source input files are modified after start of this program, that does not result in a dirty read.
    os.remove(MedianFileNamePath)

def WriteMedianResultsFile():
    MedianResultFilePtr = open(OutputFile, "w")
    i = 1
    while i<= len(MedianList):
        MedianVal = str(numpy.median(MedianList[0:i]))
        MedianResultFilePtr.write(MedianVal + "\n")
        i+= 1
    MedianResultFilePtr.close()
 
if __name__ == '__main__':
    main()
    WriteMedianResultsFile()
    print "RunningMedian program SUCCESS!"
