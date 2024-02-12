import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "ferraz2013",
    database = "housing"   #precisa criar o shcema no banco  
)

#Creating tables

cursor = connection.cursor()

create_regionstatetbl = '''
CREATE TABLE REGIONSTATE (
    region VARCHAR(31),
    state TEXT,
    PRIMARY KEY (region)
);
'''

cursor.execute(create_regionstatetbl)
connection.commit()

create_latlongregiontbl = '''
CREATE TABLE LATLONGREGION(
latitude DOUBLE SIGNED ,
longitude DOUBLE SIGNED ,
region VARCHAR(31),
PRIMARY KEY(latitude, longitude),
FOREIGN KEY(region) REFERENCES REGIONSTATE(region)
);
'''

cursor.execute(create_latlongregiontbl)
connection.commit()

create_principaltbl = '''
CREATE TABLE PRINCIPAL(
id BIGINT,
region VARCHAR(31),
price DOUBLE,
houseType TEXT,
sqFeet INT,
beds INT,
baths INT,
catsAllowed INT,
dogsAllowed INT,
smokingAllowed INT,
comesFurnished INT,
latitude DOUBLE SIGNED,
longitude DOUBLE SIGNED,
PRIMARY KEY(id),
FOREIGN KEY(region) REFERENCES REGIONSTATE(region)
); 
'''

cursor.execute(create_principaltbl)
connection.commit()

cursor.close()
connection.close()
