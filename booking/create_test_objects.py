import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tik-71.Lion",
    database="accommodation",
    )

my_cursor = mydb.cursor()

# formulas for inserting rows in the tables according to the models fields
sql_formula_hot = "INSERT INTO booking_hotel (name, country, city) VALUES (%s, %s, %s)"
sql_formula_ap = "INSERT INTO booking_apartment (name, country, city, price)" \
                  " VALUES (%s, %s, %s, %s)"
sql_formula_rt = "INSERT INTO booking_roomtype(name, price, hotel_id)" \
                  " VALUES (%s, %s, %s)"
sql_formula_rm = "INSERT INTO booking_room(room_type_id, number)" \
                  " VALUES (%s, %s)"

# list with values for random selection to create the objects
names = {"hotel": ["Hotel Royal", "Hotel Inter", "Hotel Ambassador"], "apartment": ["Best View", "Worst View"]}
countries = [("UK", "London"), ("Bulgaria", "Sofia"), ("Italy", "Milan"), ("France", "Paris")]
prices = [60.00, 80.00, 100.00, 150.00, 200.00, 250, 300]
room_types = ["single", "double", " triple", "lux", "superior"]
numbers = [103, 104, 105, 106, 107, 308, 309]


def create_test_properties(n):  # creates apartments and hotels
    for i in range(n):
        property_type = random.choice(list(names.keys()))
        name = random.choice(names[property_type])
        c = random.choice(countries)
        country, city = c[0], c[1]
        if property_type == "hotel":
            val = (name, country, city)
            my_cursor.execute(sql_formula_hot, val)
        else:
            price = random.choice(prices)
            val = (name, country, city, price)
            my_cursor.execute(sql_formula_ap, val)
        mydb.commit()

    my_cursor.execute("SELECT * FROM booking_hotel")
    my_result = my_cursor.fetchall()
    for i in my_result:
            print(i)

    my_cursor.execute("SELECT * FROM booking_apartment")
    my_result = my_cursor.fetchall()
    for i in my_result:
            print(i)

create_test_properties(10)

def create_room_type(n):
    my_cursor.execute("SELECT id FROM booking_hotel")
    my_result = my_cursor.fetchall()
    unique = []  # list to save combinations of hotel & room_type ( must be unique)
    for i in range(n):
        r_type = random.choice(room_types)
        price = random.choice(prices)
        hotel = (random.choice(my_result))[0]
        vals = (r_type, price, hotel)
        hot_rm = (r_type, hotel)
        if hot_rm not in unique:
            my_cursor.execute(sql_formula_rt, vals)
            mydb.commit()
            unique.append(hot_rm)
    my_cursor.execute("SELECT * FROM booking_roomtype")
    my_result = my_cursor.fetchall()
    for i in my_result:
        print(i)

create_room_type(20)

def create_rooms(n):
    my_cursor.execute("SELECT id FROM booking_roomtype")
    my_result = my_cursor.fetchall()
    unique = {}
    for i in my_result:
        room_type = i[0]
        number = random.choice(numbers)
        my_cursor.execute(sql_formula_rm, (room_type, number))
    my_cursor.execute("SELECT * FROM booking_roomtype")
    my_result = my_cursor.fetchall()
    for i in my_result:
        print(i)

create_rooms(60)

def clean_tables():
    my_cursor.execute("DELETE from booking_room")
    my_cursor.execute("DELETE from booking_roomtype")
    my_cursor.execute("DELETE from booking_hotel")
    my_cursor.execute("DELETE from booking_apartment")
    mydb.commit()
    my_cursor.execute("SELECT * FROM booking_hotel")
    my_result = my_cursor.fetchall()
    for i in my_result:
        print(i)

clean_tables()




