from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, JOIN
import random

# Налаштування бази даних SQLite
db = SqliteDatabase('students_management.db')

# Базова модель
class BaseModel(Model):
    class Meta:
        database = db

# 1. Таблиця для Студентів
class Student(BaseModel):
    name = CharField()

# 2. Таблиця для Курсів
class Course(BaseModel):
    title = CharField()

# 3. Проміжна таблиця для зв'язку студентів та курсів
class StudentCourse(BaseModel):
    student = ForeignKeyField(Student, backref='courses')
    course = ForeignKeyField(Course, backref='students')

# Підключаємося та створюємо таблиці
db.connect()
db.create_tables([Student, Course, StudentCourse])

# --- ОПЕРАЦІЇ З ДАНИМИ ЗА ЗАВДАННЯМ ---

# 1. Додавання нового студента та запис його на курс
def add_new_student(student_name, course_title):
    # Шукаємо курс за назвою або створюємо, якщо його немає
    course, _ = Course.get_or_create(title=course_title)
    # Створюємо студента
    new_student = Student.create(name=student_name)
    # Записуємо на курс
    StudentCourse.create(student=new_student, course=course)
    print(f"\n[Додано] Студент {student_name} успішно зареєстрований на курс '{course_title}'!")

# 2. Запит: Студенти на певному курсі
def get_students_by_course(course_title):
    print(f"\n[Запит] Студенти, які навчаються на курсі '{course_title}':")
    query = (Student
             .select()
             .join(StudentCourse)
             .join(Course)
             .where(Course.title == course_title))
    for student in query:
        print(f"- {student.name}")

# 3. Оновлення імені студента або назви курсу
def update_student_name(old_name, new_name):
    updated = Student.update(name=new_name).where(Student.name == old_name).execute()
    if updated:
        print(f"\n[Оновлено] Ім'я студента змінено з '{old_name}' на '{new_name}'")

# 4. Видалення студента з бази даних
def delete_student_by_name(student_name):
    # Спочатку видаляємо зв'язки з курсами, щоб не порушувати цілісність
    student = Student.get_or_none(Student.name == student_name)
    if student:
        StudentCourse.delete().where(StudentCourse.student == student).execute()
        student.delete_instance()
        print(f"\n[Видалено] Студент {student_name} повністю видалений з бази.")


# --- ВИКОНАННЯ ОПЕРАЦІЙ ---

# Перевіримо додавання
add_new_student("Владислав", "Python Basic")

# Перевіримо запит студентів на курсі
get_students_by_course("Python Basic")

# Перевіримо оновлення даних
update_student_name("Владислав", "Владислав (Успішний)")

# Перевіримо видалення (для тесту видалимо когось із початкових, наприклад, "Іван")
delete_student_by_name("Іван")