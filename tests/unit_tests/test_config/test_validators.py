import pytest
import toml

import vak.config.validators


class TestValidators:
    def test_are_sections_valid(self, invalid_section_config_path):
        with invalid_section_config_path.open('r') as fp:
            config_toml = toml.load(fp)
        with pytest.raises(ValueError):
            vak.config.validators.are_sections_valid(config_toml,
                                                     invalid_section_config_path)

    def test_are_options_valid(self, invalid_option_config_path):
        section_with_invalid_option = 'PREP'
        with invalid_option_config_path.open('r') as fp:
            config_toml = toml.load(fp)
        with pytest.raises(ValueError):
            vak.config.validators.are_options_valid(config_toml,
                                                    section_with_invalid_option,
                                                    invalid_option_config_path)
