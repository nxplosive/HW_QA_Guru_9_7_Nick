import os
import pytest
import shutil
from script_os import RESOURCES_DIR, ARCHIVE, CURRENT_DIR


@pytest.fixture
def zip_creation():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)
    if os.path.isfile(ARCHIVE):
        os.remove(ARCHIVE)

    return ARCHIVE

    # shutil.rmtree(os.path.join(CURRENT_DIR, "resources"))
