from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Define the SmartPiXL API endpoint
API_ENDPOINT = "https://api.smartpixl.com/data"  # Replace with the actual API endpoint

# Define the mandatory parameters for the API request
params = {
    "CompanyId": "123",  # Replace with the actual Company ID number
    "PiXLId": "1",  # Replace with the actual PiXL ID number
    "Startdate": "2022-09-01",  # Replace with the actual start date
    "Enddate": "2022-09-30",  # Replace with the actual end date
    "UserTokenId": "YourUserTokenID"  # Replace with the actual User Token ID
}

@app.route('/')
def home():
    # Make an API request to the SmartPiXL API
    response = requests.get(API_ENDPOINT, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        
        # Visualize the data (adjust according to the actual data structure)
        plt.figure(figsize=(10,6))
        # Example: plt.plot(data['x'], data['y'])
        plt.title('SmartPiXL Data Visualization')
        
        # Encode the plot to PNG
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        
        return render_template('home.html', plot_url=plot_url)
    else:
        # Handle API request failure
        return render_template('error.html', error_message="Failed to retrieve data from SmartPiXL API.")

if __name__ == '__main__':
    app.run(debug=True)
