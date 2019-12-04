# PreprocessFBOfile.py
# John Palmer
# writing2009@gmail.compile
# 20191204

# Import libraries
import os
import glob
#import numpy as np
import re


# Set the processed ETL directory
os.chdir('C:\\fbo\\data\\processed')

# Create a blank list
listOfTags = []
unique_list = []

# Process all the pFBOFeed* files
for filename in glob.glob('pFBOFeed*'):
    with open(filename, 'r+', encoding="latin_1") as f:
        listOfTags = re.findall(r"\<(.*?)\>",f.read())
    f.close()

for x in listOfTags:
    if x not in unique_list and str.isupper(x):
        unique_list.append(x)

#Write the list of unique tags to disk
unique_tagfileoutput = open('unique_tagfile.txt','w')
print(unique_list, file=unique_tagfileoutput)
unique_tagfileoutput.close()
