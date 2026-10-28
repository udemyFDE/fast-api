'''

This is the file to test the functionalities of main.py

need to import main.py

'''

from fastapi.testclient import TestClient

# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import main
# # to use a relative path can use the below import for main.py
# # based on the project structure
# from ..main import app

from fastapi import status

# app from main.py

# # if using <import main>
# # for my folder structure, this works
client = TestClient(main.app)

# # if using <from ..main import app>
# client = TestClient(app)



def test_return_health_check():
    response = client.get("/healthy")  # same endpoint defined for health check in main.py
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'Healthy'}
# # this may get a warning or error for httpx
# # pip install httpx2
