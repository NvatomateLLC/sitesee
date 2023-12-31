from flask import Flask, render_template
import requests
import json
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Define the base URL and UserTokenID
base_url = "https://smartpixl.tech/Api2.0/CreatePiXL"
user_token_id = "w3mEBSaqhNiHj5XhKhzS4JhhVcbyJIqWAdw"

# Define the model data (replace with actual model data)
model_data = {
    "CompanyId": "12406",  # Replace with your actual Company ID
    "PiXLId": "29",  # Replace with your actual PiXL ID
    "Startdate": "2023-09-01",  # Replace with your actual start date
    "Enddate": "2023-09-30",  # Replace with your actual end date


    "UserTokenId": "w3mEBSaqhNiHj5XhKhzS4JhhVcbyJIqWAdw",  # Replace with your actual User Token ID
    # Include any other parameters as required by the API
    "Query": "YourQuery",  # Optional: Replace with your actual query if applicable
    "ProspectType": "O"  # Optional: Replace with your actual Prospect Type if applicable
}


@app.route('/')
def home():
    # Construct the full URL
    url = f"{base_url}/{user_token_id}"
    
    # Convert model data to JSON
    json_data = json.dumps(model_data)
    
    # Set the headers for the request
    headers = {
        "Content-Type": "application/json"
    }
    
    # Make a POST request to the API
    response = requests.post(url, data=json_data, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        # Process the result and render the appropriate template
        return render_template('success.html', result=result)
    else:
    # Print the status code and response content for debugging
        print("Status Code:", response.status_code)
    print("Response Content:", response.content)
    # Handle API request failure and render an error template
    return render_template('error.html', error_message="Failed to make API request.")


if __name__ == '__main__':
    app.run(debug=True)