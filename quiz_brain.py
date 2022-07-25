from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list) -> None:
        self.question_number: int = 0
        self.question_list: list = question_list
        self.score: int = 0

    def check_answer(self, guess: str, ans: str) -> bool:
        if guess == ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Your current score is {self.score}/{self.question_number+1}\n")

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        current_question: Question = self.question_list[self.question_number]
        guess: str = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(guess, current_question.answer)
        self.question_number += 1

