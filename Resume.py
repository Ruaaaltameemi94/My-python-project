def calculate_average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def find_max_grade(grades):
    max_grade = max(grades)
    return max_grade

def find_my_classes(grades):
    my_classes = grades
    return my_classes

def print_my_resume(name, age, major, college):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major}")
    print(f"College: {college}")

class Graduate:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        for course in self.courses:
            print(f"Course: {course[0]}, Grade: {course[1]}")

# Example usage
if __name__ == "__main__":
    # Student information
    name = "Ruaa Altameemi"
    age = 29
    major = "Computer Engineering"
    college = "California State University Sacramento"

    # Grades
    grades = [85, 90, 92, 78, 88]

    # Calculate average grade
    average_grade = calculate_average_grade(grades)
    print(f"Average Grade: {average_grade}")

    # Find maximum grade
    max_grade = find_max_grade(grades)
    print(f"Maximum Grade: {max_grade}")
    my_classes = find_my_classes(grades)
    # Print student information
    print_my_resume(name, age, major, college)
    graduate = Graduate("Ruaa Altameemi")
    graduate.add_course(("Cmos And Vlsi", "B+"))
    graduate.add_course(("Signals and Systems", "B"))
    graduate.add_course(("Intro Circuit Analysis", "B+"))
    graduate.add_course(("Intro System Program Unix", "B"))
    graduate.add_course(("Intro to Environmental Science", "B"))
    graduate.add_course(("Logic Design", "A"))
    graduate.add_course(("Advanced Logic Design", "B+"))
    graduate.add_course(("Computer Hardware Design", "B"))
    graduate.add_course(("Signals and Systems", "A"))

    # Displaying courses
    graduate.display_courses()