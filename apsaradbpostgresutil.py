import psycopg2;
import os;

# import click
from flask import current_app, g


roadblazer_db_host = os.getenv('ROADBLAZER_DB_HOST',)
roadblazer_db_pwd = os.getenv('ROADBLAZER_DB_PWD',)

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(database="postgres",
                                host=roadblazer_db_host,
                                user="postgres",
                                password=roadblazer_db_pwd,
                                port="5432");

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)


def insertDectection(location_latitude, location_longitude, location_city,location_district, pollution_image_path, visual_pollution_type,visual_pollution_severity, location_postal_code, location_governorate):
    conn = get_db();
    cursor = conn.cursor()
    insertStmt = "INSERT INTO visual_pollution (location_latitude, location_longitude, location_city,location_district, pollution_image_path, visual_pollution_type,visual_pollution_severity, location_postal_code, location_governorate)\
          VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)";

    cursor.execute(insertStmt, (location_latitude, location_longitude, 
                                location_city, location_district, pollution_image_path,
                                visual_pollution_type, visual_pollution_severity, location_postal_code,
                                location_governorate
                                ));
    conn.commit();

# cursor = conn.cursor();
# cursor.execute("select * from visual_pollution");
# print(cursor.fetchone());

# # insertStmt = "INSERT INTO smartathon.sample (sampleint, samplevar) values (%s, %s)"
# # cursor.execute(insertStmt, (13, "sample data 2"));


# insertStmt = "INSERT INTO visual_pollution (location_latitude, location_longitude, location_city,location_district, pollution_image_path, visual_pollution_type,visual_pollution_severity, location_postal_code, location_governorate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)";

# cursor.execute(insertStmt, (24.7738, 46.6964, 
#                              "Riyadh", "Taawon", "0a4e0e88a05abd96670c8c0c3a67fc73.jpg", "1", 1, "12479", "Riyadh"
#                             ));
# conn.commit();
