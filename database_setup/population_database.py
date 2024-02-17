import pymysql

def populate_database(command):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "popopipiska",
        database = "housing"
    )

    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

    cursor.close()
    connection.close()

insert_into_principaltbl = '''
INSERT INTO PRINCIPAL VALUES
(7049044568,	"reno / tahoe",	1148,	"apartment",	1078,	3,	2,	1,	1,	1,	0,	39.5483,	119.789),
(7036140506,	"stockton",	1264,	"apartment",	830,	2,	1,	1,	1,	1,	0,	38.0228,	-121.361),
(7043770605	,"gainesville"	,750	,"apartment"	,1200	,3	,2	,1	,1	,1	,1	,29.6456	,-82.4033),
(7049732893,	"sarasota-bradenton",	3500,	"apartment",	13060,	1,	1,	1,	1,	1,	0,	27.3390,	-82.5427),
(7013425856,	"macon / warner robin",	615,	"apartment",	750,	2,	1,	1,	1,	1,	0,	33.0686,	-83.2636),
(7033444068,	"quad cities, IA/IL",	1800,	"apartment",	1278,	3,	2,	1,	1,	1,	0,	41.5509,	-90.4942),
(7043853783,	"topeka",	825, "townhouse",	723,	2,	1,	1,	1,	0,	0,	39.0515,	-95.6848),
(7032660975,	"rochester",	781,	"apartment",	875,	2,	1,	1,	1,	1,	1,	44.0558,	-92.457),
(7041392110,	"south jersey",	1050,	"apartment",	800,	2,	1,	1,	1,	1,	1,	39.6976,	-75.4068),
(7049162741,	"knoxville",	899,	"house",	1132,	2,	0,	1,	0,	1,	0,	36.1953,	-83.3797),
(7044520714,	"wichita falls",	990,	"apartment",	1050,	3,	2,	1,	1,	0,	0,	33.9675,	-98.6868)
;
'''

insert_into_latlongregiontbl = '''
 INSERT INTO LATLONGREGION VALUES
 (39.5483,	119.789,"reno / tahoe"),
 (38.0228,	-121.361,	"stockton"),
 (29.6456,	-82.4033,	"gainesville"),
 (27.3390,	-82.5427,	"sarasota-bradenton"),
 (33.0686, -83.2636,	"macon / warner robin"),
 (41.5509,	-90.4942,	"quad cities, IA/IL"),
 (39.0515,	-95.6848,	"topeka"),
 (44.0558,	-92.457,	"rochester"),
 (39.6976,	-75.4068,	"south jersey"),
 (36.1953,	-83.3797,	"knoxville"),
 (33.9675,	-98.6868,	"wichita falls")
 ;
'''

insert_into_regionstatetbl = ''' 
 INSERT INTO REGIONSTATE VALUES
 ("reno / tahoe"	,"ca"),
 ("stockton",	"ca"),
 ("gainesville",	"fl"),
 ("sarasota-bradenton","fl"),
 ("macon / warner robin",	"ga"),
 ("quad cities, IA/IL",	"il"),
 ("topeka",	"ks"),
 ("rochester",	"mn"),
 ("south jersey",	"nj"),
 ("knoxville",	"tn"),
 ("wichita falls",	"tx")
 ;
 '''

populate_database(insert_into_regionstatetbl)
populate_database(insert_into_latlongregiontbl)
populate_database(insert_into_principaltbl)