from quiz_brain import *

qb = QuizBrain()

while True:
    question = qb.next_question()
    qb.questions_attempted += 1
    guess = input(qb.get_prompt(question))
    result = qb.right_or_wrong(question, guess)
    qb.correct_ans_count += 1 if (result) else 0
    qb.reveal_answer(question)
    qb.print_score()
    print("\n\n")
    
    
    





