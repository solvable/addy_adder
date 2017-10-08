import operator, re, usaddress, phonenumbers
from nameparser import HumanName
data = []
# TODO automate text file creation from PDF directory

# Find jobs completed from text file with pages separated by '@@@@@'

def completed():
    complete_clean = []
    ten_year_guarantee = []
    sliced = []


# TODO remove hardcoded filename
#    filename = raw_input("Filename with ABSOLUTE path? ")
    filename = '/home/evan/Desktop/cleaner.txt'
    with open(str(filename)) as openfile:
        data = openfile.read().split('@@@@@')
        # Sanity check
        #print(data[1])

    for i in data:
        if "JOB" in i:
            complete_clean.append(i)

    # Count and print number of total contracts in file
    print "Number of contracts " + str(len(data))

    # Count and print number of jobs complete
    # print complete_clean
    print "Number of jobs complete " + str(len(complete_clean))

    # Count and print number of jobs with 10 year guarantee
    for i in complete_clean:
        if "10 YEAR" in i:
            ten_year_guarantee.append(i)
    print "Number of 10 year " + str(len(ten_year_guarantee))

    # Slice the first 8 lines from each contract
    for i in ten_year_guarantee:
        x = i.splitlines()
        sliced.append(x[2:10])

    # Parse Name into Readable name
    for p in sliced:
        readable = HumanName(p[0])
        p[0] = readable

        #print(p[0])

    # Parse Address into US postal service mailable address
        # print(str(p[0])+ '\n' + p[2] +'\n'+ p[4] +'\n')

    

# Run that Shit!/
completed()
