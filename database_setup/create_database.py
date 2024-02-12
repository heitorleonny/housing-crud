import pymysql


def create_table(command):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "ferraz2013",
        database = "housing"
    )

    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()


    cursor.close()
    connection.close()

create_regionstatetbl = '''
CREATE TABLE REGIONSTATE (
    region VARCHAR(31),
    state TEXT,
    PRIMARY KEY (region)
);
'''

create_latlongregiontbl = '''
CREATE TABLE LATLONGREGION(
latitude DOUBLE SIGNED ,
longitude DOUBLE SIGNED ,
region VARCHAR(31),
PRIMARY KEY(latitude, longitude),
FOREIGN KEY(region) REFERENCES REGIONSTATE(region)
);
'''
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
FOREIGN KEY(region) REFERENCES REGIONSTATE(region),
FOREIGN KEY(latitude,longitude) REFERENCES LATLONGREGION(latitude,longitude)
); 

'''


create_table(create_regionstatetbl)
create_table(create_latlongregiontbl)
create_table(create_principaltbl)
