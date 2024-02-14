import mysql.connector
# creating a connection 
conn = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

# creating a cursor object that can be used to 
# navigate the connection 

cursor = conn.cursor()

# geting a word from the user 
word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM  Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

# constructing a loop to extract all the tuples 
if results:
    for result in results:
        print(result(1))  # printing the second item which is the definition
else:
    print("No word found")

