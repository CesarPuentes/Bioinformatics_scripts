import os


# change to folder with data files
os.chdir("/home/cesar/Desktop/New/")


# Aminoacid dictionary: One to Three
CODE = {"A":"ala", "G":"gly", "I":"ile", "L":"leu",
       "P":"pro", "V":"val", "UCA":"S", "F":"phe",
       "W":"trp", "Y":"tyr", "D":"asp", "E":"glu",
       "R":"arg", "H":"his", "K":"lys", "S":"ser",
       "T":"thr", "C":"cys", "M":"met", "N":"asn",
       "Q":"gln",}


##Alternate dictionary method. User input dependent
 ##def triplet(s):
   ##   a = ' '.join(CODE.get(i.upper()) for i in s)
     ##  return a

# Aminoacid convertion: One to Three
def triplet(convert_string):
    res = ''
    for c in convert_string:
        try:
            res += CODE[c] + ' '
        except KeyError:
            pass
    return res

# File length-detector function
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# Open file with peptide list
f = open("M_list", "r")
# Read file
data = f.read()
#Remove \n
new = data.replace("\n","")
#Convert to list
s = list(new)
#Make altenate string for data visualization
string = data.split()
print("Input sequence(s): ", string)
print("Number of peptide lines entered:", file_len("M_list"))

##Loop variable initiation

#Index related variable
l = -1
#Index related variable
z = 0

with open("Complete.com", "w") as text_file:
    for x in range (file_len("M_list")):
        #C=9 so it starts printing from 10
        c = 9
        z = 0 + x
        e = z * 12
        with open("Output2.com", "w") as text_file2:
            for j in range (12):
                c = c+1
                z = s[j+e]
                y = triplet(z)
                text_file2.write("swapaa %s #0:%s.p \n" %(y, c))
                text_file.write("swapaa %s #0:%s.p \n" %(y, c))
                
           


                 
                 


