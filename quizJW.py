answered = False
q1Ans = int(0)
score = int (0)

print ("Hello and welcome to my one question quiz")
print ("In this program, you will be asked one question and given fourm options.")
print ("To chose from.")
print ("When you are ready to answer the question, hit enter.")
#These are the intructions above.

print("How many letters are in the alphabet.")
print ("1) 26")
print ("2) 6")
print ("3) 40")
print ("4) 22")

while answered == False: #This is the while loop to reread the questions
    try:
        q1Ans = int(input("Choose the best reponse that seems fit."))
        if q1Ans == 1:
            print("Ok.")
            answered = True
            score = score + 1 
        elif 0 < q1Ans < 5:
            print ("Ok.")
            answered = True
        else:
            print("Please enter a integer 1-4.") # unacceptable int response

    except ValueError:
        print("Please read answer choices.") # Non-integer response

#Score
print("you got:", score * 100, "% on the quiz")


