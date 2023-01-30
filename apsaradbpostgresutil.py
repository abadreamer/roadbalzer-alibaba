import psycopg2;

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="db@08642",
                        port="5432");

cursor = conn.cursor();
cursor.execute("select * from smartathon.visual_pollution");
print(cursor.fetchone());

# insertStmt = "INSERT INTO smartathon.sample (sampleint, samplevar) values (%s, %s)"
# cursor.execute(insertStmt, (13, "sample data 2"));


insertStmt = "INSERT INTO smartathon.visual_pollution (location_latitude, location_longitude, location_city,location_district, pollution_image_path, visual_pollution_type,visual_pollution_severity, location_postal_code, location_governorate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)";

cursor.execute(insertStmt, (24.7738, 46.6964, 
                             "Riyadh", "Taawon", "0a4e0e88a05abd96670c8c0c3a67fc73.jpg", "1", 1, "12479", "Riyadh"
                            ));
conn.commit();
