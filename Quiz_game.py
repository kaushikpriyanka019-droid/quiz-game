score = 0

q1 = input("What is the capital of France? ")

if q1.lower() == "paris":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

q2 = input("Which planet is called the Red Planet? ")

if q2.lower() == "mars":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

q3 = input("How many days are there in a week? ")

if q3 == "7":
    print("Correct")
    score = score + 1
else:
    print("Wrong")

print("Your score is", score)