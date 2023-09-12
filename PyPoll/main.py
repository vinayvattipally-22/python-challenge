import os
import csv



# Path to collect data from the Resources folder
CSV_PATH = os.path.join("Resources", "election_data.csv")

election_data = []


total_votes_cast = 0
# Opening a csvfile
with open(CSV_PATH) as file:
     reader = csv.reader(file)
     header = next(reader)
     election_data = list(reader)
     
     candidate_dict = {} 
     candidate_list = []
     
     total_votes = len(election_data)
     
     # Using a for loop to get candidate list
     for i in range (len(election_data)):
          candidate_dict[election_data[i][2]] = 0
          candidate_list = list(candidate_dict.keys())
         
     # Updating candidates votes in the candidate dictionary using a for loop
     for j in range (len(candidate_list)): 
          for i in range(len(election_data)):
               if(candidate_list[j] == election_data[i][2]):
                    candidate_dict[candidate_list[j]] = candidate_dict[candidate_list[j]] + 1

     # Displaying the output
     print("Total Votes: ", total_votes)
     for x,y in candidate_dict.items():
          print(f'{x}: {round((y/total_votes)*100,3)}% ({y})')

     winner = max(candidate_dict, key=candidate_dict.get)
     winner_votes = max(candidate_dict.values())
     print(f'Winner: {winner}')

# Declaring an output path
output_path = os.path.join("analysis", "Election_results.txt")
 # Creating an output file using "write" mode.
with open(output_path, "w") as f:
     print("\nElection Results\n", file = f)
     print("-----------------------------------------",file = f)
     print("\nTotal Votes: ", total_votes,"\n", file=f)
     print("-----------------------------------------",file = f)
     for x,y in candidate_dict.items():
          print(f'\n{x}: {round((y/total_votes)*100,3)}% ({y})\n',file=f)
     print("-----------------------------------------",file = f)
     print(f'\nWinner: {winner}\n',file=f) 
     print("-----------------------------------------",file = f)

