import os
import time

def rules(candidates):
    print("There are 20 player listed....\nYou have (3)three votes\n1st vote consist 5 points\n2nd vote consist 3 points\n3rd vote consist 1 point....\n\n\n")

    # showing the vorter list to the voters
    
    for each in candidates:
        index1=each.find('@')
        index2=each.find("\n")
        print(" press         " +each[index1+1:index2] +"     vote him      "+each[:index1])
    print()
    print("---------------------------------------------------------------\n\n\n")

#cheaking validation of voters 
def valid_voter(name,voters):
    print("Hope you are aware fo voting rules.......")
    if name in voters:
        return True
    else : 
        return False



f= open("candidatae_list.txt",'r')
candidates=f.readlines()   
#print(candidates)
no_of_candidate=len(candidates)
# Candidate_List_show(candidates)




#storing voter ids in a list
f1=open("votersLlist.txt",'r')
voters=[]
for line in f1:
    voter=line[:-1]
    voters.append(voter)
# print(voters)

no_of_Voters= len(voters)
# print(no_of_Voters)



point=[] #the list where we store the numbers
for i in range(no_of_candidate):
    point.append(0)

# print(point)

# this is the actual voting system
while no_of_Voters:
    rules(candidates)
    name=input("Enter your name with id card number(as your voter card): ")
    if(valid_voter(name,voters)):
        print("     hey "+name[:-5]+" you can prosded to vote")
        while True:
            #first vote he can vote one  member from all candidate and give 5 points 
            try:
                first_vote=int(input("Ener your 1st vote:  "))
                
            except ValueError:
                print("takes integer only")
            
                continue
            if(first_vote>0 and first_vote<21):
                point[first_vote-1]+=5
                break
            else: 
                print("Match with no prefercnces....")
                continue
        while True:
            try:
                second_vote=int(input("Ener your 2nd vote:  ")) 
                
            except ValueError:
                print("takes integer only\n")
            
                continue
            
            if(second_vote>0 and second_vote<21 and second_vote!=first_vote):
                point[second_vote-1]+=3
                break
            else: 
                print("..may be your 2nd vote is similar with 1st vote.....\nOR match with no prefercnces....")
                continue

        while True:
            try:
                third_vote=int(input("Ener your 3rd vote:  "))
                
            except ValueError:
                print("takes integer only\n")
            
                continue
            if(third_vote>0 and third_vote<21 and third_vote!=first_vote and third_vote!=second_vote):
                point[third_vote-1]+=3
                break
            else:
                print("..may be your 3rd vote is similar with 2nd vote or 1st vote.....\nOR match with no prefercnces....") 
                continue
        no_of_Voters-=1
        voters.remove(name)
        print()
    else: 
        time.sleep(1)
        print("\n              Indalid credintial !! please try later.......")
        time.sleep(3)
    time.sleep(1)
    os.system('cls')
max_point=max(point)
index_of_max=point.index(max_point)
print("---------------------------------------------------------------")
#this steps is only for print names
winner=candidates[index_of_max]
find_char=winner.find("@")
winner=winner[:find_char]
print("\nthis year ballon d'or winner is : ", winner)