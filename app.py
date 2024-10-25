from flask import Flask, jsonify, request, send_file
import json
import os

app = Flask(__name__)

# Dummy data to simulate CRM and Marketing data
dummy_lead_data = [{"lead_id": 1, "name": "John", "email": "john@example.com", "status": "active"}]
dummy_campaign_data = [{"campaign_id": 1, "name": "Fall Sale", "impressions": 1000, "clicks": 50}]

@app.route('/api/leads', methods=['GET'])
def get_leads():
    return jsonify(dummy_lead_data)

@app.route('/api/campaigns', methods=['GET'])
def get_campaigns():
    return jsonify(dummy_campaign_data)

if __name__ == "__main__":
    app.run(debug=True)
