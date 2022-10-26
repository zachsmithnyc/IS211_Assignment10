import sqlite3 as lite

def print_data(id):
    """
    param: person id
    return: data printout
    """
    con = lite.connect('pets.db')

    with con:

        cur = con.cursor()
        cur.execute("SELECT first_name, last_name, age FROM person WHERE id=?", id)

        row = cur.fetchone()
        print(row)

        cur.executescript("SELECT name, breed, age, dead FROM pet WHERE ")

    if id == None:
        raise ValueError("That id does not exist")

if __name__ == "__main__":
    print('Welcome to the pets database')
    id = input('Please enter an id: ')
    print_data(id)
