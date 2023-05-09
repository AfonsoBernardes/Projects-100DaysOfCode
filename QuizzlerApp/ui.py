from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.question_number = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.geometry("+500-100")  # places the window at (x=500, y=-100) on the screen

        # Create 'score' label.
        self.score_label = Label(text="Score: 0/0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="WELCOME TO THE QUIZ!",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create buttons.
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, width=100, height=100,
                                  highlightthickness=0, bg=THEME_COLOR,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, width=100, height=100,
                                   highlightthickness=0, bg=THEME_COLOR,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quest_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quest_text)
        else:
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
