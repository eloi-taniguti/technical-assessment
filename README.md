# Technical Assessment

Test project using Playwright Python to run UI tests against a mock data quality application.

---

## Stack
* **Python:** 3.10.6+
* **pytest:** 7.4.4+
* **Playwright:** 1.40.0+

---

## Setup & Installation

### 1. Install Python
Ensure you have Python 3.10.6 or higher installed on your machine.
* **Download**: Get the installer from the official [python.org](https://python.org) website.
* **Verify installation**: Open your terminal and run:
  ```bash
  python --version
  ```

### 2. Install Dependencies & Playwright
Install the testing framework packages and download the browser binaries required by Playwright to run tests:
```bash
# Install Python dependencies
pip install pytest playwright pytest-playwright

# Install Playwright browser binaries
playwright install
```
---

## Running the Application
Before executing the tests, you must start the mock application server locally:
```bash
cd app
python -m http.server 8080
```
The application will be accessible at `http://localhost:8080`. Keep this terminal window running.

---

## Running the Tests
Open a **new terminal window** and run the test suite:

```bash
# Run all tests headlessly (in the background)
pytest

# Run tests in headed mode (opens a visible browser window)
pytest --headed
```

---

## Executing from CI
To run tests remotely using GitHub Actions:
1. Navigate to the **Actions** tab in your GitHub repository.
2. Select the **"Run Python Project"** workflow from the left sidebar.
3. Click the **"Run workflow"** dropdown menu on the right.
4. Select your target branch and click the green **"Run workflow"** button.
