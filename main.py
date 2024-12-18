students = [
{"Firstname": "Maede", "Lastname": "Khoshgoo", "SID": 1399012268050},
{"Firstname": "Anahid", "Lastname": "Hakimi", "SID": 1401354589856},
{"Firstname": "Sara", "Lastname": "Zarei", "SID": 1401679815464},
]

sorted_students = sorted(students, key=lambda x: (x['Firstname'], x['Lastname'], x['SID']))

                                                  for student in sorted_students:
                                                                   print(student)
