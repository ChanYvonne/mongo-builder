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
				bayle = {}
				bayle[course['code']] = course['mark']
				this['courses'].append(bayle)
		ret.append(this)
	return ret

def mongofy(info):
	server = MongoClient('127.0.0.1')
	bonsai = server.bonsai
	students = bonsai.students
	for student in info:
		students.insert_one(student)
	print "Checking that everything was sent accurately! Printing contents\n"
	for i in range(11):
		print bonsai.students.find_one({'id': i-1})

def check():
	print ""

def main():
	arrs = setup()
	tog = cong(arrs[0], arrs[1])
	serv = mongofy(tog)
	check()

main()