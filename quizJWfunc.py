# Score
global score
score = 0

#Custom functions 
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
