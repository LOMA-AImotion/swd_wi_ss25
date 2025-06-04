class StudyCourse:
    def __init__(self):
        self.__students = []

    def add_student(self, mat_nr: str):
        self.__students.append(mat_nr)

    def is_immatriculated(self, mat_nr: str):
        return mat_nr in self.__students

if __name__ == "__main__":
    swd = StudyCourse() 
    swd.add_student("swr087")
    swd.add_student("maz162")
    swd.__students.insert(0, "swr007")
    print(swd.is_immatriculated("swr087"))
    print(swd.is_immatriculated("swr007"))
    print(swd.__students)