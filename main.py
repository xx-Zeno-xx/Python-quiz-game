from question_model import Question
from data import  question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    q_text = question["question"]
    q_ans = question["correct_answer"]
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)
# print(question_bank[0].text)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("\nYou've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")