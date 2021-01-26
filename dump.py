import os
import biothings, config

biothings.config_for_app(config)

import biothings.hub.dataload.dumper

class GenomicsDumper(biothings.hub.dataload.dumper.DummyDumper):
    SRC_NAME = "genomics"
    SRC_ROOT_FOLDER = os.path.join(config.DATA_ARCHIVE_ROOT, SRC_NAME)

    __metadata__ = {
        "src_meta": {
            "author": {
                "name": "Julia Mullen",
                "url":  "https://github.com/juliamullen"
                },
            "code": {
                "branch": "master",
                "repo": "https://github.com/juliamullen/genomics"
                },
            #"url": "",
            #"license": "",
        }
    }

    SCHEDULE = None
