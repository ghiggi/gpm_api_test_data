# GPM-API Test Data

This repository stores the test data required by the unit-tests of the [gpm_api](https://github.com/ghiggi/gpm_api) package.

## Test Granule Generation

To generate small files for each GPM product, run the script ``generate_test_granule_data.py`` within the ``/scripts`` directory with:
 
```bash

python generate_test_granule_data.py

```

The script downloads the GPM products, cuts the granules data and saves the corresponding GPM-API netCDFs into the ``granules`` directory.

## Update Test Granules 

To update the netCDF test granules, run the script ``update_processed_test_data.py``within the ``/scripts`` directory with:

```bash

python update_processed_test_data.py

```

## Test Plot Images 

The ``plots`` directory contains test images to be compared by those generated by the GPM-API unit tests.
To regenerate or update a test image, manually delete it from the `plots/` directory and re-execute the GPM-API tests units.

## Documentation 

Further documentation on the GPM-API software is available at [https://gpm-api.readthedocs.io/](https://gpm-api.readthedocs.io/).

Additional information on how to synchronize the `gpm_api_test_data` repository with the GPM-API software is provided in the [Contributors Guidelines](https://gpm-api.readthedocs.io/en/latest/06_contributors_guidelines.html#contributing-to-test-data) section of the GPM-API documentation. 

