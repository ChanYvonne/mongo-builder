from pymongo import MongoClient

def setup():
	server = MongoClient('127.0.0.1')
	bonsei = server.bonsei
	students = bonsei.students

def main():
	setup()