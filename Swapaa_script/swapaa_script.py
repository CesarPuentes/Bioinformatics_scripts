import os
import Midas
from chimera import runCommand as run, openModels
from Midas import write

# change to folder with data files
os.chdir("/home/cesar/Desktop/Swapaa_script")


# Aminoacid dictionary: One to Three
CODE = {"A":"ala", "G":"gly", "I":"ile", "L":"leu",
       "P":"pro", "V":"val", "UCA":"S", "F":"phe",
       "W":"trp", "Y":"tyr", "D":"asp", "E":"glu",
       "R":"arg", "H":"his", "K":"lys", "S":"ser",
       "T":"thr", "C":"cys", "M":"met", "N":"asn",
       "Q":"gln",}


# Aminoacid convertion: One to Three
def triplet(convert_string):
    res = ''
    for c in convert_string:
        try:
            res += CODE[c] + ' '
        except KeyError:
            pass
    return res

# File length function
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

    


# Open file with peptide list
f = open("M_list", "r")
data = f.read()
print("Input sequences:\n",data)
new = data.replace("\n","")
s = list(new)
print(s)
print("Number of peptide lines entered:", file_len("M_list"))


##Loop variable initiation

#Index related variable
l = -1
#Index related variable
z = 0

pdb_path = "/home/cesar/Desktop/Swapaa_script/Mutations/"


with open("Complete.com", "w") as text_file:

    for x in range (file_len("M_list")):
        #C=9 so it starts printing from 10
        c = 9
        z = 0 + x
        print("Z value: ", z)
        e = (z * 9)
        print("E value: ", e)
        Midas.open("Output2.com")
        run('write relative #0 #0 %smutation_%s.pdb' %(pdb_path, x))
        with open("Output2.com", "w") as text_file2:
            for j in range (9):
                c = c+1
                print("J value: ", j)
                print("E value next loop: ", e)
                z = s[j+e]
                print(j+e)
                print("index value: ", z)
                y = triplet(z)
                text_file2.write("swapaa %s #0:%s.p \n" %(y, c))
                text_file.write("swapaa %s #0:%s.p \n" %(y, c))


f.close()
text_file.close()
text_file2.close()





