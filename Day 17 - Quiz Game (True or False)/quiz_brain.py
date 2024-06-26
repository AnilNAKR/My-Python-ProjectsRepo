class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/ False): ").lower()
        self.check_input(user_answer, current_question.answer)

    def check_input(self, u_answer, c_answer):
        if u_answer == c_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {c_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

