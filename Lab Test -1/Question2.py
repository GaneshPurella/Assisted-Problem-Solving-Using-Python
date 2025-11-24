student_marks = {
    "Alice": 75,
    "Bob": 62,
    "Charlie": 95,
    "Diana": 88,
    "Eve": 42
}

mean = sum(student_marks.values()) / len(student_marks)
above_mean_students = [student for student, mark in student_marks.items() if mark > mean]
print("Mean:", mean)
print("Students above mean:", above_mean_students)
