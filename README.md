# 🧮 FastAPI Calculator with PostgreSQL and Docker

This project demonstrates a simple FastAPI application integrated with PostgreSQL using Docker Compose. The API supports basic user and product data operations, and includes a working pgAdmin interface for database administration.

---

## 📦 Project Structure

fastapi-calculator/
├── docker-compose.yml
├── fastapi_app/
│ ├── init.py
│ ├── main.py
│ ├── crud.py
│ ├── models.py
│ ├── schemas.py
│ └── database.py
├── sql/
│ ├── create_tables.sql
│ ├── insert_data.sql
│ └── select_queries.sql
├── pgadmin/
│ └── (pgAdmin configs if any)
└── README.md


---

## 🚀 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/jc2552-celo/fastapi-calculator.git
cd fastapi-calculator

2. Launch Docker Environment
bash
Copy code
docker-compose up --build
This will start:

FastAPI app on http://localhost:8000

pgAdmin on http://localhost:5050 (Login: admin@example.com / Password: admin)

PostgreSQL on port 5432

3. Interact with the API
Open in browser:

bash
Copy code
http://localhost:8000/docs
Use Swagger UI to test endpoints like:

GET /users

GET /products

POST /users

POST /products

🛠️ SQL Files
create_tables.sql: Creates users and products tables.

insert_data.sql: Adds example users and products.

select_queries.sql: Fetches all data from both tables.

🧠 Technologies Used
FastAPI

PostgreSQL

Docker + Docker Compose

pgAdmin

SQL (DDL + DML)

👤 Author
Jason Codiot
GitHub: jc2552-celo

📂 GitHub Repo Link
🔗 https://github.com/jc2552-celo/fastapi-calculator

---

