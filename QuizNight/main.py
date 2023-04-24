from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Add questions to list of Question()
question_bank = []
for question_dict in question_data:
    question_bank.append(Question(text=question_dict['text'], answer=question_dict['answer']))


quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}.")
