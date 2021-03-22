import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd ="1234",
   # auth_plugin='mysql_native_password',
    database ="usedcars"
)

my_cursor = db.cursor()

def query_state(x):
    abc = ("SELECT latitude,longitude,price,car_year,model,manufacturer,region,paint_color,fuel,state FROM usedcars.used_cars_dashboard " 
            "where state = %s and car_year >= 2000 order by car_year")
    myresult = my_cursor.execute(abc,(x,))
    myresult = my_cursor.fetchall()
    headings = [i[0] for i in my_cursor.description]
    return pd.DataFrame(myresult, columns = headings)