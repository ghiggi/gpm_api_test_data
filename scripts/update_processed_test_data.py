import glob
import os

import gpm
from gpm import _root_path

# from tqdm import tqdm
from gpm.io.products import available_scan_modes

RAW_DIRNAME = "raw"
CUT_DIRNAME = "cut"
PROCESSED_DIRNAME = "processed"

VERSIONS = [7, 6]
PRODUCT_TYPES = ["RS"]

gpm.config.set(
    {
        "warn_non_contiguous_scans": False,
        "warn_non_regular_timesteps": False,
        "warn_invalid_geolocation": False,
    },
)

###############################################################################
## Test directory structure
# .../gpm/tests/data/granules/
# <CUT>/<product_type>/<version>/<product>/<filename.hdf5>)
# <PROCESSED>/<product_type>/<version>/<product>/<scan_mode>.nc)

###############################################################################


granules_dir_path = os.path.join(_root_path, "gpm", "tests", "data", "granules")
cut_dir_path = os.path.join(granules_dir_path, "cut")

for product_type in PRODUCT_TYPES:
    if product_type == "RS":
        cut_filepaths = glob.glob(os.path.join(cut_dir_path, "RS", "*", "*", "*"))
    else:
        cut_filepaths = glob.glob(os.path.join(cut_dir_path, "NRT", "*", "*"))

    for cut_filepath in cut_filepaths:
        version_str, product = cut_filepath.split(os.sep)[-3:-1]
        version = int(version_str[1])
        product_info = f"{product_type} {product} {version_str} product"

        # Create the processed netCDF
        print(f"Create {product_info} netCDF")
        scan_modes = available_scan_modes(product=product, version=version)
        processed_dir_path = os.path.dirname(cut_filepath).replace(
            CUT_DIRNAME,
            PROCESSED_DIRNAME,
        )
        os.makedirs(processed_dir_path, exist_ok=True)
        for scan_mode in scan_modes:
            processed_filepath = os.path.join(processed_dir_path, f"{scan_mode}.nc")
            if os.path.exists(processed_filepath):
                os.remove(processed_filepath)
            try:
                ds = gpm.open_granule_dataset(
                    cut_filepath,
                    scan_mode=scan_mode,
                ).compute()
                ds.close()
                ds.to_netcdf(processed_filepath)
            except Exception as e:
                print(
                    f"Failed to process {product_info} with scan mode {scan_mode}: {e}",
                )
