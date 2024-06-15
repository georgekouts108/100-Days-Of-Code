THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class Screen:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,  # this will ensure word-wrapping
            text='question text here',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.check_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.check_img, command=self.choose_true)
        self.true_button.grid(row=2, column=0)

        self.x_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.x_img, command=self.choose_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def choose_true(self):
        old_score = self.score
        self.score = self.quiz.check_answer(user_answer='True')
        self.give_feedback(is_right=(old_score != self.score))

    def choose_false(self):
        old_score = self.score
        self.score = self.quiz.check_answer(user_answer='False')
        self.give_feedback(is_right=(old_score != self.score))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.score_label.config(text=f'Score: {self.score}')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Final score:\n{self.score} / {len(self.quiz.question_list)}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        self.canvas.config(bg='white')
