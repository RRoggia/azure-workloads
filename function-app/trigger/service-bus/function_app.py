import os
import azure.functions as func
import logging

logger = logging.getLogger(__name__)

queue1_name = os.getenv("queue1_name", "queue1")
queue2_name = os.getenv("queue2_name", "queue2")
sb_read_connection = os.getenv("service_bus_read_connection_prefix", "ReadServiceBusConnection")
sb_write_connection = os.getenv("service_bus_write_connection_prefix", "WriteServiceBusConnection")

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.service_bus_queue_trigger(arg_name="body", queue_name=queue1_name, connection=sb_read_connection)
@app.service_bus_queue_output(arg_name="output", queue_name=queue2_name, connection=sb_write_connection)
def trigger_queue1(body: func.ServiceBusMessage, output: func.Out[str]):
    response = body.get_body().decode()
    logger.info(response)
    output.set(response)
