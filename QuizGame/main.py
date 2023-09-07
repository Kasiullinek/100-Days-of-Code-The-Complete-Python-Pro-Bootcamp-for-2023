from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
index = 0

for data in question_data:
    data = question_data[index]
    question_bank.append(Question(question_data[index]["question"], question_data[index]["correct_answer"]))
    index += 1

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")