"""# Load Database Pkg
import sqlite3
conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\project\\end2end-nlp-project\\App\\data.db',check_same_thread=False)
c = conn.cursor()"""
import sqlite3
from sqlite3 import Error
from datetime import datetime
conn = sqlite3.connect('C:\\Users\\hp\\Desktop\\project\\end2end-nlp-project\\App\\data.db',check_same_thread=False)
c = conn.cursor()

DATABASE_PATH = 'C:\\Users\\hp\\Desktop\\project\\end2end-nlp-project\\App\\data.db'

def create_page_visited_table():
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS pageTrackTable1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pagename TEXT NOT NULL,
                timeOfvisit TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error creating table: {e}")

def add_page_visited_details(pagename, time_of_visit):
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        c.execute('INSERT INTO pageTrackTable1(pagename, timeOfvisit) VALUES (?, ?)', (pagename, time_of_visit))
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error inserting data: {e}")

# Other functions...

# Uncomment the line below if you want to create the table when this script is executed
# create_page_visited_table()



# Fxn
def create_page_visited_table():
	c.execute('CREATE TABLE pageTrackTable1(pagename TEXT,timeOfvisit TIMESTAMP)')
	
def add_page_visited_details(pagename,timeOfvisit):
	c.execute('INSERT INTO pageTrackTable1(pagename,timeOfvisit) VALUES(?,?)',(pagename,timeOfvisit))
	#conn.commit()

def view_all_page_visited_details():
	c.execute('SELECT * FROM pageTrackTable1')
	data = c.fetchall()
	return data


# Fxn To Track Input & Prediction
def create_emotionclf_table():
	c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT,prediction TEXT,probability NUMBER,timeOfvisit TIMESTAMP)')
	

def add_prediction_details(rawtext,prediction,probability,timeOfvisit):
	c.execute('INSERT INTO emotionclfTable(rawtext,prediction,probability,timeOfvisit) VALUES(?,?,?,?)',(rawtext,prediction,probability,timeOfvisit))
	#conn.commit()
	

def view_all_prediction_details():
	c.execute('SELECT * FROM emotionclfTable')
	data = c.fetchall()
	return data