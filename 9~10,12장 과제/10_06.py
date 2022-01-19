import random

infile = open("numbers.txt","w")

for i in range(1,11):
        su = str(random.randint(1,100));
        infile.write(su)
        infile.write("\n")

        
infile.close()