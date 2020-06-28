import os
import csv

poll_csv = os.path.join('election_data.csv')

def get_results(data):

    totalVotescount = 0
    votes = []
    candidateCount = []
    uniqueCandidates = []
    percent = []

    for row in data:

        totalVotescount += 1
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])

            votes.append(row[2])

            for candidate in uniqueCandidates:
                candidateCount.append(votes.count(candidate))
                percent.append(round(votes.count(candidate)/totalVotescount*100,3))

                winner = uniqueCandidates[candidateCount.index(max(candidateCount))]

                print('Election Results')
                print('----------------------')
                print(f'Total Votes: {totalVotescount}')
                print('------------------')
                for i in range(len(uniqueCandidates)):
                    print(f'{uniqueCandidates[i]}: {percent[i]}% {candidateCount[i]}')
                    print('----------------------')
                    print(f'Winner: {winner}')
                    print('-------------------')

                    poll_output = os.path.join("PyPollResults.Txt")

                    with open(poll_output, "w") as txtfile:
                        txtfile.write('Election Results')
                        txtfile.write('\n------------------------')
                        txtfile.write(f'\nTotal Votes: {totalVotescount}')
                        txtfile.write('\n-----------------------')
                        for i in range (len(uniqueCandidates)):
                            txtfile.write(f'\n{uniqueCandidates[i]}: {percent[i]}%{candidateCount[i]}')
                            txtfile.write(f'\n----------------------')
                            txtfile.write(f'\nWinner: {winner}')
                            txtfile.write('\n--------------------------')

                            with open(poll_csv,newline='') as csvfile:
                                csvreader = csv.reader(csvfile,delimiter=',')

                                csv_header = next(csvfile)

                                get_results(csvreader)



