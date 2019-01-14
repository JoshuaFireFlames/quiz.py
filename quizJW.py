#Importing data file

from quizJWdata import *

global score
score = 0 

def run_quest(quest, ansU, check, ansR):
    print(quest)
    while check == False:
        try:
            ansU = int(input("Choose the best reponse that seems fit." ))
            if ansU == ansR:
                print("Ok")
                global score 
                score += 1
                check = True
            elif 0 < ansU < 5:
                print("Ok")
                check = True
            else:
                print("Please enter a integer 1-4.") # unacceptable int response

        except ValueError:
            print("Please read answer choices.") # Non-integer response


#intro
print ("Hello and welcome to my ten question quiz")
print ("In this program, you will be asked one question and given fourm options.")
print ("To chose from.")
print ("When you are ready to answer the question, hit enter.")
#These are the intructions above.


# run questions 1-10
run_quest(q1, q1Ans, answered1, q1r)
run_quest(q2, q2Ans, answered2, q2r)
run_quest(q3, q3Ans, answered3, q3r)
run_quest(q4, q4Ans, answered4, q4r)
run_quest(q5, q5Ans, answered5, q5r)
run_quest(q6, q6Ans, answered6, q6r)
run_quest(q7, q7Ans, answered7, q7r)
run_quest(q8, q8Ans, answered8, q8r)
run_quest(q9, q9Ans, answered9, q9r)
run_quest(q10, q10Ans, answered10, q10r)

#Score
print("you got:", score * 10, "% on the quiz")
if score == 10:
    print("You did a great job.")
    
elif score == 9:
    print("You were so close from a perfect score.")
    
elif score == 8:
    print("You were close you should try again.")
    
elif score == 7:
    print("You should try again that wasn't a bad score.")

elif score == 6:
    print("You should try again becuase I knwo you can get a much better score.")

elif score == 5:
    print("You didn't get a great score were you trying.")

elif score == 4:
    print("You failed but I beleive you can get a way better score.")

elif score == 3:
    print("You should try again becuase you have the potiential to do better.")

elif score == 2:
    print("This is not a great score, you can do much better.") 

elif socre == 1:
    print("Were you trying")

elif socre == 0:
    print("You should go on google to look up the answers and study to get a better score.")

else:
    print("Ok you have made a mistake please read the questions throughly.")

          


