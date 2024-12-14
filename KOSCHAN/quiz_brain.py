class QuizBrain:
    def __init__(self, question_list):
        self.qno = 0
        self.qlist = question_list
        self.score = 0

    def still_has_koschan(self):
        return self.qno < len(self.qlist)-1

    def next_question(self):
        for q in self.qlist:
            ans = input(f"Q.{self.qno+1}) {self.qlist[self.qno].txt} (True/False?) (+4/-1)\n")
            self.check_answer(ans)
            print(f"{self.score}")
            
            self.qno +=1
        print(f"Score:- {self.score}/{len(self.qlist)*4}")

    def check_answer(self, ans):
        if ans.lower() == self.qlist[self.qno].ans.lower():
            print("Correct")
            self.score +=4
        else:
            print("Incorrect")
            self.score -=1