from pathlib import Path

import pytest

HERE = Path(__file__).parent
TEST_DATA_ROOT = HERE.joinpath('..', '..', 'test_data')
TEST_CONFIGS_ROOT = TEST_DATA_ROOT.joinpath('configs')


@pytest.fixture
def train_config_audio_cbin_annot_notmat():
    return TEST_CONFIGS_ROOT.joinpath('test_train_audio_cbin_annot_notmat.toml')


@pytest.fixture
def train_config_spect_mat_annot_yarden():
    return TEST_CONFIGS_ROOT.joinpath('test_train_spect_mat_annot_yarden.toml')


@pytest.fixture
def predict_config():
    return TEST_CONFIGS_ROOT.joinpath('test_predict_audio_cbin_annot_notmat.toml')


@pytest.fixture
def invalid_section_config_path():
    return TEST_CONFIGS_ROOT.joinpath('invalid_section_config.toml')


@pytest.fixture
def invalid_option_config_path():
    return TEST_CONFIGS_ROOT.joinpath('invalid_option_config.toml')
