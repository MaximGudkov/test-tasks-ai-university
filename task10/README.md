### Quick start:

- `pip install -r requirements.txt` - install packages
- fill variables in .env
- create credentials.json file with you credentials
- `uvicorn src.main:app --reload`

### Usage:

- http://127.0.0.1:8000/github/{username} - get info about github user
- http://127.0.0.1:8000/add-to-sheet?username={username} - add info about user to sheet (this api is better check with swagger - http://127.0.0.1:8000/docs)
- http://127.0.0.1:8000/get-from-sheet - get info from sheet