# Remove all data files and directory
rm -rf ./data

psql -c "DROP DATABASE template1"
psql -c "CREATE DATABASE template1"
psql template1 -f schema.sql -f seed.sql