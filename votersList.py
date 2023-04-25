# taking voters details
import random
import os
import time
data_of_voter=open("DataOfVoters.txt",'w')
def count_age(date_of_birth,age):
    return True
def form_fill_up(name):
    country=input("Enter your country: ")
    date_of_birth=input("Enter your date_of_birth: ")
    while True:
        try:
            age=int(input("Enter your age: "))
        except:
            print("Age is always be in integer from\n")
        else: 
            break
    id=input("Enter your id(passport/driving lisence/pan card): ")
    Email=input("Enter your Email: ")

    #collect this data for further use

    data_of_voter.write("name: "+name+"\n"+"country: "+country +"\n"+"date_of_birth: "+date_of_birth +"\n"+'age: '+str(age)+"\n" +"id: "+id+'\n'+"Email: "+Email+"\n")
    if(int(age)>=18 and count_age(date_of_birth,age)):
        return True
    else: 
        return False


def genarate_id(i):
    id=''
    a1=str(i+1)
    a0=str(random.randint(101,999))
    id=a1+a0
    # print(id)
    return id




while True: # asking conformation
    try:
        voters_numnber=int(input("Enter total number of voters:  "))
    except ValueError : 
        print("Please give an integer number ")
        continue
    ch1=input("do you want to continue? (yes(y)/no):  ")
    if(ch1== 'y' or ch1== "Y"):
        break
    else: 
        try:
            voters_numnber=int(input("Enter total number of voters:  "))
        except ValueError : 
            print("Please give an integer number ")
            continue
voter_list=open("VotersLlist.txt",'w')   

for i in range(voters_numnber):
    name=input("Enter name: ")
    eligibility=form_fill_up(name)
    time.sleep(3) 
    if(eligibility):
        voter_id=genarate_id(i)
        voter_list.write(name+"@"+voter_id+"\n")
        print("\nyour voter id  is : "+name+"@"+voter_id)
        data_of_voter.write(name+"@"+voter_id+"\n"+"-------------------------\n")
        time.sleep(3)
    else: 
        print("sorry you are not eligible for giving vote(as your age<18)")
        time.sleep(3)
    os.system('cls')
voter_list.close()
data_of_voter.close()