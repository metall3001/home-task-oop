class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# Создаем лекторов и закрепляем их за курсом
best_lecturer_1 = Lecturer('Один', 'Всеотец')
best_lecturer_1.courses_attached += ['Полет верхом на секире']

best_lecturer_2 = Lecturer('Гном', 'Эйтри')
best_lecturer_2.courses_attached += ['Владение жезлом']

# Создаем проверяющих и закрепляем их за курсом
cool_reviewer_1 = Reviewer('Вонг', 'Маг')
cool_reviewer_1.courses_attached += ['Полет верхом на секире'
cool_reviewer_1.courses_attached += ['Владение жезлом']

cool_reviewer_2 = Reviewer('Доктор', 'Стренж')
cool_reviewer_2.courses_attached += ['Полет верхом на секире']
cool_reviewer_2.courses_attached += ['Владение жезлом']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Тор', 'Одинсон')
student_1.courses_in_progress += ['Полет верхом на секире']
student_1.finished_courses += ['Магия Асгарда']

student_2 = Student('Локи', 'Йотонхеймский')
student_2.courses_in_progress += ['Владение жезлом']
student_2.finished_courses += ['Магия Асгарда']

# Выставляем оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Полет верхом на секире', 10)
student_1.rate_hw(best_lecturer_1, 'Полет верхом на секире', 10)
student_1.rate_hw(best_lecturer_1, 'Полет верхом на секире', 10)

student_1.rate_hw(best_lecturer_2, 'Полет верхом на секире', 5)
student_1.rate_hw(best_lecturer_2, 'Полет верхом на секире', 7)
student_1.rate_hw(best_lecturer_2, 'Полет верхом на секире', 8)

student_1.rate_hw(best_lecturer_1, 'Полет верхом на секире', 7)
student_1.rate_hw(best_lecturer_1, 'Полет верхом на секире', 8)
student_1.rate_hw(best_lecturer_1, 'Полет верхом на секире', 9)

student_2.rate_hw(best_lecturer_2, 'Владение жезлом', 10)
student_2.rate_hw(best_lecturer_2, 'Владение жезлом', 8)
student_2.rate_hw(best_lecturer_2, 'Владение жезлом', 9)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.rate_hw(student_1, 'Полет верхом на секире', 8)
cool_reviewer_1.rate_hw(student_1, 'Полет верхом на секире', 9)
cool_reviewer_1.rate_hw(student_1, 'Полет верхом на секире', 10)

cool_reviewer_2.rate_hw(student_2, 'Владение жезлом', 8)
cool_reviewer_2.rate_hw(student_2, 'Владение жезлом', 7)
cool_reviewer_2.rate_hw(student_2, 'Владение жезлом', 9)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n')
print()
print()

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Создаем список студентов
student_list = [student_1, student_2]

# Создаем список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Полет верхом на секире'}: {student_rating(student_list, 'Полет верхом на секире')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Полет верхом на секире'}: {lecturer_rating(lecturer_list, 'Полет верхом на секире')}")
print()