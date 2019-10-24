import psutil

def process(logger) -> str:
    str_output = "CPU Usage: {0}\n".format(psutil.cpu_percent())
    str_output += "Memory Usage: {0}\n".format(psutil.virtual_memory())
    str_output += "Storage Usage: {0}\n".format(psutil.disk_usage("/"))

    logger.log("HealthCheck Request Inbounded.")

    return str_output