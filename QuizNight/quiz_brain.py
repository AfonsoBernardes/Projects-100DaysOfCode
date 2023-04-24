class QuizBrain():
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.upper() == correct_answer.upper():
            self.score += 1
            print('You are right!')
        else:
            print('You are wrong!')

        print(f"Your current score is {self.score}/{self.question_number}.\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f"Q.{self.question_number}: {current_question.text} True or False? ")
            if user_answer.upper() == 'TRUE' or user_answer.upper() == 'FALSE':
                self.check_answer(user_answer, current_question.answer)
                break
            else:
                print('Invalid answer, try again.\n')
