from data import question_data
from question_model import koschan
from quiz_brain import QuizBrain

koschan_bank = []
for q in question_data:
    qtext = q["text"]
    qans = q["answer"]
    new_koschan = koschan(qtext, qans)
    koschan_bank.append(new_koschan)

# print(koschan_bank[0].txt)

# QuizBrain(koschan_bank).next_question() 
# exit code not possible this way as program terminates once questions are completed
# so we need a while loop to check if all are done

quiz = QuizBrain(koschan_bank)
while quiz.still_has_koschan():
    quiz.next_question()