import sqlite3

connection = sqlite3.connect('databases_file/add_questions.db')

cursor = connection.cursor()
cursor.execute("create table enish (classes integer, question text, answer text)")

question_list=[
    (8, "What is your name?", "Enish Pandey"),
    (9, "What is your name?", "Anish Pandey")
]
cursor.executemany("insert into enish values(?,?,?)", question_list)

for row in cursor.execute("select * from enish"):
    print(row)

# cursor.execute("select * from enish where classes=:c", {"c": 9})
# fetch_data = cursor.fetchall()
# print(fetch_data)




connection.close()