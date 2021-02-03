mapping_dict = {
    "nextstrain_clade": {
        "type": "keyword",
        "normalizer": "keyword_lowercase_normalizer"
    },
    "submitting_lab": {
        "type": "keyword"
    },
    "genbank_accession": {
        "type": "keyword"
    },
    "mutations": {
        "type": "nested",
        "properties": {
            "type": {
                "type": "keyword"
            },
            "mutation": {
                "type": "keyword"
            },
            "gene": {
                "type": "keyword"
            },
            "ref_codon": {
                "type": "keyword"
            },
            "pos": {
                "type": "keyword"
            },
            "alt_codon": {
                "type": "keyword"
            },
            "is_synonymous": {
                "type": "keyword"
            },
            "ref_aa": {
                "type": "keyword"
            },
            "codon_num": {
                "type": "keyword"
            },
            "alt_aa": {
                "type": "keyword"
            },
            "absolute_coords": {
                "type": "keyword"
            },
            "change_length_nt": {
                "type": "keyword"
            },
            "nt_map_coords": {
                "type": "keyword"
            },
            "aa_map_coords": {
                "type": "keyword"
            }
        }
    },
    "division": {
        "type": "keyword",
        "normalizer": "keyword_lowercase_normalizer"

    },
    "country": {
        "type": "keyword",
        "normalizer": "keyword_lowercase_normalizer"

    },
    "gisaid_clade": {
        "type": "keyword"
    },
    "date_submitted": {
        "type": "keyword"
    },
    "originating_lab": {
        "type": "keyword"
    },
    "date_collected": {
        "type": "keyword"
    },
    "date_modified": {
        "type": "keyword"
    },
    "country_id": {
        "type": "keyword"
    },
    "authors": {
        "type": "keyword"
    },
    "pangolin_lineage": {
        "type": "keyword",
        "normalizer": "keyword_lowercase_normalizer"

    },
    "location": {
        "type": "keyword"
    },
    "division_id": {
        "type": "keyword"
    },
    "purpose_of_sequencing": {
        "type": "keyword"
    },
    "gisaid_epi_isl": {
        "type": "keyword"
    },
    "strain": {
        "type": "keyword"
    }
}
