import json
import azure.functions as func
import logging
import httpx

app = func.FunctionApp()


@app.service_bus_queue_trigger(
    arg_name="message", queue_name="qa", connection="ServiceBusConnection"
)
@app.service_bus_queue_output(
    arg_name="response", queue_name="qb", connection="ServiceBusConnection"
)
def process(message: func.ServiceBusMessage, response: func.Out[str]):
    logging.info("processing")
    body = message.get_body().decode("utf-8")
    logging.info(body)
    try:
        httpRes = httpx.get(
            f"https://roggia-as-fzh8avafepc3f8cm.eastus-01.azurewebsites.net/{body}"
        )
        if httpRes.status_code == 200:
            logging.info("success bro")
            response.set(json.dumps(httpRes.json()))
        else:
            logging.info("failed")
            raise Exception("system failed")

    except Exception as err:
        logging.info(err)
        logging.info("failed")
        raise Exception("system failed")
