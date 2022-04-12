import sqlite3
import pandas as pd

option = ''

connection = sqlite3.connect('contactbook.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(Name TEXT, Email TEXT, Phone TEXT, ID INT PRIMARY KEY)''')

connection.commit()



def main():
	print("-"*50)
	print("Contact Book!")
	print("-"*50)
	print('''
		[1] - Add Contact\n
		[2] - Delete Contact\n
		[3] - Show Contacts\n
		[4] - Help\n
		[5] - Exit\n
		''')

def option1():
	connection = sqlite3.connect('contactbook.db')
	connection.cursor()
	s_name = input("Name: ")
	s_email =input("Email: ")
	s_phone = input("Phone: ")
	s_ID = int(input("ID: "))
	cursor.execute("INSERT INTO contacts VALUES (?, ?, ?, ?)", (s_name, s_email, s_phone, s_ID))
	connection.commit()
	print("Added "+ s_name+" "+ s_email+" "+ s_phone+" Successfully!")



def option2():
	print("Please type in the ID of the contact you would like to remove.")
	s_ID = int(input("ID: "))
	with connection:
		cursor.execute("""DELETE from contacts WHERE ID = :ID""",{'ID': s_ID})

def option3():
	print(pd.read_sql_query("SELECT * FROM contacts", connection))
	




main()


while option != 5:
	print("-"*50)
	option = int(input("Choose an option: "))
	print("-"*50)
	if option == 1:
		option1()

	elif option == 2:
		option2()

	elif option == 3:
		option3()

	elif option == 4:
		main()

	elif option == 5:
		print("Exiting...")
		connection.commit()
		connection.close()
		exit()
	else:
		print("Invalid Input")


