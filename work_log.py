import os
import sys

from tasks import AddNewEntry, SearchInExisting, SearchByExactDate
from tasks import SearchByRangeOfDates, SearchByExactSearch, SearchByRegexPattern


class WorkLog(AddNewEntry, SearchInExisting, SearchByExactDate,
	SearchByRangeOfDates, SearchByExactSearch, SearchByRegexPattern):

	def setup(self):
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
		os.system('clear')
		return self.to_do


	def choose_what_to_do(self, to_do):
		if self.to_do.upper() == "A":
			self.add_new_entry()
		elif self.to_do.upper() == "B":
			self.search_in_existing()
		elif self.to_do.upper() == "C":
			print("Thank you for using the Work Log program.")
			print("Come again soon.")
			sys.exit(0)
		else:
			print("Enter a,b or c!")
			self.choose_what_to_do(to_do)


foo = WorkLog()
foo.setup()
