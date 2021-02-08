import json
import gzip
import os

from biothings import config
logger = config.logger

def load_annotations(data_folder):
    json_path = os.path.join(data_folder, "data.json.gz")
    with gzip.open(json_path) as f:
        data = json.loads(f.read().decode('utf-8'))

    for datum in data:
        datum['_id'] = datum['gisaid_epi_isl']
        yield datum
