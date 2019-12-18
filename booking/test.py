import random


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tik-71.Lion",
    database="accommodation",
    )

my_cursor = mydb.cursor()

sql_formula = "INSERT INTO hotels_rooms_accommodations(property_type, name, country, city) VALUES (%s, %s, %s, %s)"

names = {"hotel": ["Hotel Royal", "Hotel Inter", "Hotel Ambassador"], "apartment": ["Best View", "Worst View"]}
countries = [("UK", "London"), ("Bulgaria", "Sofia"), ("Italy", "Milan"), ("France", "Paris")]

print(random.choice(list(names.keys())))

def create_test_accomodations():
    n = 4
    for i in range(n):
        property_type = random.choice(list(names.keys())),
        nickname = random.choice(names[property_type[0]])
        c = random.choice(countries)
        country, city = c[0], c[1]
        print(property_type, nickname, country, city)
        val = (property_type, nickname, country, city)
        my_cursor.execute(sql_formula, val)
        mydb.commit()

        my_cursor.execute("SELECT * FROM accommodation.hotels_rooms_accommodation")
        my_result = my_cursor.fetchall()
        for i in my_result:
            print(i)
        my_cursor.execute("DELETE FROM inventory.hotels_rooms_accommodation")
        # mydb.commit()

create_test_hotels ()
n = 15
for i in range(n):
    property_type = random.choice(list(names.keys())),
    nickname = random.choice(names[property_type[0]])
    c = random.choice(countries)
    country, city = c[0], c[1]
    print(property_type, nickname, country, city)
    val = (property_type, nickname, country, city)
    my_cursor.execute(sql_formula, val)
    mydb.commit()

    my_cursor.execute("SELECT * FROM accommodation.hotels_rooms_accommodation")
    my_result = my_cursor.fetchall()
    for i in my_result:
        print(i)
    my_cursor.execute("DELETE FROM inventory.hotels_rooms_accommodation")
    mydb.commit()