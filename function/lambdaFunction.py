import pandas as pd
import json
import boto3
import csv
import io

s3Client = boto3.client('s3')

def lambda_handler(event,context):
    
    # Get Bucket and file name
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(bucket)
    print(key)
    
    # Get Object
    response = s3Client.get_object(Bucket=bucket, Key=key)
    
    teachers = ['cucinella', 'asaro']
    file_path = "/content/sample_data/preferenze.csv"  
    max_students_per_class = 20  
    
    # Run the algorithm
    students = generate_student_dictionary(response)
    

    # Remove companion preferences that are not in the list of students
    for student in students:
        if student['companion_preference'] not in [s['name'] for s in students]:
            student['companion_preference'] = ''
    
    # Assign classes
    class_assignments = assign_classes(students, teachers, max_students_per_class)
    
    # need to convert class_assignments to csv before

    modified_csv = class_assignments
    
    s3.put_object(Bucket=bucket, Key=key, Body=modified_csv) 

    # Generate donwload URL for edited CSV
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=3600  # link expiration
    )

    # Restituisci l'URL come risposta
    return {
        'statusCode': 200,
        'body': json.dumps({'download_url': url})
    }

def generate_student_dictionary(file_path):
    students = []
    
    data_response = response['Body'].read().decode('utf-8')
    data_response_file = StringIO(data_response)
    
    # Read the CSV file
    data = pd.read_csv(data_response_file, delimiter=',')
    
    for _, row in data.iterrows():
        # Ignore rows with missing or invalid values in 'professore' column
        if pd.notna(row['professore']):
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
    other_students = [student for student in students if len(student['teacher_preferences']) == 0 and student['companion_preference'] == '']

    # Assign students with single preference
    for student in single_preference_students:
        teacher = student['teacher_preferences'][0]
        class_num = 1 if len(class_assignments[teacher][1]) < max_students_per_class else 2
        class_assignments[teacher][class_num].append(student['name'])
        if student['companion_preference'] in companions and isinstance(companions[student['companion_preference']], list):
            companions[student['companion_preference']].remove(student['name'])

    # Assign students without preferences
    for student in other_students:
        teacher = min(teachers, key=lambda teacher: sum(len(class_assignments[teacher][i]) for i in [1, 2]))
        class_num = 1 if len(class_assignments[teacher][1]) < max_students_per_class else 2
        class_assignments[teacher][class_num].append(student['name'])

    # Assign remaining students without preferences or companions
    for teacher in teachers:
        for class_num in [1, 2]:
            while len(class_assignments[teacher][class_num]) < max_students_per_class and students:
                student = students.pop(0)
                class_assignments[teacher][class_num].append(student['name'])

    return class_assignments
