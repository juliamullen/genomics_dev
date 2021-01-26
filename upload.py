import biothings.hub.dataload.uploader
import biothings
import config
import requests

biothings.config_for_app(config)

#MAP_URL = "https://raw.githubusercontent.com/SuLab/outbreak.info-resources/master/outbreak_resources_es_mapping.json"
#MAP_VARS = ["@type", "author", "curatedBy", "dateModified", "datePublished", "description", "distribution", "doi", "keywords", "@id", "funding", "identifier", "creator", "license", "name", "date"]

try:
    from genomics.parser  import load_annotations as parser_func
    from genomics.mapping import mapping_dict
except ImportError:
    from .parser  import load_annotations as parser_func
    from .mapping import mapping_dict

class GenomicsUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    main_source = "genomics_parser"
    name = "genomics_parser"

    __metadata__ = {
        "src_meta": {
            "author": {
                "name": "Julia Mullen",
                "url":  "https://github.com/juliamullen"
                },
            "code": {
                "branch": "main",
                "repo": "https://github.com/juliamullen/genomics_parser"
                },
            #"url": "",
            #"license": "",
        }
    }

    idconverter = None
    storage_class = biothings.hub.dataload.storage.BasicStorage

    def load_data(self, data_folder):
        if data_folder:
            self.logger.info("Load data from directory: '%s'", data_folder)
        return parser_func()

    @classmethod
    def get_mapping(klass):
        return mapping_dict
