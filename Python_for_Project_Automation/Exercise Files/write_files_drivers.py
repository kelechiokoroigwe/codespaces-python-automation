# open inputFileDrivers.txt with the intention of reading it
inputFileDrivers = open("inputFileDrivers.txt", "r")

# open passDriversFile.txt with the intention of writing it
passDriversFile = open("passDriversFile.txt","w")

# open failDriversFile.txt with the intention of writing it
failDriversFile = open("failDriversFile.txt","w")

# loop through each line in inputFileDrivers.txt

for line in inputFileDrivers:
    line_split = line.split()
    if line_split[2] == "P":
        passDriversFile.write(line)
    else:
        failDriversFile.write(line)

# close inputFileDrivers.txt
inputFileDrivers.close()

# close passDriversFile.txt
passDriversFile.close()

# close failDriversFile.txt
failDriversFile.close()