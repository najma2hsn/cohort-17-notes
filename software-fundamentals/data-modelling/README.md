# Data modelling

"Designing how we store the data"

## Relational data

- Entities : A table containing data about a type of thing
- Row : An individual example of an entity
- Fields : A column containing one piece of information for each row about the entity
- Value : A single piece of information (e.g. a number for a row in a field)
- Relationships : A connection between two entities

## Normalisation

data --> refine/restructure it

## 1NF

- No duplicate rows
- No lists/tables inside values
- No non-atomic values (depend on purpose)


## Challenge

Design an entity-relationship diagram in 3NF

- Gnomes live in mushroom houses
- 3-4 gnomes can live in a house
- Gnomes always wear hats, and they are very possessive of their own hats
- Gnomes ride forest animals to work (toads, frogs, bats)
- Forest animals refuse to have more than one rider
- Gnomes might have several animals for different jobs