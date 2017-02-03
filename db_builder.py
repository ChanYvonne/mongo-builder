from pymongo import MongoClient
from csv import DictReader

def setup():
	server = MongoClient('127.0.0.1')
	bonsai = server.bonsai
	students = bonsai.students
	peeps = DictReader(open("peeps.csv"))
	courses = DictReader(open("courses.csv"))
	print peeps
	print courses
	return [peeps,courses]

def main():
	arrs = setup()
	print arrs[0]
	print arrs[1]