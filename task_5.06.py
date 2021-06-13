pupils = [
    {
     'firstname': 'Masha',
     'Group': 42,
     'physics': 7,
     'informatics': 6,
     'history': 8,
    },
    {
     'firstname': 'Pasha',
     'Group': 42,
     'physics': 3,
     'informatics': 3,
     'history': 4,
    },
    {
     'firstname': 'Sasha',
     'Group': 41,
     'physics': 6,
     'informatics': 5,
     'history': 8,
    },
    {
     'firstname': 'Dasha',
     'Group': 41,
     'physics': 4,
     'informatics': 3,
     'history': 5,
    },
]
number = 0
pupil = ""
average_grade = ""
while number < len(pupils):
    pupil = pupils[number]
    average_grade = (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3
    if average_grade > 4:
        print(pupil)
    number += 1
