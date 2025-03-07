"""Test that Psychrochart object is serializable."""

import pickle

from psychrochart import load_config, PsychroChart
from tests.conftest import store_test_chart, TEST_BASEDIR


def test_0_serialize_psychrochart():
    """Test the plot custom styling with JSON files/dicts."""
    path_svg = TEST_BASEDIR / "test_to_pickle.svg"
    chart = PsychroChart.create()
    chart.save(path_svg)
    (TEST_BASEDIR / "chart.pickle").write_bytes(pickle.dumps(chart))
    (TEST_BASEDIR / "chart.json").write_text(chart.model_dump_json(indent=2))

    assert (
        PsychroChart.model_validate_json(
            chart.model_dump_json()
        ).model_dump_json()
        == chart.model_dump_json()
    )


def test_1_unpickle_psychrochart():
    chart = pickle.loads((TEST_BASEDIR / "chart.pickle").read_bytes())
    path_svg = TEST_BASEDIR / "test_from_pickle.svg"
    chart.save(path_svg)


def test_1_load_json_psychrochart():
    chart = PsychroChart.model_validate_json(
        (TEST_BASEDIR / "chart.json").read_text()
    )
    path_svg = TEST_BASEDIR / "test_from_json.svg"
    chart.save(path_svg)


def test_2_compare_psychrocharts():
    chart_1 = (TEST_BASEDIR / "test_to_pickle.svg").read_text()
    chart_2 = (TEST_BASEDIR / "test_from_pickle.svg").read_text()
    chart_3 = (TEST_BASEDIR / "test_from_json.svg").read_text()
    assert len(chart_1) == len(chart_2) == len(chart_3)


def test_workflow_with_json_serializing():
    # Get a preconfigured style model and customize it
    chart_config = load_config("interior")
    chart_config.figure.dpi = 72
    chart_config.limits.range_temp_c = (18.0, 32.0)
    chart_config.limits.range_humidity_g_kg = (1.0, 40.0)
    chart_config.limits.altitude_m = 3000

    custom_chart = PsychroChart.create(chart_config)
    store_test_chart(custom_chart, "custom-chart-1.svg", png=True)

    # serialize the config for future uses
    assert (
        chart_config.model_dump_json() == custom_chart.config.model_dump_json()
    )
    (TEST_BASEDIR / "custom-chart-config.json").write_text(
        chart_config.model_dump_json()
    )
    # or even the full psychrochart
    (TEST_BASEDIR / "custom-chart.json").write_text(
        custom_chart.model_dump_json()
    )

    # reuse config
    custom_2 = PsychroChart.create(
        (TEST_BASEDIR / "custom-chart-config.json").as_posix()
    )
    store_test_chart(custom_2, "custom-chart-2.svg", png=True)

    # or reload chart from disk
    custom_3 = PsychroChart.model_validate_json(
        (TEST_BASEDIR / "custom-chart.json").read_text()
    )
    store_test_chart(custom_3, "custom-chart-3.svg", png=True)

    # anyway it produces the same psychrochart
    svg1 = (TEST_BASEDIR / "custom-chart-1.svg").read_text()
    svg2 = (TEST_BASEDIR / "custom-chart-2.svg").read_text()
    svg3 = (TEST_BASEDIR / "custom-chart-3.svg").read_text()
    assert svg1 == svg2 == svg3

    png1 = (TEST_BASEDIR / "custom-chart-1.png").read_bytes()
    png2 = (TEST_BASEDIR / "custom-chart-2.png").read_bytes()
    png3 = (TEST_BASEDIR / "custom-chart-3.png").read_bytes()
    assert png1 == png2 == png3
