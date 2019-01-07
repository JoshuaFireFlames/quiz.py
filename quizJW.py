score = int (0)
answered1 = False
answered2 = False



#q1
q1 ="""How many letters are in the alphabet ?
1)26
2)6
3)40
4)22"""
q1Ans = int(0)
answered = False


#q2
q2 ="""How many planets are in our solar system
1)15
2)10
3)8
4)7"""
q2Ans = int(0)
answered = False


#intro
print ("Hello and welcome to my one question quiz")
print ("In this program, you will be asked one question and given fourm options.")
print ("To chose from.")
print ("When you are ready to answer the question, hit enter.")
#These are the intructions above.


#test question1
print(q1)

while answered1 == False: #This is the while loop to reread the questions
    try:
        q1Ans = int(input("Choose the best reponse that seems fit."))
        if q1Ans == 1:
            print("Ok.")
            answered1 = True
            score = score + 1 
        elif 0 < q1Ans < 5:
            print ("Ok.")
            answered1 = True
        else:
            print("Please enter a integer 1-4.") # unacceptable int response

    except ValueError:
        print("Please read answer choices.") # Non-integer response


#test question2
print(q2)

while answered2 == False: #This is the while loop to reread the questions
    try:
        q2Ans = int(input("Choose the best reponse that seems fit."))
        if q2Ans == 3:
            print("Ok.")
            answered2 = True
            score = score + 1 
        elif 0 < q2Ans < 5:
            print ("Ok.")
            answered2 = True
        else:
            print("Please enter a integer 1-4.") # unacceptable int response

    except ValueError:
        print("Please read answer choices.") # Non-integer response

#Score
print("you got:", score * 50, "% on the quiz")


