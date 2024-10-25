## Getting Started

First, enter your credentials in the .env file:

```bash
DATABASE_URI=postgresql://username:password@localhost:5432/postgres
use your postgresql account username and password

EMAIL_USER=youremail@example.com
use your postgresql account email

EMAIL_PASSWORD=yourpassword
use email password

```
in alerts.py
```bash
msg['From'] = 'youremail@example.com'
use your email
msg['To'] = 'recipient@example.com'
use the email of the recipient(where alert is received)

```

Running the Project:
1. Set up and activate the environment (if using a virtual environment).
2. Install dependencies with:
```bash
pip install -r requirements.txt
```
3. Run the Flask Server:
```bash
python app.py
```
4. Execute ETL and Reporting:
```bash
python etl.py       # Runs ETL to populate data
python report.py    # Generates CSV/PDF reports
```
5. Send Alerts:
```bash
python alerts.py
```


