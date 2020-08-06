olypmicsfile = open("olympics.txt", "r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print('{} is on the roster for {}'.format(values[0], values[4]))
    if('Finland' in values):
        print("Is from Finlad")
    print("original line", ",".join(values))

olypmicsfile.close()


    
boardfile = open("board.txt", "w")
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]

for stopword in stopwords:
    boardfile.write(stopword + "\n")

boardfile.close()


##
## REading data from a CSV file

 fileconnection = open("olympics.txt", 'r')
 lines = fileconnection.readlines()
 header = lines[0]
 field_names = header.strip().split(',')
 print(field_names)
 for row in lines[1:]:
     vals = row.strip().split(',')
     if vals[5] != "NA":
         print("{}: {}; {}".format(
                 vals[0],
                 vals[4],
                 vals[5]))


olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    # row_string = ','.joint([olympian[0], olympian[1], olympian[2]]) # array or tuple
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()



### More efficient way to read a file when it is too large

fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    for lin in fileref:                   # step 2
        ## some code that reference the variable lin
#some other code not relying on fileref   # step 3