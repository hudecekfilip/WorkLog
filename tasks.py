import datetime
import os
import re
import sys


class AddNewEntry:
    entries = []
    master_count = 0


    def add_new_entry(self):
        self.task_date = self.date_of_the_task()
        self.task_title = self.title_of_the_task()
        self.task_time = self.time_spent()
        self.task_note = self.note()
        self.entries.append(
            (self.task_date, self.task_title,
            self.task_time, self.task_note)
            )
        input("You entry has been added. Press enter to return to the menu")


    def date_of_the_task(self):
        print("Date of the task")
        print("Please use DD/MM/YYYY format:")
        self.task_date = input("> ")
        try:
            datetime.datetime.strptime(self.task_date, '%d/%m/%Y')
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY!")
            input("Press enter to continue")
            self.date_of_the_task()
        os.system('clear')
        return self.task_date


    def title_of_the_task(self):
        print("Title of the task")
        self.task_title = input("> ")
        if not self.task_title:
            print("You have to enter the title of the task!")
            input("Press enter to continue")
            self.title_of_the_task()
        os.system('clear')
        return self.task_title


    def time_spent(self):
        print("Time spent (rounded minutes)")
        self.task_time = input("> ")
        try:
            self.task_time = int(self.task_time)
        except ValueError:
            print("You have to enter the time spent!")
            input("Press enter to continue")
            self.time_spent()
        os.system('clear')
        return int(self.task_time)


    def note(self):
        print("Add note (optional). Insert note or press Enter")
        self.task_note = input("> ")
        return self.task_note


class SearchInExisting:

    def search_in_existing(self):
        self.search_output = self.search_in_existing_choose()
        self.search_by_what()


    def search_by_what(self):
        if self.search_output.upper() == "A":
            self.search_by_exact_date()
        elif self.search_output.upper() == "B":
            self.search_by_range_of_dates()
        elif self.search_output.upper() == "C":
            self.search_by_exact_search()
        elif self.search_output.upper() == "D":
            self.search_by_regex_pattern()
        elif self.search_output.upper() == "E":
            self.what_to_do()
        else:
            print("You entered the wrong value!")
            self.search_by_what()


    def search_in_existing_choose(self):
        print("Do you want search by:")
        print("a) Exact Date")
        print("b) Range of dates")
        print("c) Exact Search")
        print("d) Regex Pattern")
        print("e) Return to menu")
        self.search_output = input("> ")
        os.system('clear')
        return self.search_output


class SearchByExactDate:
    results = []

    def search_by_exact_date(self):
        self.results.clear()
        self.search_by_exact_date_prompt()
        self.search_in_list()
        self.show_results()


    def search_by_exact_date_prompt(self):
        print("Enter the date")
        print("Please use DD/MM/YYYY:")
        self.exact_date = input("< ")
        try:
            datetime.datetime.strptime(self.exact_date, '%d/%m/%Y')
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY!")
            input("Press enter to continue")
            self.search_by_exact_date()
        return self.exact_date


    def search_in_list(self):
        count = 0
        for each in self.entries:
            if each[0] == self.exact_date:
                self.results.append(each)
            else:
                pass
            count += 1
            self.master_count += 1


    def show_results(self):
        if self.results:
            count = 0

            for each in self.results:
                print("Date: {}".format(each[0]))
                print("Title {}".format(each[1]))
                print("Time Spent: {}".format(each[2]))

                if not each[3]:
                    print("Notes: NONE")
                else:
                    print("Notes: {}".format(each[3]))

                print("\nResult(s) {} of {}".format(count + 1, len(self.results)))
                print("[N]ext, [E]dit, [D]elete, [R]eturn to search menu")

                count += 1
                self.show_results_2()

        else:
            print("No entries has been found!")
            self.search_in_existing()


    def show_results_2(self):
        answer = input("< ")
        if answer.upper() == "R":
            self.search_in_existing()
        elif answer.upper() == "D":
            self.delete_entry()
            # vymazat aktualni zaznam
        elif answer.upper() == "E":
            self.edit_entry()
            # editovat aktualni zaznam
        elif answer.upper() == "N":
            self.continue_to_next_entry()
            # pokracovat na dalsi zaznam (pokud je dalsi)
        else:
            print("{} is not correct input. Please insert [N]ext"
            " [E]dit, [D]elete, [R]eturn to search menu".format(answer))
            self.show_results_2()


    def delete_entry(self):
        print(self.master_count - 1)
        print("This entry has been deleted: {}, {}".format(
        self.entries[self.master_count - 1][0],
        self.entries[self.master_count - 1][1])
        )
        del(self.entries[self.master_count - 1])


    def edit_entry(self):
        del(self.entries[self.master_count - 1])
        print("Lets edit this entry!")
        self.add_new_entry()
        print("Entry has been edited")


    def continue_to_next_entry(self):
        if len(self.results) <= 1:
            print("You have only one result!")
            self.show_results()
        else:
            pass


class SearchByRangeOfDates:

    def search_by_range_of_dates(self):
        self.results.clear()
        self.search_by_range_of_dates_prompt()
        self.search_in_list_2()
        self.show_results()


    def search_by_range_of_dates_prompt(self):
        print("Enter the date")
        print("Please use 'DD/MM/YYYY-DD/MM/YYYY:'")
        self.exact_date_2 = input("< ")
        try:
            self.date_1, self.date_2 = self.exact_date_2.split("-")
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY-DD/MM/YYYY!")
            input("Press enter to continue")
            self.search_by_range_of_dates_prompt()
        try:
            datetime.datetime.strptime(self.date_1, '%d/%m/%Y') and datetime.datetime.strptime(
            self.date_2, '%d/%m/%Y')
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY-DD/MM/YYYY!")
            input("Press enter to continue")
            self.search_by_range_of_dates_prompt()
        return self.exact_date_2, self.date_1, self.date_2


    def search_in_list_2(self):
        self.results_2 = []
        self.results_3 = []
        count = 0
        count_2 = 0

        self.from_day, self.from_month, self.from_year = self.date_1.split("/")
        self.to_day, self.to_month, self.to_year = self.date_2.split("/")

        d1 = (self.from_day, self.from_month, self.from_year)
        d3 = (self.to_day, self.to_month, self.to_year)

        while count < len(self.entries):
            self.results_2.append(self.entries[count][0])
            count += 1

        for each in self.results_2:
            print(each)
            self.day, self.month, self.year = each.split("/")
            d2 = (self.day, self.month, self.year)

            if d1 < d2 < d3:
                self.results_3.append(each)
            else:
                pass

        while count_2 < len(self.results_3):
            if self.results_3[count_2] == self.entries[count_2][0]:
                self.results.append(self.entries[count_2])
            else:
                pass
            count_2 += 1


class SearchByExactSearch:

    def search_by_exact_search(self):
        self.results.clear()
        self.search_by_exact_search_prompt()
        self.search_in_list_3(self.entries, self.exact_search)
        self.show_results()


    def search_by_exact_search_prompt(self):
        print("Enter Date, Title, Time Spent or Note:")
        self.exact_search = input("< ")


    def search_in_list_3(self, data1, data2):
        count = 0
        while count < len(data1):
            for each in data1[count]:
                if data2 == each:
                    self.results.append(data1[count])
                else:
                    pass
            count += 1


class SearchByRegexPattern:

    def search_by_regex_pattern(self):
        self.results.clear()
        self.search_by_regex_pattern_prompt()
        self.search_in_list_4(self.entries, self.regex)
        self.show_results()


    def search_by_regex_pattern_prompt(self):
        print("Enter Regex Pattern:")
        self.regex = input("< ")


    def search_in_list_4(data1, data2):
        count = 0
        while count < len(data1):
            for each in data1[count]:
                a = re.findall(data2, each)
                print(each)
                if a == each:
                    results.append(data1[count])
                else:
                    pass
            count += 1
