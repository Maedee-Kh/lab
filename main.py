
students = [
    {"Firstname": "Maede", "Lastname": "Khoshgoo", "SID": 1399012268050},
    {"Firstname": "Anahid", "Lastname": "Hakimi", "SID": 1401946875351},
    {"Firstname": "Sara", "Lastname": "Zarei", "SID": 14016345787512},
]

sorted_students = sorted(students, key=lambda x: (x['Firstname'], x['Lastname'], x['SID']))

for student in sorted_students:
    print(student)


students.append({"Firstname": "Ali", "Lastname": "Hosseini", "SID": 1400120653997})
students.append({"Firstname": "Nasim", "Lastname": "jafari", "SID": 1398645923278})

