lecturer_list = []
students_list = []
class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.course_progress = []
        self.grades = {}
        students_list.append(self)

    def add_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer, Lecturer) and course in self.course_progress and course in lecturer.course_list and grade_lecturer <=10:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade_lecturer]
            else:
                lecturer.grades_lecturer[course] = [grade_lecturer]
        else:
            return 'Ошибка'

    def average_grades(self):
        all_grades_stud = []
        if not self.grades.values():
            return f'У студента {self.name} нет оценок'
        else:
            for marks in self.grades.values():
                for mark in marks:
                    all_grades_stud.append(mark)
            return round(sum(all_grades_stud) / len(all_grades_stud), 1)

    def __gt__(self, other):
        if self.average_grades() == f'У студента {self.name} нет оценок' or other.average_grades() == f'У студента {self.name} нет оценок':
            return 'Невозможно сравнить'
        else:
            return self.average_grades() > other.average_grades()

    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашнее задание: {self.average_grades()}
        Курсы в процессе изучения: {self.course_progress}
        Завершенные курсы: {self.finished_courses}
        """

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course_list = []

    def __str__(self):
        return f"""
           Имя: {self.name}
           Фамилия: {self.surname}
           """

class Reviewer(Mentor):

    def rate_students(self, student, course, grade):
        if isinstance(student, Student) and course in self.course_list and course in student.course_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"{super().__str__()}"

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}
        lecturer_list.append(self)

    def average_grades_lec(self):
        all_grades_lec = []
        if not self.grades_lecturer.values():
            return f'У лектора {self.name} нет оценок'
        else:
            for marks in self.grades_lecturer.values():
                for mark in marks:
                    all_grades_lec.append(mark)
            return round(sum(all_grades_lec) / len(all_grades_lec), 1)

    def __gt__(self, other):
        if self.average_grades_lec() == f'У лектора {self.name} нет оценок' or other.average_grades_lec() == f'У лектора {self.name} нет оценок':
            return 'Невозможно сравнить'
        else:
            return self.average_grades_lec() > other.average_grades_lec()

    def __str__(self):
        return f"{super().__str__()}Средняя оценка за лекции: {self.average_grades_lec()}"

    def average_lecturer(self, course):
        if not course in self.course_list:
            return f'Лектор {self.name} не проводит лекции по курсу: {course}'
        else:
            return f'Cредняя оценка лектора {self.name} за курс {course}: {round(sum(self.grades_lecturer[course]) / len(self.grades_lecturer[course]), 1)}'


def average_course_lec(lecturer_list, course):
    grades_list_lec = []
    for lecturer in lecturer_list:
        if  course in lecturer.course_list:
            for mark in lecturer.grades_lecturer[course]:
                grades_list_lec.append(mark)
            print(f'Преподаватель {lecturer.name} ведет лекции по курсу: {course}')
        
        else:
            print(f'Преподаватель {lecturer.name} не ведет лекции по курсу: {course}')
    
    return f'Средняя оценка всех лекторов за лекции в рамках курса {course}: {round(sum(grades_list_lec) / len(grades_list_lec), 1)}'

def average_course_stud(students_list, course):
    grades_list_stud = []
    for student in students_list:
        if  course in student.course_progress:
            for mark in student.grades[course]:
                grades_list_stud.append(mark)
            print(f'Студент {student.name} изучает курс: {course}')
        else:
            print(f'Студент  {student.name} не изучает: {course}')
    
    return f'Средняя оценка всех студентов за лекции в рамках курса {course}: {round(sum(grades_list_stud) / len(grades_list_stud), 1)}'



student_1 = Student('Максим', 'Коткин', 'мужской')
student_1.add_course('git')
student_1.course_progress += ['python']

student_2 = Student('Анна', 'Воробьева', 'женский')
student_2.add_course('python')
student_2.course_progress += ['git']

reviewer_1 = Reviewer('Даниил', 'Крылов')
reviewer_1.course_list += ['python']

reviewer_2 = Reviewer('Елена','Иванова')
reviewer_2.course_list += ['git']

lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.course_list += ['python']

lecturer_2 = Lecturer('Алёна', 'Батицкая')
lecturer_2.course_list += ['git']

reviewer_1.rate_students(student_1,'python', 8)
reviewer_1.rate_students(student_1,'python', 10)
reviewer_2.rate_students(student_2,'git', 9)
reviewer_2.rate_students(student_2,'git', 7)

student_1.rate_lecturer(lecturer_1, 'python', 9)
student_1.rate_lecturer(lecturer_1, 'python', 10)
student_2.rate_lecturer(lecturer_2, 'git', 10)
student_2.rate_lecturer(lecturer_2, 'git', 8)

print(f'студент 1: {student_1}')
print(f'студент 2: {student_2}')

print(f'ревьюер 1: {reviewer_1}')
print(f'ревьюер 2: {reviewer_2}')

print(f'лектор 1: {lecturer_1}')
print(f'лектор 2: {lecturer_2}')

print(student_1 < student_2)
print(student_1 > student_2)
print(student_1 == student_2)
print(student_1 != student_2)

print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)

print(lecturer_1.average_grades_lec())
print(lecturer_2.average_grades_lec())
print(lecturer_1.average_lecturer('python'))
print(lecturer_1.average_lecturer('git'))
print(lecturer_2.average_lecturer('python'))
print(lecturer_2.average_lecturer('git'))

print(average_course_stud(students_list,'git'))
print(average_course_stud(students_list,'python'))
print(average_course_lec(lecturer_list,'git'))
print(average_course_lec(lecturer_list,'python'))