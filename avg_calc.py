from pymongo import MongoClient

def get_info():
    server = MongoClient('127.0.0.1')
    bonsai = server.bonsai
    students = bonsai.students

    arr = []

    for person in students.find():
        sum = 0
        amt = 0
        for course in person['courses']:
                sum += int(course[1])
                amt += 1
        avg = sum/amt
        info = { 'name' : person['name'],
                 'id' : str(person['id']),
                 'average' : avg
                 }
        arr.append(info)

    for peep in arr:
        print "Student: " + peep['name']
        print "id: " + peep['id']
        print "average: " + str(peep['average'])
        print ""

get_info()
