from random import randint
from question_model import *
from data import question_data

class QuizBrain:
    def __init__(self):
        self.questions_attempted = 0
        self.correct_ans_count = 0
        
        self.questions = []
        for qd in question_data:
            q = Question(text=qd["text"], answer=qd["answer"])
            self.questions.append(q)
    
    def next_question(self):
        return self.questions[randint(0, len(self.questions)-1)]

    def get_prompt(self, question):
        return (f"Q.{self.questions_attempted}: {question.text} (True/False)? : ")

    def right_or_wrong(self, question, guess):
        print(f"You got it {'right' if question.answer.lower() == str(guess).lower() else 'wrong'}!")
        return question.answer.lower() == str(guess).lower()
        
    def reveal_answer(self, question):
        print(f"The correct answer was: {question.answer}.")

    def print_score(self):
        print(f"Your current score is: {self.correct_ans_count}/{self.questions_attempted}.")
        
        
