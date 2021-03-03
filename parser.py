import json
import gzip
import os

from biothings import config
logger = config.logger

def load_annotations(data_folder):
    json_path = os.path.join(data_folder, "new_api_data.json.gz")
    with gzip.open(json_path) as f:
        data = json.loads(f.read().decode('utf-8'))
    for _id, datum in enumerate(data):
        datum['_id'] = _id
        yield datum
