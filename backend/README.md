# Django + PostgreSQL backend

## Prerequisites

- **Docker Engine**
- **Docker Compose v2** plugin

## Setup
first setup .env file

use example_env

or look at the shared drive for mine

*might need to use sudo*

docker compose build

docker compose up

*check http://localhost:8000/ to confirm it worked*

## Useful Commands

- **docker compose down** (stop everything)
- **docker compose up** (start)

- **docker exec -it postgres psql -U postgres** (access area to run postgres commands)
- **\c <database_name>** *just do \c for default db* (enter a database)
- **\d** (view stuff in the db you entered)
- **\d+ <table_name>**
- **\q** (quit)

- **docker exec -it django bash** (enter container for the backend)
- run commands for django here and other related stuff

## Tips
- NEVER run pip install ....   instead add it to requirements.txt
- Don't run django commands outside of the docker container (explanation on how to enter in commands section)

## Models

### Accounts
```mermaid
erDiagram
    USER {
        UUID id PK
        string email
        string username
        string first_name
        string last_name
        string visibility
        smallint xp
        smallint level
        smallint xpneeded
        string school
        smallint grad_year
        string major
        string discord
        string instagram
        string github
        string linkedin
        text bio
        json blocked
        datetime updated_at
        datetime date_joined
    }

    SKILL {
        int id PK
        string name
    }

    INTEREST {
        int id PK
        string name
    }

    USER ||--o{ USER_SKILLS : "has"
    SKILL ||--o{ USER_SKILLS : "used by"

    USER ||--o{ USER_INTERESTS : "has"
    INTEREST ||--o{ USER_INTERESTS : "chosen by"

    USER_SKILLS {
        UUID user_id FK
        int skill_id FK
    }

    USER_INTERESTS {
        UUID user_id FK
        int interest_id FK
    }
```
