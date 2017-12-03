import queryBuilder     # Dynamically builds query (local file)

# import nltk             # For Parsing
import sys              # for sys.exit
import mysql.connector  # for querying db
from mysql.connector import errorcode  # for handling bad connections, etc.


# Replace all occurances starting with the second

# Connect to DB
GoodDb = False
while GoodDb is False:
    # IP = input("Select Server IP or \"Exit\" to quit: ")
    # if IP.lower() == "exit":
    #     sys.exit("Have a nice Day :)")
    # User = input("Username: ")
    # Pass = input("Password: ")
    # DB = input("Select Database to use: ")
    User = 'root'
    Pass = 'Password1'
    IP = 'localhost'
    DB = 'Gamedb'
    try:  # try statement to ensure connection is valid
        dbcon = mysql.connector.connect(user=User, password=Pass, host=IP, database=DB)
    except mysql.connector.Error as err:
        GoodDb = False  # since connecting threw error
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials\n")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(DB + " is an invalid database name\n")  # maybe print name of valid db?
            # Query: show databases?
        else:
            print("Error with connecting to db: ", err, '\n')
    else:
        GoodDb = True  # no errors caught, db is good
        cursor = dbcon.cursor()  # used to query db

# while True:
# s = input("Please enter a Query or \"Exit\" to quit\n")
s = "list every game"
if s.lower() == "exit":
    sys.exit("Have a nice Day :)")


# if s.lower().find("from database") != -1:
#     print("Please select a valid Database Table (Tables are listed below)")
#     showTablesQuery = "show tables;"
#     cursor.execute(showTablesQuery)  # executes query, we could also just have a static list to print out
#     allTables = cursor.fetchall()
#     print('\n', allTables, '\n')
#     # continue

s = queryBuilder.buildQuery(s)  # should be of form select..from..where


try:
    cursor.execute(s)
except mysql.connector.Error:
    print("Query: \"" + s + "\" Failed to Execute")
else:
    output = cursor.fetchall()
    for row in output:
        print(row[0])

cursor.close()  # close cursor, bad form to keep open
dbcon.close()   # close connection, bad form to keep open
