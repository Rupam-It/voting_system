#we will create a file to store candidate name
# while True:
#     try:
#         candidate_number=int(input("Enter no of candidate:  "))
#     except ValueError : 
#         print("Please give an integer number ")
#     else:
#          break




f=open("candidatae_list.txt",'w')


while True: # asking conformation
    try:
        candidate_number=int(input("Enter total number of candidate:  "))
    except ValueError : 
        print("Please give an integer number ")
        continue
    ch1=input("do you want to continue? (yes(y)/no):  ")
    if(ch1== 'y' or ch1== "Y"):
        break
    else: 
        try:
            candidate_number=int(input("Enter no of candidate:  "))
        except ValueError : 
            print("Please give an integer number ")
            continue
# taking inpput of candidate names
for i in range(candidate_number):
    name=input("Candidate Nmae: ")
    f.write(name + "@" +str(i+1)+"\n")
f.close()

print("----------------------------------------------------------------")
