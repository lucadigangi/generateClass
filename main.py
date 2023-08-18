import pandas as pd

def generate_student_dictionary(file_path):
    students = []
    
    # Read the CSV file
    data = pd.read_csv(file_path, delimiter=',')
    for _, row in data.iterrows():
        student = {
            'name': row['studente'],
            'teacher_preferences': [row['professore']],
            'companion_preference': row['compagno']
        }
        students.append(student)
    
    return students

def assign_classes(students, teachers, max_students_per_class):
    class_assignments = {teacher: {1: [], 2: []} for teacher in teachers}
    companions = {student['name']: student['companion_preference'] for student in students}
    
    single_preference_students = [student for student in students if len(student['teacher_preferences']) == 1]
    other_students = [student for student in students if len(student['teacher_preferences']) == 0]
    
    # Assign students with single preference
    for student in single_preference_students:
        teacher = student['teacher_preferences'][0]
        class_num = 1 if len(class_assignments[teacher][1]) < max_students_per_class else 2
        class_assignments[teacher][class_num].append(student['name'])
        companions[student['companion_preference']].remove(student['name'])
    
    # Assign other students
    for teacher in teachers:
        for class_num in [1, 2]:
            while len(class_assignments[teacher][class_num]) < max_students_per_class:
                if other_students:
                    student = other_students.pop(0)
                    class_assignments[teacher][class_num].append(student['name'])
    
    return class_assignments

#---- MAIN ----#

teachers = ['carla', 'marta']
file_path = "/content/sample_data/Cartel1.csv"  # Assicurati che il percorso sia corretto
max_students_per_class = 20  # Modifica questo valore se necessario

# Run the algorithm
students = generate_student_dictionary(file_path)
class_assignments = assign_classes(students, teachers, max_students_per_class)
print(class_assignments)
