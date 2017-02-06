from pymongo import MongoClient
from csv import DictReader

def setup():
	ps = DictReader(open("peeps.csv"))
	courses = open("courses.csv")
	return [ps, courses]

def get_avg():
    server = MongoClient('127.0.0.1')
    bonsai = server.bonsai
    students = bonsai.students

    arr = []

    for person in students.find():
        info = { 'name' : person['name']
                 'id' : str(person['id'])
                 }
        
        arr.append(

def main():
    info = setup()

main()
