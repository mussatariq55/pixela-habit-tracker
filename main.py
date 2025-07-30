import requests
from datetime import datetime
import os

# Get current date in YYYYMMDD format
DATE = datetime.now().strftime('%Y%m%d')

# Load Pixela credentials securely from environment variables
USERNAME = os.getenv("PIXELA_USERNAME", "your-username")
TOKEN = os.getenv("PIXELA_TOKEN", "your-token")  # Make sure to set this in your env

GRAPH = "graph1"

# Base Pixela API endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Step 1: Create a user account (run only once)
pixela_params = {
    "notMinor": "yes",
    "agreeTermsOfService": "yes",
    "username": USERNAME,
    "token": TOKEN
}
# Uncomment the next lines only to create account once
# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(f"Create Account Response: {response.text}")

# Step 2: Create a graph (run only once)
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# Uncomment the next lines only to create graph once
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(f"Create Graph Response: {response.text}")

# Step 3: Post a pixel (run every time you want to log a workout)
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}"

quantity = input("How many km did you cycle today? ")

pixel_data = {
    "date": DATE,
    "quantity": quantity
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

if response.status_code == 200 or response.status_code == 201:
    print("Pixel created successfully!")
else:
    print(f"Failed to create pixel: {response.status_code} - {response.text}")

# Optional Step 4: Update a pixel (if you need to correct data)
# update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}/{DATE}"
# new_pixel_data = {"quantity": "5"}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(f"Update Pixel Response: {response.text}")

# Optional Step 5: Delete a pixel
# delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}/{DATE}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(f"Delete Pixel Response: {response.text}")

