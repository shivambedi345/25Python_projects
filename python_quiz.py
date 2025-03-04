questions = ("how many elements are in the periodic table?",
             "which is the most abundant gas in earth's atmosphere?",
             "which animal lays the largest eggs?",
             "how many bones are there in the human body?",
             "which planet in the solar system is the hotest?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Nitrogen", "B. Hydrogen", "C. Helium", "D. Carbon-dioxide"),
           ("A. crocodile", "B. elephant", "C. ostrich", "D. hen"),
           ("A. 306", "B. 308", "C. 208", "D. 319"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "B", "A", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("------------------")
print("      result      ")
print("------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses;", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is : {score}%")
