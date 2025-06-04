from answer_alternative import Answer

class Question:
    def __init__(self, question, alternatives, correct_index):
        self.question = question
        self.alternatives = alternatives
        self.correct_index = correct_index

    def is_correct(self, given_index: int):
        return self.correct_index == given_index
    
    def answer_is_correct(self, given_answer: str):
        correct_answer: Answer = self.alternatives[self.correct_index]
        return correct_answer.answer == given_answer

if __name__ == "__main__":
    q1 = Question("Was ist 2+2?", [ Answer("1", False), Answer("2", False),
                                   Answer("3", False), Answer("4", True)],
                                   3)
    print(q1.alternatives)
    print(q1.is_correct(0)) # denke an is_correct(q1, 0)
    print(q1.answer_is_correct("4"))
    