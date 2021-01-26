import json

try:
    from biothings import config
    logger = config.logger
except ImportError:
    import logging
    logger = logging.getLogger('genomics')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('genomics_log.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def load_annotations():
    with open('/Users/julia/Desktop/test_data_model_2021-01-22_v3.json', 'r') as data_file:
        data = json.load(data_file)

    for datum in data:
        yield datum

if __name__ == "__main__":
    with open('transformed.json', 'w') as output:
        json.dump([i for i in load_annotations()], output)
