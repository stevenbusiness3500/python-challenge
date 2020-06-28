import os
import csv


csvpath = os.path.join('election_data.csv')


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



    candidate1 = "Khan"
    candidate2 = "Correy"
    candidate3 = "Li"
    candidate4 = "O'Tooley"


    initialvotes1 = 0
    initialvotes2 = 0
    initialvotes3 = 0
    initialvotes4 = 0


    for row in csvreader:
        if row[2] == candidate1:
            initialvotes1 = initialvotes1 + 1
        elif row[2] == candidate2:
            initialvotes2 = initialvotes2 + 1
        elif row[2] == candidate3:
            initialvotes3 = initialvotes3 + 1
        elif row[2] == candidate4:
            initialvotes4 = initialvotes4 + 1



    totalvotes = initialvotes1 + initialvotes2 + initialvotes3 + initialvotes4



    khanpercentage = round((initialvotes1 / totalvotes) * 100, 3)
    correypercentage = round((initialvotes2 / totalvotes) * 100, 3)
    lipercentage = round((initialvotes3 / totalvotes) * 100, 3)
    otooleypercentage = round((initialvotes4 / totalvotes) * 100, 3)


    print("Election Results:")
    print("Total Votes:" + str(totalvotes))
    print("Khan:" + str(khanpercentage) + '%' + ' ' + '(' + str(initialvotes1) + ')')
    print("Correy:" + str(correypercentage) + '%' + ' ' + '(' + str(initialvotes2) + ')')
    print("Li:" + str(lipercentage) + '%' + ' ' + '(' + str(initialvotes3) + ')')
    print("Otooley:" + str(otooleypercentage) + '%' + ' ' + '(' + str(initialvotes4) + ')')

    if initialvotes1 > initialvotes2 and initialvotes1 > initialvotes2 and initialvotes1 > initialvotes4:
        print("Winner: Khan")
    elif initialvotes2 > initialvotes1 and initialvotes2 > initialvotes3 and initialvotes2 > initialvotes4:
        print("Winner: Correy")
    elif initialvotes3 > initialvotes1 and initialvotes3 > initialvotes2 and initialvotes3 > initialvotes4:
        print("Winner: Li")
    elif initialvotes4 > initialvotes1 and initialvotes4 > initialvotes2 and initialvotes4 > initialvotes3:
        print("Winner: O'Tooley")

        output = open("output.txt", "w")

        line1 = "Election Results"
        line2 = "------------------"
      
        output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))


