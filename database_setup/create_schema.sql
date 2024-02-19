-- Script do Banco de Dados Housing


-- Criando Schema
begin;
drop schema if exists housing; 
create schema housing;
use housing;

-- Criando as tabelas

-- Tabela para tipos de propriedade
CREATE TABLE property_type_info (
    type_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    type_description VARCHAR(255)
);

-- Tabela para opções de lavanderia
CREATE TABLE laundry_options_info (
    laundry_option_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    laundry_option_description VARCHAR(255)
);

-- Tabela para opções de estacionamento
CREATE TABLE parking_options_info (
    parking_option_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    parking_option_description VARCHAR(255)
);

-- Tabela para combinações de amenidades
CREATE TABLE amenity_combinations (
    combination_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cats_allowed BOOLEAN,
    dogs_allowed BOOLEAN,
    smoking_allowed BOOLEAN,
    wheelchair_access BOOLEAN,
    electric_vehicle_charge BOOLEAN,
    comes_furnished BOOLEAN
);

-- Tabela para informações de região
CREATE TABLE region_info (
    region_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    region_name VARCHAR(255)
);

-- Tabela para informações de estado
CREATE TABLE state_info (
    state_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_name VARCHAR(255),
    state_abbreviation CHAR(2)
);

-- Tabela para informações de listagem
CREATE TABLE listing_info (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    region_id INT,
    state_id INT,
    price DECIMAL,
    description TEXT,
    latitude DECIMAL,
    longitude DECIMAL,
    FOREIGN KEY (region_id) REFERENCES region_info(region_id),
    FOREIGN KEY (state_id) REFERENCES state_info(state_id)
);

-- Tabela para informações da propriedade
CREATE TABLE property_info (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    type_id INT,
    sqfeet INT,
    beds INT,
    baths INT,
    FOREIGN KEY (id) REFERENCES listing_info(id),
    FOREIGN KEY (type_id) REFERENCES property_type_info(type_id)
);

-- Tabela para informações de amenidades
CREATE TABLE amenities_info (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    combination_id INT,
    laundry_option_id INT,
    parking_option_id INT,
    FOREIGN KEY (id) REFERENCES listing_info(id),
    FOREIGN KEY (combination_id) REFERENCES amenity_combinations(combination_id),
    FOREIGN KEY (laundry_option_id) REFERENCES laundry_options_info(laundry_option_id),
    FOREIGN KEY (parking_option_id) REFERENCES parking_options_info(parking_option_id)
);

-- Precisa adicionar latitude e longitude como chaves estrangeiras para manter a integridade relacional
 
 
 -- Populando as tabelas
 
-- Inserir regiões
INSERT INTO region_info (region_id, region_name)
VALUES (1,	'reno / tahoe');

-- Inserir estados
INSERT INTO state_info (state_id, state_name, state_abbreviation)
VALUES (1,	'alabama',	'al'),
       (2,	'alaska',	'ak'),
       (3,	'arizona',	'az'),
       (4,	'arkansas',	'ar'),
       (5,	'california',	'ca'),
       (6,	'colorado',	'co'),
       (7,	'connecticut',	'ct'),
       (8,	'district of columbia',	'dc'),
       (9,	'delaware',	'de'),
       (10,	'florida',	'fl'),
       (11,	'georgia',	'ga'),
       (12,	'hawaii',	'hi'),
       (13,	'idaho',	'id'),
       (14,	'illinois',	'il'),
       (15,	'indiana',	'in'),
       (16,	'iowa',	'ia'),
       (17,	'kansas',	'ks'),
       (18,	'kentucky',	'ky'),
       (19,	'louisiana',	'la'),
       (20,	'maine',	'me'),
       (21,	'maryland',	'md'),
       (22,	'massachusetts',	'ma'),
       (23,	'michigan',	'mi'),
       (24,	'minnesota',	'mn'),
       (25,	'mississippi',	'ms'),
       (26,	'missouri',	'mo'),
       (27,	'montana',	'mt'),
       (28,	'nebraska',	'ne'),
       (29,	'nevada',	'nv'),
       (30,	'new hampshire',	'nh'),
       (31,	'new jersey',	'nj'),
       (32,	'new mexico',	'nm'),
       (33,	'new york',	'ny'),
       (34,	'north carolina',	'nc'),
       (35,	'north dakota',	'nd'),
       (36,	'ohio',	'oh'),
       (37,	'oklahoma',	'ok'),
       (38,	'oregon',	'or'),
       (39,	'pennsylvania',	'pa'),
       (40,	'rhode island',	'ri'),
       (41,	'south carolina',	'sc'),
       (42,	'south dakota',	'sd'),
       (43,	'tennessee',	'tn'),
       (44,	'texas',	'tx'),
       (45,	'utah',	'ut'),
       (46,	'vermont',	'vt'),
       (47,	'virginia',	'va'),
       (48,	'washington',	'wa'),
       (49,	'west virginia',	'wv'),
       (50,	'wisconsin',	'wi'),
       (51,	'wyoming',	'wy');


-- Inserir tipos de propriedade
INSERT INTO property_type_info (type_id, type_description)
VALUES (1,	'apartment'),
       (2,	'condo'),
       (3,	'house'),
       (4,	'duplex'),
       (5,	'townhouse'),
       (6,	'loft'),
       (7,	'manufactured'),
       (8,	'cottage/cabin'),
       (9,	'flat'),
       (10,	'in-law'),
       (11,	'land'),
       (12,	'assisted living');

-- Inserir opções de lavanderia
INSERT INTO laundry_options_info (laundry_option_id, laundry_option_description)
VALUES (1,	'w/d in unit'),
       (2,	'w/d hookups'),
       (3,	'laundry on site'),
       (4,	'laundry in bldg'),
       (5,	'no laundry on site');

-- Inserir opções de estacionamento
INSERT INTO parking_options_info (parking_option_id, parking_option_description)
VALUES (1,	'carport'),
       (2,	'attached garage'),
       (3,	'off-street parking'),
       (4,	'detached garage'),
       (5,	'street parking'),
       (6,	'no parking'),
       (7,	'valet parking');

-- Inserir combinações de amenidades
INSERT INTO amenity_combinations (combination_id, cats_allowed, dogs_allowed, smoking_allowed, wheelchair_access, electric_vehicle_charge, comes_furnished)
VALUES (1,	0,	0,	0,	0,	0,	0),
       (2,	0,	0,	0,	0,	0,	1),
       (3,	0,	0,	0,	0,	1,	0),
       (4,	0,	0,	0,	0,	1,	1),
       (5,	0,	0,	0,	1,	0,	0),
       (6,	0,	0,	0,	1,	0,	1),
       (7,	0,	0,	0,	1,	1,	0),
       (8,	0,	0,	0,	1,	1,	1),
       (9,	0,	0,	1,	0,	0,	0),
       (10,	0,	0,	1,	0,	0,	1),
       (11,	0,	0,	1,	0,	1,	0),
       (12,	0,	0,	1,	0,	1,	1),
       (13,	0,	0,	1,	1,	0,	0),
       (14,	0,	0,	1,	1,	0,	1),
       (15,	0,	0,	1,	1,	1,	0),
       (16,	0,	0,	1,	1,	1,	1),
       (17,	0,	1,	0,	0,	0,	0),
       (18,	0,	1,	0,	0,	0,	1),
       (19,	0,	1,	0,	0,	1,	0),
       (20,	0,	1,	0,	0,	1,	1),
       (21,	0,	1,	0,	1,	0,	0),
       (22,	0,	1,	0,	1,	0,	1),
       (23,	0,	1,	0,	1,	1,	0),
       (24,	0,	1,	0,	1,	1,	1),
       (25,	0,	1,	1,	0,	0,	0),
       (26,	0,	1,	1,	0,	0,	1),
       (27,	0,	1,	1,	0,	1,	0),
       (28,	0,	1,	1,	0,	1,	1),
       (29,	0,	1,	1,	1,	0,	0),
       (30,	0,	1,	1,	1,	0,	1),
       (31,	0,	1,	1,	1,	1,	0),
       (32,	0,	1,	1,	1,	1,	1),
       (33,	1,	0,	0,	0,	0,	0),
       (34,	1,	0,	0,	0,	0,	1),
       (35,	1,	0,	0,	0,	1,	0),
       (36,	1,	0,	0,	0,	1,	1),
       (37,	1,	0,	0,	1,	0,	0),
       (38,	1,	0,	0,	1,	0,	1),
       (39,	1,	0,	0,	1,	1,	0),
       (40,	1,	0,	0,	1,	1,	1),
       (41,	1,	0,	1,	0,	0,	0),
       (42,	1,	0,	1,	0,	0,	1),
       (43,	1,	0,	1,	0,	1,	0),
       (44,	1,	0,	1,	0,	1,	1),
       (45,	1,	0,	1,	1,	0,	0),
       (46,	1,	0,	1,	1,	0,	1),
       (47,	1,	0,	1,	1,	1,	0),
       (48,	1,	0,	1,	1,	1,	1),
       (49,	1,	1,	0,	0,	0,	0),
       (50,	1,	1,	0,	0,	0,	1),
       (51,	1,	1,	0,	0,	1,	0),
       (52,	1,	1,	0,	0,	1,	1),
       (53,	1,	1,	0,	1,	0,	0),
       (54,	1,	1,	0,	1,	0,	1),
       (55,	1,	1,	0,	1,	1,	0),
       (56,	1,	1,	0,	1,	1,	1),
       (57,	1,	1,	1,	0,	0,	0),
       (58,	1,	1,	1,	0,	0,	1),
       (59,	1,	1,	1,	0,	1,	0),
       (60,	1,	1,	1,	0,	1,	1),
       (61,	1,	1,	1,	1,	0,	0),
       (62,	1,	1,	1,	1,	0,	1),
       (63,	1,	1,	1,	1,	1,	0),
       (64,	1,	1,	1,	1,	1,	1);

-- Inserir dados das listagens
INSERT INTO listing_info (id, region_id, state_id, price, description, latitude, longitude)
VALUES (1,	1,	5,	1148,	'Ridgeview by Vintage is where you will find all of your apartment living needs at a price you can afford! ...',	39.5483,	-119.796),
       (2,	1,	5,	1200,	'Conveniently located in the middle town of Reno. Close to Highway, 10 mins to UNR, shopping and restaurants...',	39.5026,	-119.789),
       (3,	1,	5,	1813,	'2BD | 2BA | 1683SQFT Discover exceptional service and well-designed spacious floor plans at Caviata apartment homes in Sparks, Nevada...',	39.6269,	-119.708),
       (4,	1,	5,	1095,	'MOVE IN SPECIAL FREE WASHER/DRYER WITH 6 OR 12 MONTH LEASE! *Ask about our preferred employer program for extra discounts!...',	39.4477,	-119.771),
       (5,	1,	5,	289,	'Move In Today: Reno Low-Cost, Clean & Furnished Apartments close to Restaurants, Cafes, Parks, and More! Call Us! Move In Today!...',	39.5357,	-119.805),
       (6,	1,	5,	1093,	'1BD | 1BA | 720SQFT In addition to attractive, comfortable apartments, Village at Iron Blossom combines all that Reno has to offer...',	39.4572,	-119.776),
       (7,	1,	5,	935,	'Tucked away in a park-like setting on the edge of midtown, located just minutes from shopping, restaurants...',	39.5118,	-119.802),
       (8,	1,	5,	1095,	'MOVE IN SPECIAL FREE WASHER/DRYER WITH 6 OR 12 MONTH LEASE! *Ask about our preferred employer program for extra discounts!...',	39.4477,	-119.771),
       (9,	1,	5,	1525,	'BRAND NEW APARTMENT HOMES, NOW OPEN! **GET 1 MONTH FREE AND WAIVED APPLICATION AND ADMIN FEES!! **O.A.C when you sign a 12-month lease**...',	39.6185,	-119.672),
       (10,	1,	5,	1295,	'6850 Sharlands Ave E-1021 Reno NV 89523 Property Address 6850 Sharlands Avenue E-1021 | Reno, NV 89523 Available: 02/07/2020 Offered By Dickson Realty, Inc...',	39.5193,	-119.897);

INSERT INTO property_info (id, type_id, sqfeet, beds, baths)
VALUES (1,	1,	1078,	3,	2),
       (2,	2,	1001,	2,	2),
       (3,	1,	1683,	2,	2),
       (4,	1,	708,	1,	1),
       (5,	1,	250,	0,	1),
       (6,	1,	720,	2,	2),
       (7,	1,	661,	1,	1),
       (8,	1,	708,	1,	1),
       (9,	1,	1053,	2,	2),
       (10,	2,	930,	2,	2);

INSERT INTO amenities_info (id, combination_id, laundry_option_id, parking_option_id)
VALUES (1,	50,	1,	2),
       (2,	40,	2,	1),
       (3,	30,	1,	2),
       (4,	10,	2,	1),
       (5,	20,	1,	2),
       (6,	60,	2,	2),
       (7,	1,	1,	1),
       (8,	5,	2,	1),
       (9,	25,	1,	2),
       (10,	30,	2,	2);
