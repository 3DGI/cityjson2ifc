from pathlib import Path
import urllib.request
import gzip
import shutil

import pytest

from cityjson2ifc_cli.cli import load_cityjson


@pytest.fixture(scope='session')
def data_dir():
    tests_dir = Path(__file__).resolve().parent
    yield tests_dir / "data"


@pytest.fixture(scope='session')
def tmp_dir(data_dir):
    yield data_dir / "tmp"


def download_model(data_dir, filename):
    path_model = data_dir / filename
    if not path_model.exists():
        print(f"Downloading {filename}")
        result = urllib.request.urlretrieve(
            url=f"https://data.3dgi.xyz/cityjson2ifc/{filename}.gz",
            filename=path_model.with_suffix(".gz")
        )
        with gzip.open(result[0], "rb") as f_in:
            with path_model.open("wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        Path(result[0]).unlink()
    return path_model


@pytest.fixture(scope="session")
def input_model_5907_path(data_dir):
    """3D BAG v21.09.08, tile 5907 subset"""
    return download_model(data_dir, "3dbag_v210908_fd2cee53_5907_subset.json")


@pytest.fixture(scope="function")
def input_model_5907(input_model_5907_path):
    """3D BAG v21.09.08, tile 5907 subset"""
    with input_model_5907_path.open("r") as fo:
        return load_cityjson(fo, ignore_duplicate_keys=True)


@pytest.fixture(scope="session")
def input_model_68dn2_path(data_dir):
    """3D Basisvoorziening, tile 68dn2 subset file"""
    return download_model(data_dir, "68dn2_04_sub.json")


@pytest.fixture(scope="function")
def input_model_68dn2(input_model_68dn2_path):
    """3D Basisvoorziening, tile 68dn2 subset citymodel"""
    with input_model_68dn2_path.open("r") as fo:
        return load_cityjson(fo, ignore_duplicate_keys=True)


@pytest.fixture(scope="session")
def input_model_22ci3_path(data_dir):
    """3D Basisvoorziening, tile 22ci3 subset file"""
    return download_model(data_dir, "22ci3.city.json")


@pytest.fixture(scope="function")
def input_model_22ci3(input_model_22ci3_path):
    """3D Basisvoorziening, tile 22ci3 subset citymodel"""
    with input_model_22ci3_path.open("r") as fo:
        return load_cityjson(fo, ignore_duplicate_keys=True)
