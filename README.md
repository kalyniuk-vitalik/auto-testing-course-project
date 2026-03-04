A training project on automated software testing, created as part of the course  
**"Automated Software Testing"** by [Prometheus](https://prometheus.org.ua) in partnership with **GlobalLogic**.

---

## About the Project

The project covers three main areas of automated testing:

| Area | Technologies | Folder |
|---|---|---|
| UI Testing | Selenium WebDriver, Page Object Model | `tests/ui/` |
| API Testing | requests, pytest | `tests/api/` |
| Database Testing | SQLite3 | `tests/database/` |

---

## Project Structure

```
auto-testing-course/
│
├── config/
│   └── config.py                   # Project configuration (URLs, timeouts)
│
├── module/
│   ├── api/
│   │   └── clients/
│   │       └── github.py           # HTTP client for GitHub API
│   │
│   ├── common/
│   │   └── database.py             # Class for working with SQLite DB
│   │
│   └── ui/
│       └── page_objects/
│           ├── base_page.py            # Base class for all pages
│           ├── github_sign_in_page.py  # Page Object — GitHub login
│           └── answear_sign_in_page.py # Page Object — Answear login
│
├── tests/
│   ├── api/
│   │   └── test_github_api.py      # GitHub API tests
│   │
│   ├── database/
│   │   └── test_database.py        # Database tests
│   │
│   └── ui/
│       ├── test_ui.py                  # UI tests without Page Object (basic level)
│       ├── test_ui_page_object.py      # UI tests with Page Object (GitHub)
│       └── test_answear_page_object.py # UI tests with Page Object (Answear)
│
├── conftest.py        # Global pytest fixtures
├── data_base.db       # SQLite database
├── pytest.ini         # pytest configuration (markers)
├── requirements.txt   # Project dependencies
└── README.md
```

---

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/kalyniuk-vitalik/auto-testing-course.git
cd auto-testing-course
```

### 2. Create a virtual environment
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the project
Open `config/config.py` and set the correct path to `data_base.db`:
```python
DB_PATH = "/your/path/to/data_base.db"
```

### 5. Install ChromeDriver
Make sure [ChromeDriver](https://chromedriver.chromium.org/downloads) is installed  
and its version matches your installed version of Google Chrome.

---

## Running Tests

### All tests
```bash
pytest
```

### By marker
```bash
pytest -m api        # API tests only
pytest -m database   # database tests only
pytest -m ui         # UI tests only
pytest -m http       # HTTP tests only
```

### With console output
```bash
pytest -v -s
```

### Specific file
```bash
pytest tests/api/test_github_api.py -v
```

---

## Pytest Markers

| Marker | Description |
|---|---|
| `@pytest.mark.api` | GitHub API tests via client |
| `@pytest.mark.http` | Direct HTTP requests via requests |
| `@pytest.mark.database` | SQLite database tests |
| `@pytest.mark.ui` | Selenium UI tests |
| `@pytest.mark.check` | Fixture and user object checks |
| `@pytest.mark.change` | Object state change tests |

---

## Key Concepts Covered

- **pytest fixtures** — setup/teardown via `conftest.py`
- **Page Object Model (POM)** — pattern for UI tests
- **WebDriverWait + Expected Conditions** — explicit waits in Selenium
- **HTTP client** — working with REST API via `requests`
- **SQLite** — interacting with a relational database in tests
- **pytest markers** — grouping and filtering tests

---

## Requirements

- Python 3.8+
- Google Chrome (latest version)
- ChromeDriver (matching version)
- SQLite3 (built into Python)

---

## Course

This project is the practical part of the course  
**"Automated Software Testing"**  
by [Prometheus](https://prometheus.org.ua) in partnership with GlobalLogic.
