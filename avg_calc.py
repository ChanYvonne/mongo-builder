from pymongo import MongoClient
from csv import DictReader

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

def teachers():
    #check
    server = MongoClient('127.0.0.1')
    tch = server.bonsai.teachers
    if tch.count() > 0:
        print "Teachers col already populated.. clearing for retry"
        tch.delete_many({})
    
    ts = DictReader(open("teachers.csv"))
    #return ts
    techrs = []

    #setup to add student id's
    for person in ts:
        this = {
            'name': person['teacher'],
            'class': person['code'],
            'period': person['period'],
            'students': []
        }
        techrs.append(this)

    peeps = server.bonsai.students.find()
    for peep in peeps: #iterate students
        for course in peep['courses']: #iterate each students courses
            for teacher in techrs: #iterate thru teachers
                if teacher['class'] == course[0]: #if same course
                    teacher['students'].append(peep['_id']) #add students
    for person in techrs: #add results
        tch.insert_one(person)
    for info in tch.find():
        print info
    
get_info()
teachers()
