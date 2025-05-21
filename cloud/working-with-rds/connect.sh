source .env
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER $DB_NAME