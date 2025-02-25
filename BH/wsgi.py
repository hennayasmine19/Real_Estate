import sys
import os

# Print current directory for debugging
print("Root directory:", os.getcwd())

# Add the correct paths to the Python path
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'BH'))

# Import your Flask app
from BH.server import app

# This is required for Vercel
application = app

if __name__ == "__main__":
    app.run()