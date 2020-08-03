olypmicsfile = open("olympics.txt", "r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print('{} is on the roster for {}'.format(values[0], values[4]))
    if('Finland' in values):
        print("Is from Finlad")
    print("original line", ",".join(values))

olypmicsfile.close()
