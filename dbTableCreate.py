def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

create_table()

def enter_data():
    c.execute("INSERT INTO example VALUES ('Python', '2.7', 'Beginner')")
    c.execute("INSERT INTO example VALUES ('Python', '3.3', 'Expert')")
    c.execute("INSERT INTO example VALUES ('Python', '3.6', 'Intermediate')")

def enter_dynamic_data():
    variety = input("What flavah? ")
    vineyard = input("Where from? ")
    year = input("Which year? ")

    c.execute("INSERT INTO wino (Variety, Vineyard, Year) VALUES (?,?,?)", (variety, vineyard, year))

    conn.commit()
    