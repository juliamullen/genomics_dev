import os
import biothings, config
import datetime

biothings.config_for_app(config)

import biothings.hub.dataload.dumper

class GenomicsDumper(biothings.hub.dataload.dumper.DummyDumper):
    SRC_NAME = "genomics_parser"
    SRC_ROOT_FOLDER = os.path.join(config.DATA_ARCHIVE_ROOT, SRC_NAME)

    __metadata__ = {
        "src_meta": {
            "author": {
                "name": "Julia Mullen",
                "url":  "https://github.com/juliamullen"
                },
            "code": {
                "branch": "master",
                "repo": "https://github.com/juliamullen/genomics_parser"
                },
            #"url": "",
            #"license": "",
        }
    }

    SCHEDULE = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_release()

    def set_release(self):
        self.release = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
