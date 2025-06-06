import azure.functions as func
import logging

app = func.FunctionApp()


@app.service_bus_queue_trigger(
    arg_name="message", queue_name="qa", connection="ServiceBusConnection"
)
@app.service_bus_queue_output(
    arg_name="response", queue_name="qb", connection="ServiceBusConnection"
)
def process(message: func.ServiceBusMessage, response: func.Out[str]):
    logging.info("processing")
    logging.info(message.get_body().decode("utf-8"))
    response.set("aa")
