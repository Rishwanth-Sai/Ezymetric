import pandas as pd
import pdfkit
from config import session, leads, campaigns

def generate_csv():
    lead_df = pd.read_sql(session.query(leads).statement, session.bind)
    campaign_df = pd.read_sql(session.query(campaigns).statement, session.bind)

    lead_df.to_csv("leads_report.csv", index=False)
    campaign_df.to_csv("campaigns_report.csv", index=False)

def generate_pdf():
    html_content = "<h1>Lead Report</h1>"  
    pdfkit.from_string(html_content, "leads_report.pdf")

if __name__ == "__main__":
    generate_csv()
    generate_pdf()
