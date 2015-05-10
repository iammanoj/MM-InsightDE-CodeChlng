#!/usr/bin/env bash
############################################
#       Program Name    :       Shell Script for executing WordCount and RunningMedian Python Programs
#       Description     :       This script checks for environment setup and then executes the WordCount and RunningMedian programs with neccessary parameters.
#       Coder           :       Manoj Mohan
#       Create Date     :       05/08/2015
#       Mod Log         :
#
#
#
############################################


# Check and install dependencies on the machine being run
if [ "$(uname)" == "Darwin" ]; then
    if ! type python > /dev/null; then
        # Install Homebrew
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        # Install Python
        brew install python
    fi
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    if ! type python > /dev/null; then
        apt-get install -y python
    fi
fi

# Check for script permissions
chmod a+x WordCount.py
chmod a+x RunningMedian.py

# Execute my programs, with the input directory wc_input and output the files in the directory wc_output
python WordCount.py ./wc_input ./wc_output/wc_result.txt
python RunningMedian.py ./wc_input ./wc_output/med_result.txt



