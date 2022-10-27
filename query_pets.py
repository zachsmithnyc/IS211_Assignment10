import sqlite3 as lite

DB_PATH = 'pets.db'
PERSON_QRY = "SELECT first_name, last_name, age FROM person WHERE id=?"
PETS_QRY = "SELECT p.name, p.breed, p.age, p.dead FROM pet p INNER JOIN person_pet pp ON pp.pet_id = p.id INNER JOIN person ps ON ps.id = pp.person_id WHERE ps.id == ?"

def print_data():
    """
    param: person id
    return: data printout
    """
    con = lite.connect(DB_PATH)
    print('Welcome to the pets database')

    with con:
            
        cur = con.cursor()
        id = int(input("Please enter owner id: "))
        while id > 0:
            cur.execute(PERSON_QRY, (id,))
            row = cur.fetchone()

            if row:
                print(f"{row[2]} year old {row[0]} {row[1]}")

                cur.execute(PETS_QRY, (id,))
                records = cur.fetchall()
        
                for r in records:
                    if r[3] == 1:
                        print(f"Owned {r[0]} a {r[1]} who was {r[2]} years old.")
                    else:
                        print(f"Owns {r[0]} a {r[1]} who is {r[2]} years old.")
            else:
                print(f"id: {id} does not exist.")
            
            id = int(input("Please enter owner id: "))

        else:
            print("so long space cowboy")

if __name__ == "__main__":
    print_data()
        

    
        
            

        
        
            

        
