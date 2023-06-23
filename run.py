from MSapp import app
import os
from dotenv import load_dotenv

load_dotenv()

# Access environment variables
env_var = os.getenv('FLASK_APP')


# this file is the entry point for the application, it will run the app by importing the app object from the MSapp module
# this line will run the app, will run only if module is directly run and not as an import from another module
if __name__ == '__main__':
    print("I am being run directly (inside run.py), not as an import from another module")
    app.run(port=5002, debug=True) # had to run on port 5001 because Mac OSX Monterey (12.x) currently uses ports 5000 and 7000, causes issues sometimes