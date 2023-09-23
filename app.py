from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def home():
    # Make an API request
    response = requests.get('API_URL')  # Replace 'API_URL' with the actual URL of the API you are using
    data = response.json()  # Assume the response is in JSON format
    
    # Visualize the data
    plt.figure(figsize=(10,6))
    # Adjust the plotting according to the structure of the API data
    plt.plot(data['x'], data['y'])  # Assume the data has 'x' and 'y' values
    plt.title('API Data Visualization')
    
    # Encode the plot to PNG
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return render_template('home.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
