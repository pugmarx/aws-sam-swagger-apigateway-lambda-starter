import logging

def handler(event, context):
    logging.info("--- postPet handler ---")
    return event