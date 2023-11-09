#user will choose afile and 
#and search how many line start with 
#specific name
fname = input("enter the file name ?\n")
fhand = open(fname)
count =0
for line in fhand:
    if line.startswith("x"):
        count =count +1
    
        print ("there is ",count,"start with x")
        print (line.startswith("x"))