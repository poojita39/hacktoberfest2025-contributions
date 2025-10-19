import logging, datetime

logging.basicConfig(filename="app.log", level=logging.INFO)
def log_event(event):
    logging.info(f"{datetime.datetime.now()} - {event}")

def run_app():
    log_event("App started")
    try:
        x = 10 / 0
    except ZeroDivisionError:
        log_event("Error: Division by zero")
    log_event("App ended")

run_app()
