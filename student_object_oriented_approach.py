class Student:
    def __init__(self, name, is_hosteler):
        self.name = name
        self.is_hosteler = is_hosteler

# Create student objects
class_roster = [
    Student("Alice", True),
    Student("Bob", False),
    Student("Charlie", True)
]

# Filter using object attributes
hostelers = [student.name for student in class_roster if student.is_hosteler]
print("Hostelers:", hostelers)
