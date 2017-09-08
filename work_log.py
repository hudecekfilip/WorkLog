import csv
import os
import sys

from tasks import AddNewEntry, SearchInExisting, SearchByExactDate
from tasks import SearchByRangeOfDates, SearchByExactSearch, SearchByRegexPattern


class WorkLog(AddNewEntry, SearchInExisting, SearchByExactDate,
	SearchByRangeOfDates, SearchByExactSearch, SearchByRegexPattern):

	def __init__(self):
		self.does_csv_file_exist()
		while True:
			self.to_do = self.what_to_do()
			self.choose_what_to_do(self.to_do)


	def what_to_do(self):
		print("WORK LOG")
		print("What would you like to do?:")
		print("a) Add new entry")
		print("b) Search in existing entries")
		print("c) Quit program")
		self.to_do = input("> ")
		self.clear_screen()
		return self.to_do


	def choose_what_to_do(self, to_do):
		if self.to_do.upper() == "A":
			self.add_new_entry()
		elif self.to_do.upper() == "B":
			self.search_in_existing()
		elif self.to_do.upper() == "C":
			print("Thank you for using the Work Log program.")
			print("Come again soon.")
			self.add_entries_to_csv()
			sys.exit(0)
		else:
			print("Enter a,b or c!")
			self.what_to_do()


	def does_csv_file_exist(self):
		if not os.path.exists("entries.csv"):
			with open('entries.csv', 'w') as csvfile:
				fieldnames = ['date', 'title', 'time', 'note']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
		else:
			with open('entries.csv', 'r') as f:
				reader = csv.reader(f)
				self.entries = list(reader)
				self.entries.pop(0)


	def add_entries_to_csv(self):
		count = 0
		with open('entries.csv','a',newline='') as csvfile:
			fieldnames = ['date', 'title', 'time', 'note']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			while count < len(self.entries):
				writer.writerow({'date': self.entries[count][0], 'title': self.entries[count][1], 'time': self.entries[count][2], 'note': self.entries[count][3]})
				count += 1




if __name__ == '__main__':
	foo = WorkLog()
