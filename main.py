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

def assign_classes(students, teachers):
    class_assignments = {teacher: {1: [], 2: []} for teacher in teachers}
    companions = {student['name']: student['companion_preference'] for student in students}
    
    for student in students:
        teacher_preferences = student['teacher_preferences']
        
        for teacher in teacher_preferences:
            for class_num in [1, 2]:
                if len(class_assignments[teacher][class_num]) < 3:
                    class_assignments[teacher][class_num].append(student['name'])
                    if student['companion_preference'] in companions and student['name'] in companions[student['companion_preference']]:
                        companions[student['companion_preference']].remove(student['name'])
                    break
    
    return class_assignments

#---- MAIN ----#

teachers = ['carla', 'marta']
file_path = "/content/sample_data/Cartel1.csv"  # Assicurati che il percorso sia corretto

# Run the algorithm
students = generate_student_dictionary(file_path)
class_assignments = assign_classes(students, teachers)
print(class_assignments)
