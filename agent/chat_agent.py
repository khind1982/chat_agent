import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="H0liday_info",
    database="holiday_agent"
)


def render_input_criteria(criteria):
    input_criteria = []
    for c in criteria:
        if len(c) > 0:
            input_criteria.append(c)
    return input_criteria


def retrieve_holiday_data(criteria):
    results = []
    mycursor = db.cursor()
    category, temp_rating, location = render_input_criteria(criteria)
    sql = "SELECT city, price, country, hotel_name FROM holiday WHERE category IN (%s) AND temp_rating IN (%s) AND location IN (%s)"
    values = (category, temp_rating, location)
    mycursor.execute(sql, values)
    result = mycursor.fetchall()
    for x in result:
        results.append(x)
    return results