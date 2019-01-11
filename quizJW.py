#Defining function

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
q2 ="""How many planets are in our solar system ?
1)15
2)10
3)8
4)7"""
q2Ans = int(0)
answered2 = False
q2r = 3

#q3 vaiables
q3 ="""What is the fastest water animal ?
1)Porpoise
2)Sailfish
3)Flying fish
4)Tuna"""
q3Ans = int(0)
answered3 = False
q3r = 2

#q4 vaiables
q4 ="""When was apple founded ? 
1)1969
2)1970
3)2000
4)1976"""
q4Ans = int(0)
answered4 = False
q4r = 4

#q5 vaiables
q5 ="""who invented the game of basketball ? 
1)Adam Sliver
2)William G. Morgan
3)James Naismith
4)Micheal Jordan"""
q5Ans = int(0)
answered5 = False
q5r = 3

#q6 vaiables
q6 ="""who created the periodic table ? 
1)Dmitri Mendeleev
2)John Newlands
3)Henry Moseley
4)J.J Thomson"""
q6Ans = int(0)
answered6 = False
q6r = 1

#q7 vaiables
q7 ="""which of the following country is the coldest in the world ? 
1)Canda
2)Antartica
3)Russia
4)Greenland"""
q7Ans = int(0)
answered7 = False
q7r = 2

#q8 vaiables
q8 ="""What is fornite worth ? 
1)$20 billion
2)$15 billion
3)$50 billion
4)$8 billion"""
q8Ans = int(0)
answered8 = False
q8r = 4

#q9 vaiables
q9 ="""How tall is Mount Everst ? 
1)20,150ft
2)24,400ft
3)20,029ft
4)25,900ft"""
q9Ans = int(0)
answered9 = False
q9r = 3
  
#q10 vaiables
q10 ="""When was aston martin (cars) founded ? 
1)1913
2)1989
3)1907
4)1932"""
q10Ans = int(0)
answered10 = False
q10r = 1 
  
  
  

#intro
print ("Hello and welcome to my ten question quiz")
print ("In this program, you will be asked one question and given fourm options.")
print ("To chose from.")
print ("When you are ready to answer the question, hit enter.")
#These are the intructions above.


# run questions 1-2
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
    print("You were close you should try again")
    
elif score == 7:
    print("You should try again that wasn't a bad score")

elif score == 6:
    print("You should try again becuase I knwo you can get a much better score")

elif score == 5:
    print("You didn't get a great score were you trying.")

elif score == 4:
    print("You failed but I beleive you can get a way better score")

elif score == 3:
    print("You should try again becuase you have the potiential to do better")

elif score == 2:
    print("This is not a great score, you can do much better") 

elif socre == 1:
    print("Were you trying")

elif socre == 0:
    print("You should go on google to look up the answers and study to get a better score")

else:
    print("Ok you have made a mistake please read the questions throughly.")

          


