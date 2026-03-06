# Data Model

## companies

| Column     | Type           | Constraints                |
|------------|----------------|----------------------------|
| id         | INTEGER        | PK, autoincrement          |
| name       | VARCHAR(255)   | NOT NULL                   |
| street     | VARCHAR(255)   | NOT NULL                   |
| city       | VARCHAR(100)   | NOT NULL                   |
| state      | VARCHAR(100)   | NOT NULL                   |
| zip_code   | VARCHAR(20)    | NOT NULL                   |
| country    | VARCHAR(100)   | NOT NULL                   |
| billing    | NUMERIC(12,2)  | NOT NULL, default 0        |
| expenses   | NUMERIC(12,2)  | NOT NULL, default 0        |
| employees  | INTEGER        | NOT NULL, default 0        |
| clients    | INTEGER        | NOT NULL, default 0        |
| created_at | TIMESTAMP      | NOT NULL, default now()    |
| updated_at | TIMESTAMP      | NOT NULL, default now()    |

`profit` is computed as `billing - expenses` at the application/presentation layer, not stored in the database.
