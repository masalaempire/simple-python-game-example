questions = ()
options = ((), (), (), (), (), ())
answers = ()
guesses = []
score = 0
question_num = 0
print ("Welcome to LMLD quiz!")
questions = (
    "Where does most of the digestive process take place?: ",
    "what organ makes bile?: ", 
    "Why do we eat food?: ",
    "what is the small intestine responsible for?: ",
    "The process by which the body breaks down food so that it can be used for energy?: ",
    "A substance such as fat, a protein, or a carbonhydrate that a living thing needs to survive?: "
)
options = (("A. Small intestine", "B. Stomach", "C. Mouth", "D. All the above"),
           ("A. Gallbladder", "B.Pancreas", "C. Appendix", "D.liver"),
           ("A. To keep our stomachs full", "B.To put oxygen into the body cells", "C.To make waste products", "D. To get nuitrients and energy"),
           ("A. Breaking down food", "B. Adding food", "C.chewing", "D.Takes in more enzymes and starts absorbtion"),
           ("A.composition", "B.Absorbtion", "C.Digestion", "D.composition"),
           ("A.Saliva", "B.nutrients", "C.carrots", "D.minerals"))
answers = ("A", "A", "D", "D", "C", "B")
guesses = []
score = 0
question_num = 0
for question in questions:
  print("---------------------")
  print(question)
  for option in options [question_num]:
    print(option)

  guess = input("Enter (A,B,C,D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("CORRECT!!!!!!")
  else:
    print("Nope")
    print(f"{answers[question_num]} is the correct answer")
  question_num += 1

print("---------------------------")
print("          Results          ")
print("---------------------------")

print("answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
  print(guess, end=" ")
print()
score = int (score / len(questions) * 100)
print (f"Your score is: {score}%")
