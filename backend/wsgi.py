import sys
import pathlib
# Ensure the backend folder is on the path
project_root = pathlib.Path(__file__).resolve().parent
sys.path.append(str(project_root))

from backend.app.main import app as application  # Gunicorn looks for "application"

