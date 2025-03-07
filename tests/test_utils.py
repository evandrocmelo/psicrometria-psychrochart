"""Tests utilities."""

import json
import logging

from psychrochart.__main__ import main
from psychrochart.chart_entities import make_item_gid
from psychrochart.models.parsers import DEFAULT_CHART_CONFIG_FILE, load_config
from psychrochart.util import mod_color
from tests.conftest import TEST_BASEDIR

_PATH_CONFIG_UPDATE = str(
    TEST_BASEDIR.parent / "test_chart_config_update.json"
)


def test_load_plot_config():
    """Test the plot custom styling with JSON files/dicts."""
    # Test load default config
    default_config = load_config()

    # Test passing dict vs JSON path:
    config_2 = load_config(config=DEFAULT_CHART_CONFIG_FILE)
    config_3 = load_config(
        config=json.loads(DEFAULT_CHART_CONFIG_FILE.read_text())
    )
    assert config_2 == config_3

    # Test update config:
    config_custom = load_config(config=_PATH_CONFIG_UPDATE)
    assert default_config.model_dump() != config_custom.model_dump()
    assert "constant_h" in config_custom.model_dump()
    assert "constant_v" in config_custom.model_dump()
    assert "test_fake_param" not in config_custom.model_dump()

    # Test config styles:
    default_config_s = load_config(config="default")
    assert default_config == default_config_s

    ashrae_config_s = load_config(config="ashrae")
    assert default_config != ashrae_config_s


def test_cli_main():
    """Unit test for the CLI entry point."""
    main()


def _to_8bit_color(color):
    return tuple(
        int(round(255 * c)) if i < 3 else c for i, c in enumerate(color)
    )


def test_color_palette():
    """Test rgba utilities."""
    color_base = [0.475, 0.612, 0.075]
    assert _to_8bit_color(color_base) == (121, 156, 19)

    color_light_20 = mod_color(color_base, 20)
    assert _to_8bit_color(color_light_20) == (145, 187, 23)

    color_dark_40 = mod_color(color_base, -40)
    assert _to_8bit_color(color_dark_40) == (73, 94, 11)

    color_alpha_08 = mod_color(color_base, 0.8)
    assert _to_8bit_color(color_alpha_08) == (121, 156, 19, 0.8)


def test_gid_generator(caplog):
    with caplog.at_level(logging.WARNING):
        assert make_item_gid("kind", name="name") == make_item_gid(
            "kind", name="name"
        )
        assert len(caplog.messages) == 0
        # unnamed items have random suffixes (and emit logging warnings)
        assert make_item_gid("kind", "family_label") != make_item_gid(
            "kind", "family_label"
        )
        assert len(caplog.messages) == 2
        caplog.clear()

    # !note: even different names can generate same gid
    gid1 = make_item_gid("kind", name=f"{-5.1}")
    gid2 = make_item_gid("kind", name=f"{5.1}")
    assert gid1 == gid2
