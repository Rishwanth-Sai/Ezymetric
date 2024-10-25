import requests
from sqlalchemy import Table, Column, Integer, String, MetaData
from config import engine, session

metadata = MetaData()

leads = Table('leads', metadata,
              Column('lead_id', Integer, primary_key=True),
              Column('name', String),
              Column('email', String),
              Column('status', String))

campaigns = Table('campaigns', metadata,
                  Column('campaign_id', Integer, primary_key=True),
                  Column('name', String),
                  Column('impressions', Integer),
                  Column('clicks', Integer))

metadata.create_all(engine)

def fetch_data():
    lead_data = requests.get("http://127.0.0.1:5000/api/leads").json()
    campaign_data = requests.get("http://127.0.0.1:5000/api/campaigns").json()

    for lead in lead_data:
        session.execute(leads.insert().values(lead))

    for campaign in campaign_data:
        session.execute(campaigns.insert().values(campaign))

    session.commit()

if __name__ == "__main__":
    fetch_data()
