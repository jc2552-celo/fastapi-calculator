# FastAPI Calculator

This is a FastAPI-based calculator application with basic arithmetic operations and full test coverage.

## Features
- Add, subtract, multiply, divide endpoints
- Unit tests for logic functions
- Integration tests for API routes
- GitHub Actions CI workflow
- Playwright-ready for end-to-end testing

## Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/jc2552-celo/fastapi-calculator.git
   cd fastapi-calculator

Create virtual environment and install dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Start server:

bash
Copy code
uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000/docs

Run Tests
bash
Copy code
PYTHONPATH=. pytest
CI/CD
GitHub Actions automatically runs tests on each push to main.

yaml
Copy code

---

#### 💾 3. Save and exit:
- Press `CTRL + O`, then `ENTER` to save  
- Press `CTRL + X` to exit

---

### 🔁 4. Commit and push it to GitHub:

```bash
git add README.md
git commit -m "Add README.md for FastAPI calculator project"
git push origin main
