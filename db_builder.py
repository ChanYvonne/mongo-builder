from pymongo import MongoClient
from csv import DictReader

def setup():
	ps = DictReader(open("peeps.csv"))
	courses = open("courses.csv")
	return [ps, courses]

def cong(peeps, crses):
	ret = []
	for peep in peeps:
		this = {'name': peep['name'],
				'age': peep['age'],
				'id': peep['id'],
				'courses': []
		}
		crses.seek(0)
		courses = DictReader(crses)
		for course in courses:
			if course['id'] == peep['id']:
				this['courses'].append([course['code'], course['mark']])
		ret.append(this)
	return ret

def mongofy(info):
	server = MongoClient('127.0.0.1')
	bonsai = server.bonsai
	students = bonsai.students
        if students.count() > 0:
                print "Db already exists. Clearing it and trying again..."
                server.drop_database("bonsai")
                mongofy(info)
                return
	for student in info:
		students.insert_one(student)
	print "Checking that everything was sent accurately! Printing contents\n"
	for doc in students.find():
                print "Student: " + doc['name']
                print "id: " + str(doc['id'])
                print "age: " + str(doc['age'])
                print "course grades:"
                for course in doc['courses']:
                        print course[0] + "grade: " + str(course[1])
                print ""

def main():
	arrs = setup()
	tog = cong(arrs[0], arrs[1])
	serv = mongofy(tog)

main()
