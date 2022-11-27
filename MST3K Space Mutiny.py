# Sometime in April-July 2017 Ryftik Converted using Python 2 to 3 from the 2 version
# Generates a MST3K space mutiny name

import random
import os

#Files to open, and file path
Filepath = "" #No folder, would be the folder name the texts are in normally
FileA = "Firstname.txt"
FileB = "Lastname.txt"
repeats = 5 #Number of outputs to display in a go
displaytext = 'This is a tough guy\'s name:' #lede
intercalctext = ' ' #adds text between the file entries, in this a case a space between first name and lastname. Set to '' for no space

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Program guts below this line. Only change top,
    # unless you have more files or something
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

FileCatalogue = [FileA, FileB]
debug = False
if debug: print("Starting.")


def make_File_Locations(FileCatalogue, Filepath):
    if debug: print("Making file locations.")
    TEMP = []
    for i in range(len(FileCatalogue)):
        if debug: print (i, Filepath, FileCatalogue[i], TEMP)
        TEMP.append(Filepath + FileCatalogue[i])
    if debug: print(TEMP)
    return TEMP

#Thank you stack overflow.
#Waterman's "Reservoir Algorithm" from Knuth's "The Art of Computer Programming
#https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
#The num + 2 produces the sequence 2, 3, 4... The randrange will therefore be 0 with a probablity of 1.0/(num + 2) -- and that's the probability with which we must replace the currently selected line (the special-case of sample size 1 of the referenced algorithm -- see Knuth's book for proof of correctness == and of course we're also in the case of a small-enough "reservoir" to fit in memory;-)... and exactly the probability with which we do so.
def get_random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line

def array_to_string(description_array):
    full_string = ""
    for description in description_array:
        #description = description[:-1]
        #if description.endswith(' ') == False:
        #    description = description + ' '
        full_string = full_string + description
    return full_string
        

def generateDescription(FileCatalogue):
    FilePaths = []  #files+paths to files.
    description_array = [] #string array of descriptions
    FilePaths = make_File_Locations(FileCatalogue, Filepath)
    #if debug: print FilePaths
    fullpath = os.path.dirname(__file__) #<-- absolute directory  pathname this python script is in.
    if debug: print(fullpath)
    #if debug: print(os.listdir(Filepath))

    description_array = [] #string array of descriptions, reset
        
    #Gen a name
    try: #FileA
        #if debug: print FileCatalogue[1]
        if Filepath != "":
            if debug: print(os.path.join(Filepath, FileCatalogue[0]))
            currentfile = open(os.path.join(Filepath, FileCatalogue[0]), "r+")
        else:
            currentfile = open(FilePaths[0], "r+")
        description_array.append(get_random_line(currentfile).strip('\t\n\r'))#whitespace stripping + first name space
        description_array.append(intercalctext)
    except: #ValueError:
        description_array.append("Not able to get target line from: " + str(FileCatalogue[0]))
        
    try: #FileB
        #if debug: print FileCatalogue[2]
        if Filepath != "":
            if debug: print(os.path.join(Filepath, FileCatalogue[1]))
            currentfile = open(os.path.join(Filepath, FileCatalogue[1]), "r+")
        else:
            currentfile = open(FilePaths[1], "r+")
        description_array.append(get_random_line(currentfile).strip(' \t\n\r'))#whitespace stripping
    except: #ValueError:
        description_array.append("Not able to get target line from: " + str(FileCatalogue[1]))
       
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
    print(displaytext,array_to_string(description_array))

for i in range(0,repeats):        
    generateDescription(FileCatalogue)

input() #So it will pause in the command window. Hit Enter to close the program.
