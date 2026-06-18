## This script requires that the asf-search python module is installed
## to install, run the following in a terminal
## `pip install asf-search`
## Then from the correct folder in your terminal run:
## `python asf-search-script-2026-06-18_01-36-37.py`
##
## For more information, see the official documentation
## https://docs.asf.alaska.edu/asf_search/basics/
import pprint

import asf_search as asf

opts = asf.ASFSearchOptions(
    **{
        "maxResults": 250,
        "beamSwath": ["IW"],
        "flightDirection": "DESCENDING",
        "platform": ["SC"],
        "polarization": ["HH+HV"],
        "end": "2025-12-24T04:59:59Z",
        "dataset": ["SENTINEL-1"],
    }
)










results = asf.search(opts=opts)
pprint.pp(results.geojson())
