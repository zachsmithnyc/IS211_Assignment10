import sqlite3 as lite

con = lite.connect('pets.db')

persons = (('James', 'Smith', 41), ('Diana', 'Greene', 23), ('Sara', 'White', 27), ('William', 'Gibson', '23'))
pets = (('Rusty', 'Dalmation', 4, 1), ('Bella', 'Alaskan Malamute', 3, 0), ('Max', 'Cocker Spaniel', 1, 0), ('Rocky', 'Beagle', 7, 0), ('Rufus', 'Cocker Spaniel', 1, 0), ('Spot', 'Bloodhound', 2, 1))
person_pet = ((1,1), (1,2), (2,3), (2, 4), (3, 5), (4, 6))

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS person")
    cur.execute("DROP TABLE IF EXISTS pet")
    cur.execute("DROP TABLE IF EXISTS person_pet")
    cur.execute("CREATE TABLE person (id INTEGER PRIMARY KEY ASC, first_name TEXT, last_name TEXT, age INTEGER)")
    cur.execute("CREATE TABLE pet (id INTEGER PRIMARY KEY ASC, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
    cur.execute("CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER)")
    
    cur.executemany("INSERT INTO person (first_name, last_name, age) VALUES (?,?,?)", persons)
    
    cur.executemany("INSERT INTO pet (name, breed, age, dead) VALUES (?,?,?,?)", pets)

    cur.executemany("INSERT INTO person_pet VALUES (?,?)", person_pet)


