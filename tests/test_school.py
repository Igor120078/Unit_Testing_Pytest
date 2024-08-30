import pytest
from source.school import Classroom, Student, Teacher, TooManyStudents


@pytest.fixture
def empty_classroom():
    teacher = Teacher("Severus Snape")
    course_title = "Potions"
    return Classroom(teacher, [], course_title)


@pytest.fixture
def classroom_with_students():
    teacher = Teacher("Minerva McGonagall")
    course_title = "Transfiguration"
    students = [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]
    return Classroom(teacher, students, course_title)


def test_add_student(empty_classroom):
    student = Student("Neville Longbottom")
    empty_classroom.add_student(student)
    assert len(empty_classroom.students) == 1
    assert empty_classroom.students[0].name == "Neville Longbottom"


def test_add_student_raises_exception(empty_classroom):
    for _ in range(10):
        empty_classroom.add_student(Student("Some Student"))
    with pytest.raises(TooManyStudents):
        empty_classroom.add_student(Student("Another Student"))


def test_remove_student_by_name(classroom_with_students):
    classroom_with_students.remove_student_by_name("Harry Potter")
    assert len(classroom_with_students.students) == 2
    assert "Harry Potter" not in [student.name for student in classroom_with_students.students]


def test_change_teacher(classroom_with_students):
    new_teacher = Teacher("Filius Flitwick")
    classroom_with_students.change_teacher(new_teacher)
    assert classroom_with_students.teacher.name == "Filius Flitwick"
