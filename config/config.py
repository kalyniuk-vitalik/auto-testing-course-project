import os

# --- Database -----------------------------------------------------------
# Set the absolute path to data_base.db on your machine,
# or keep the relative path if running from the project root
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data_base.db")

# --- Selenium -----------------------------------------------------------
WAIT_TIMEOUT = 10          # seconds for WebDriverWait

# --- GitHub API ---------------------------------------------------------
GITHUB_API_BASE_URL = "https://api.github.com"

# --- Test URLs ----------------------------------------------------------
GITHUB_LOGIN_URL  = "https://github.com/login"
ANSWEAR_LOGIN_URL = "https://answear.ua/mii-akkaunt/uviity"
