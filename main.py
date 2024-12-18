
students = [
    {"Firstname": "Maede", "Lastname": "Khoshgoo", "SID": 123},
    {"Firstname": "Anahid", "Lastname": "Hakimi", "SID": 456},
    {"Firstname": "Sara", "Lastname": "Zarei", "SID": 789},
]

sorted_students = sorted(students, key=lambda x: (x['Firstname'], x['Lastname'], x['SID']))

for student in sorted_students:
    print(student)

