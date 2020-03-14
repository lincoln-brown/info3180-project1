DROP TABLE IF EXISTS user_profiles;
CREATE TABLE user_profiles (
 id SERIAL PRIMARY KEY,
 first_name VARCHAR(80) not null,
 last_name VARCHAR(80) not null,
 gender VARCHAR(80) not null,
 Email VARCHAR(225) not null,
 Location VARCHAR(255) not null,
 biography VARCHAR(255) not null,
 date date,
 photo VARCHAR(255) not null);
