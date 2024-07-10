import requests
import csv
from google.cloud import storage



url = "https://booking-com.p.rapidapi.com/v1/static/hotels"

querystring = {"country":"in"}

headers = {
	"x-rapidapi-key": "429ff63a74msha0e92ee4058e695p123368jsn751c8796acfe",
	"x-rapidapi-host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json().get('result', [])  
    csv_filename = 'hotel.csv'
    
    if data:
        field_names = ['hotel_id', 'name', 'city', 'address', 'hotel_class', 'url', 'ranking', 'number_of_rooms']  # Specify required field names

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")
    
        bucket_name = 'hyper-bkt-booking-com'
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data fetched from the API.")
else:
    print("Failed to fetch data:", response.status_code)