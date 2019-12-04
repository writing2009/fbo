# PreprocessFBOfile.py
# John Palmer
# writing2009@gmail.compile
# 20191202
# To fix 2019 12 02
    # Find out how many multiples their are <DESC>, <URL>, others like line number
    # Develop routine to determine worst case data structure
    # Figure out why some of the tsv have something in the first line (length of text)
    # Figure out maximum length of each filed
    # Figure out how to find errors in a line after processing
    # Figure out how to convert strings to dollars (and find those ones that are text writeups)
    # Figure out how to insert into noSQL database

# Import libraries
import os
import glob


# Set the default directory
# C:\fbo\data\processed
os.chdir('C:\\fbo\\data\\processed')


# End of transaction keywords
end_of_transaction_keywords = [
    "</AMDCSS>","</ARCHIVE>","</AWARD>","</COMBINE>","</FAIROPP>",
    "</FSTD>","</ITB>","</JA>","</MOD>","</PRESOL>","</SNOTE>",
    "</SRCSGT>","</SSALE>","</UNARCHIVE>"]

# Transaction attribute keywords
transaction_attributes = [
    "<PRESOL>", "<DATE>", "<YEAR>", "<AGENCY>", "<OFFICE>",
    "<LOCATION>", "<ZIP>", "<CLASSCOD>", "<NAICS>", "<OFFADD>",
    "<SUBJECT>", "<SOLNBR>", "<RESPDATE>", "<ARCHDATE>", "<CONTACT>",
    "<DESC>", "<LINK>", "<URL>", "<SETASIDE>", "</PRESOL>", "<EMAIL>",
    "<POPCOUNTRY>", "<POPZIP>", "<POPADDRESS>", "<SRCSGT>",
    "</SRCSGT>", "<SNOTE>", "</SNOTE>", "<COMBINE>", "</COMBINE>",
    "<AMDCSS>", "<NTYPE>", "</AMDCSS>", "<MOD>", "</MOD>", "<AWARD>",
    "<AWDNBR>", "<AWDAMT>", "<AWDDATE>", "<AWARDEE>", "</AWARD>",
    "<LINENBR>", "<JA>", "<STAUTH>", "</JA>", "<MODNBR>", "<FAIROPP>",
    "<FOJA>", "<DONBR>", "</FAIROPP>", "<ARCHIVE>", "</ARCHIVE>", 
    "<UNARCHIVE>", "</UNARCHIVE>", "<SSALE>", "</SSALE>"]

# Get a list of all the files in the assigned directory
for filename in glob.glob('FBOFeed*'):
    with open(filename, 'r+', encoding='latin_1') as file :
        filedata = file.read()

        # Change tabs to four spaces
        filedata = filedata.replace('\t', '    ')
        # Remove linefeeds
        filedata = filedata.replace('\n',' ')
        # Insert tab delimiters between transaction attributes
        for tabinsert in transaction_attributes:
            filedata = filedata.replace(tabinsert,'\t'+tabinsert)
        # Insert record delimiters between transactions
        for end_of_transaction in end_of_transaction_keywords:
            filedata = filedata.replace(
                end_of_transaction,end_of_transaction+'\n')

    # Write the the updated file
    with open('p'+filename+'.tsv', 'w', encoding='utf8') as outfile:
        outfile.write(filedata)



