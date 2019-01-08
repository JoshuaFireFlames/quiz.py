#Defining function

def run_quest(quest, ansU, check, ansR):
    print(quest)
    while check == False:
        try:
            ansU = int(input("Choose the best reponse that seems fit." ))
            if ansU == ansR:
                print("Ok")
                #grade += 1
                check = True
            elif 0 < ansU < 5:
                print("Ok")
                check - True
            else:
                print("Please enter a integer 1-4.") # unacceptable int response

        except ValueError:
            print("Please read answer choices.") # Non-integer response




score = int (0)



#q1 variables
q1 ="""How many letters are in the alphabet ?
1)26
2)6
3)40
4)22"""
q1Ans = int(0)
answered1 = False
q1r = 1


#q2 vaiables
q2 ="""How many planets are in our solar system
1)15
2)10
3)8
4)7"""
q2Ans = int(0)
answered2 = False
q2r = 3


#intro
print ("Hello and welcome to my ten question quiz")
print ("In this program, you will be asked one question and given fourm options.")
print ("To chose from.")
print ("When you are ready to answer the question, hit enter.")
#These are the intructions above.


# run questions 1-2
run_quest(q1, q1Ans, answered1, q1r)
run_quest(q2, q2Ans, answered2, q2r)

#Score
print("you got:", score * 50, "% on the quiz")


