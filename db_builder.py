from pymongo import MongoClient
from csv import DictReader

def setup():
	server = MongoClient('127.0.0.1')
	bonsai = server.bonsai
	students = bonsai.students
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
	for thing in ret:
		print thing
		print ""
	return ret

def main():
	arrs = setup()
	tog = cong(arrs[0], arrs[1])

main()