from azure.identity import ManagedIdentityCredential
from azure.storage.blob import BlobServiceClient
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()
logger = logging.getLogger(__name__)


@app.route(route="ok", methods=[func.HttpMethod.GET])
def ok(req: func.HttpRequest):
    return func.HttpResponse("ok")


@app.route(route="test", methods=[func.HttpMethod.GET])
async def get_test(req: func.HttpRequest) -> func.HttpResponse:
    print("received call")
    logger.info("received call")
    try:
        credentials = ManagedIdentityCredential(
            client_id="f74f555c-5df3-4134-9a95-08301bc6e050"
        )

        account_url = "https://roggiatest.blob.core.windows.net"
        blob_service_client = BlobServiceClient(account_url, credential=credentials)
        container_client = blob_service_client.get_blob_client(
            container="demo-docs", blob="README.md"
        )

        with open("README.md") as file:
            content = file.read()
            print(content)
            container_client.upload_blob(data=content, overwrite=True)

        return func.HttpResponse("ok")
    except Exception as e:
        logger.info(e)
        print(e)
        return func.HttpResponse(str(e))
