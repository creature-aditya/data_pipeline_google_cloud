from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "booking-dotcom-429013"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bqload-booking-com",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://hyper-bkt-booking-com-metadata/udf.js",
        "JSONPath": "gs://hyper-bkt-booking-com-metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "booking-dotcom-429013.booking.booking-com",
        "inputFilePattern": "gs://hyper-bkt-booking-com/hotel.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://hyper-bkt-booking-com-metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
