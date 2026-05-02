import os


DB_CONFIG = {
    "host": os.getenv("PGHOST", "localhost"),
    "port": int(os.getenv("PGPORT", "5432")),
    # Practice 7 uses the same schema as TSIS1, but the default database name
    # is separate so tests/demo data do not overwrite the original TSIS1 DB.
    "database": os.getenv("PGDATABASE", "phonebook_practice7"),
    "user": os.getenv("PGUSER", "postgres"),
    "password": os.getenv("PGPASSWORD", "12345"),
}
