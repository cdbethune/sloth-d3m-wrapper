# Sloth D3M Wrapper
Wrapper of the Sloth clustering primitives (the base Sloth library can be found here: https://github.com/NewKnowledge/sloth) into D3M infrastructure. All code is written in Python 3.5 and must be run in 3.5 or greater. 

## Install

pip3 install -e git+https://github.com/NewKnowledge/sloth-d3m-wrapper.git#egg=SlothD3MWrapper --process-dependency-links

## Output
The output is a DataFrame containing a single column where each entry is the associated series' cluster number.

## Available Functions

#### produce
Produce primitive's best guess for the cluster number of each series. The input is a pandas frame where each row is a series. Series timestamps are stored in the column names. The output is a dataframe containing a single column where each entry is the associated series' cluster number.
