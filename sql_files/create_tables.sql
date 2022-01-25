-- create_table.sql - Code needed to create the tables from the ERD:
--   https://lucid.app/lucidchart/6693c4a1-348e-4c93-acfb-c3f6dc8658ce/edit?invitationId=inv_5690ccb3-8faf-46bf-a86b-2dd05e26ce3e

CREATE TABLE users (
  userId SERIAL PRIMARY KEY NOT NULL,
  userName VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(50) NOT NULL,
  salt CHAR(25) NOT NULL,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE NOT NULL,
  dob DATE NOT NULL,
  sex BOOLEAN NOT NULL
  -- TODO: profilePhotoLink 
);

ALTER TABLE Users OWNER TO admin;
