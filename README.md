# Booking.com data pipeline on google cloud services

Data pipeline bulding beween the source and destination with extraction, tranformation and loading the data into the analytical tool from where data analysis can be performed.
Architecture of this pipeline is as follows:

![Architecture](https://github.com/creature-aditya/data_pipeline_google_cloud/assets/83203134/ee606934-b891-4afe-b0a4-d7f2efe2196c)

Here I'm using Booking.com API from RapidAPI which provides the data of their hotels present in India. Using the python program (extract_and_push_gcs.py) it is fetching the data from the API and storing it into the cloud bucket (hyper-bkt-booking-com) as a csv file (hotel.csv).

**Objective of the pipeline:**
Not to loose data from our GCS storage and in case we lost then this project will automatically recollect all the data as per schedule.

Using the airflow composer DAG it keeps a checks everyday that the data is present in out bucket or not. If it is not present then it will runs the python script to extract and store the data from API to csv file. As soon as the file created and stored in the bucket, a cloud function is triggered which creates and run a dataflow job. Job named as booking-com-load has js user defined tranformation function and json BigQuery schema to store in  table (please not that the table is already created and it's location is provieded to the job).

![DF_job](https://github.com/creature-aditya/data_pipeline_google_cloud/assets/83203134/42db30c7-1d69-4bd1-b0f2-2d3bf54ec5f1)


As dataflow job ends suceessfully, it will store the transformed data into the given bigQuery table. Here we can write SQL queries on the table for analysis and generate meaningful insights. 

![bq_table_preview](https://github.com/creature-aditya/data_pipeline_google_cloud/assets/83203134/0dedcc4d-cfa0-48f5-99c1-77a3530fb756)


Looker studio is connected with the project output table from where it directly fetched the schema and data. we can apply filters based on datatypes and business requirements for analysis purposes. 
The report in the looker studio looks like this:

![looker_view](https://github.com/creature-aditya/data_pipeline_google_cloud/assets/83203134/3b62cb4d-053c-4722-b0b4-cec5aa5c0701)

Anyday if we lost data in our storage(bucket), on the next day DAG will run the above stated series of events and plots the data again in place.
