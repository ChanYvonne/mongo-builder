from pymongo import MongoClient
from csv import DictReader

def setup():
	ps = DictReader(open("peeps.csv"))
	courses = open("courses.csv")
	return [ps, courses]

def cong(peeps, crses):
	ret = []

	for peep in peeps:
                #add info from peeps.csv
		this = {'name': peep['name'],
			'age': peep['age'],
			'id': peep['id'],
			'courses': []
		}
		crses.seek(0) #look at crses from the beginning
		courses = DictReader(crses)
		for course in courses:
			if course['id'] == peep['id']: #if course belongs to this student
                                #then add it to their courses
				this['courses'].append([course['code'], course['mark']])
		ret.append(this)
	return ret

def mongofy(info):
        #mongo setup
	server = MongoClient('127.0.0.1') #for testing locally
        #server = MongoClient('149.89.150.100') 
	bonsai = server.bonsai
	students = bonsai.students
        
        if students.count() > 0: #collection already has stuff
                print "Db already exists. Clearing it and trying again..."
                server.drop_database("bonsai")
                mongofy(info)
                return #returning nothing prevents it from crashing after checking for duplicates
                
        #insert each student as a doc to collection
	for student in info:
		students.insert_one(student)
                print "student added!"
                
        #check things were added correctly
	print "Checking that everything was sent accurately! Printing contents\n"
	for doc in students.find(): #.find() returns all contents
                print "Student: " + doc['name']
                print "id: " + str(doc['id'])
                print "age: " + str(doc['age'])
                print "course grades:"
                for course in doc['courses']:
                        print course[0] + "grade: " + str(course[1])
                print ""

def main():
	arrs = setup() #get csvs of info
	tog = cong(arrs[0], arrs[1]) #congregate the data from the two csvs
        mongofy(tog) #add this data to mongo database

main()
