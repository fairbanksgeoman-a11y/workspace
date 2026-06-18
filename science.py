## This script requires that the asf-search python module is installed
## to install, run the following in a terminal
## `pip install asf-search`
## Then from the correct folder in your terminal run:
## `python asf-search-script-2026-06-18_01-21-15.py`
## 
## For more information, see the official documentation
## https://docs.asf.alaska.edu/asf_search/basics/
import asf_search as asf
import pprint

opts=asf.ASFSearchOptions(**{
    "maxResults": 250,
    "bbox": [
        -116.039883963679,
        42.19565399705729,
        -110.94222771367899,
        44.37068324141245
    ],
    "dataset": [
        "SLC-BURST"
    ]
})

## if the search requires authentication, uncomment
## the lines below, and enter your EDL credentials when prompted
## (use `session.auth_with_token(getpass('EDL Token'))` instead if a CMR bearer token is required)
# from get_pass import get_pass
# session=asf.ASFSession()
# session.auth_with_creds(input('EDL Username'), getpass('EDL Password'))
# opts.session = session

results=asf.search(opts=opts)
pprint.pp(results.geojson())

