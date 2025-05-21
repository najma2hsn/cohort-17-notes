DROP TABLE IF EXISTS enclosure_type;
DROP TABLE IF EXISTS dinosaur;
DROP TABLE IF EXISTS species;
DROP TYPE dinosaur_gender;

CREATE TYPE dinosaur_gender AS ENUM ('M', 'F', 'X');

CREATE TABLE enclosure_type (
    enclosure_type_id BIGINT GENERATED ALWAYS AS IDENTITY,
    type_name TEXT NOT NULL UNIQUE,
    PRIMARY KEY (enclosure_type_id)
);

CREATE TABLE species (
    species_id BIGINT GENERATED ALWAYS AS IDENTITY,
    species_name TEXT NOT NULL UNIQUE,
    is_carnivore BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (species_id)
);

CREATE TABLE dinosaur (
    dinosaur_id BIGINT GENERATED ALWAYS AS IDENTITY,
    species_id BIGINT NOT NULL,
    gender dinosaur_gender NOT NULL,
    colour VARCHAR(25) NOT NULL,
    PRIMARY KEY(dinosaur_id),
    FOREIGN KEY (species_id) REFERENCES species(species_id),
    CONSTRAINT no_chrome_lizards  CHECK (LOWER(colour) != 'chrome')
);

-- Adding master data

INSERT INTO species (species_name, is_carnivore) VALUES ('Tyrannosaurus Rex', TRUE);

INSERT INTO dinosaur (species_id, gender, colour) VALUES (1, 'F', 'Chrome');