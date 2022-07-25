from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main() -> None:
    question_bank: list = [Question(question["question"], question["correct_answer"]) for question in question_data]
    qb: QuizBrain = QuizBrain(question_bank)
    while qb.still_has_questions():
        qb.next_question()
    print(f"You've completed the quiz!\nYour final score is {qb.score}/{qb.question_number}.")


main()
