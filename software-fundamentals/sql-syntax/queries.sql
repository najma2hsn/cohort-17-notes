
-- GET species where the scientific name has rex
SELECT * 
FROM species 
WHERE scientific_name ~ 'rex';

-- A second query

SELECT *
FROM species
LIMIT 20;

-- Pokemon

CREATE TABLE pokemon (
    pokemon_id int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    pokemon_name varchar(35)
);

CREATE TABLE pokemon_type_assigment (
    pokemon_type_assigment_id int PRIMARY KEY,
    pokemon_id int,
    type_id int,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id)
);

SELECT p.pokemon_name 
from pokemon as p,
JOIN pokemon_type_assigment as t USING(pokemon_id);
