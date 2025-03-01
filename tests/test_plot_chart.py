"""Tests plotting."""

import numpy as np

from psychrochart import PsychroChart
from tests.conftest import store_test_chart

# fmt: off
TEST_EXAMPLE_ZONES = [
    {
        "label": "Summer",
        "points_x": [23, 28],
        "points_y": [40, 60],
        "style": {
            "edgecolor": [1.0, 0.749, 0.0, 0.8],
            "facecolor": [1.0, 0.749, 0.0, 0.2],
            "linestyle": "--",
            "linewidth": 2,
        },
        "zone_type": "dbt-rh",
    },
    {
        "label": "Winter",
        "points_x": [18, 23],
        "points_y": [35, 55],
        "style": {
            "edgecolor": [0.498, 0.624, 0.8],
            "facecolor": [0.498, 0.624, 1.0, 0.2],
            "linestyle": "--",
            "linewidth": 2,
        },
        "zone_type": "dbt-rh",
    },
]
TEST_EXAMPLE_FIG_CONFIG = {
    "figsize": [16, 9],
    "partial_axis": True,
    "position": [0, 0, 1, 1],
    "title": None,
    "x_axis": {
        "color": [0.855, 0.145, 0.114],
        "linestyle": "-",
        "linewidth": 2,
    },
    "x_axis_labels": {"color": [0.855, 0.145, 0.114], "fontsize": 10},
    "x_axis_ticks": {
        "color": [0.855, 0.145, 0.114],
        "direction": "in",
        "pad": -20,
    },
    "x_label": None,
    "y_axis": {
        "color": [0.0, 0.125, 0.376],
        "linestyle": "-",
        "linewidth": 2,
    },
    "y_axis_labels": {"color": [0.0, 0.125, 0.376], "fontsize": 10},
    "y_axis_ticks": {
        "color": [0.0, 0.125, 0.376],
        "direction": "in",
        "pad": -20,
    },
    "y_label": None,
}
# fmt: on


def test_custom_style_psychrochart():
    """Test the plot custom styling with dicts."""
    custom_style = {
        "figure": {
            "figsize": [12, 8],
            "base_fontsize": 12,
            "title": None,
            "x_label": None,
            "y_label": None,
            "partial_axis": False,
        },
        "limits": {
            "range_temp_c": [15, 25],
            "range_humidity_g_kg": [0, 20],
            "altitude_m": 900,
            "step_temp": 0.2,
        },
        "saturation": {"color": [0, 0.3, 1.0], "linewidth": 2},
        "constant_rh": {
            "color": [0.0, 0.498, 1.0, 0.7],
            "linewidth": 2.5,
            "linestyle": ":",
        },
        "chart_params": {
            "with_constant_rh": True,
            "constant_rh_curves": [25, 50, 75],
            "constant_rh_labels": [25, 50, 75],
            "with_constant_v": False,
            "with_constant_h": False,
            "range_wet_temp": [-10, 30],
            "constant_humid_label_include_limits": False,
            "with_zones": False,
        },
        "constant_v_annotation": {
            "color": [0.2, 0.2, 0.2],
            "fontsize": 7,
            "bbox": {
                "boxstyle": "square,pad=-0.2",
                "color": [1, 1, 1, 0.9],
                "lw": 0.5,
            },
        },
        "constant_h_annotation": {
            "color": [0.2, 0.2, 0.2],
            "fontsize": 6,
            "bbox": {
                "boxstyle": "square,pad=-0.1",
                "color": [1, 1, 1, 0.9],
                "lw": 0.5,
            },
        },
        "constant_wet_temp_annotation": {
            "color": "#7f1cd0",
            "fontsize": 15,
            "bbox": {"boxstyle": "round", "ec": "#0909f310", "lw": 0.5},
        },
        "constant_rh_annotation": {
            "fontsize": 12,
            "bbox": {"boxstyle": "square,pad=2", "color": [1, 1, 1, 0.3]},
        },
    }
    chart = PsychroChart.create(custom_style)
    chart.plot()
    chart.plot_legend()
    store_test_chart(chart, "test_custom_psychrochart.svg")


def test_custom_style_psychrochart_2():
    """Test the plot custom styling with dicts."""
    custom_style = {
        "chart_params": {
            "constant_h_label": None,
            "constant_h_labels": [0, 10, 20, 30, 40, 50, 60, 70],
            "constant_h_step": 5,
            "constant_h_labels_loc": -0.1,
            "constant_humid_label": None,
            "constant_humid_label_include_limits": False,
            "constant_humid_label_step": 5,
            "constant_humid_step": 2.5,
            "constant_rh_curves": [20, 40, 50, 60, 80],
            "constant_rh_label": None,
            "constant_rh_labels": [20, 30, 40, 50, 60],
            "constant_rh_labels_loc": 0.5,
            "constant_temp_label": None,
            "constant_temp_label_include_limits": False,
            "constant_temp_label_step": 10,
            "constant_temp_step": 5,
            "constant_v_label": None,
            "constant_v_labels": [0.83, 0.84, 0.85, 0.86, 0.87, 0.88],
            "constant_v_labels_loc": 0.1,
            "constant_v_step": 0.01,
            "constant_wet_temp_label": None,
            "constant_wet_temp_labels": [10, 15, 20, 25],
            "constant_wet_temp_step": 5,
            "range_wet_temp": [10, 30],
            "range_h": [10, 100],
            "range_vol_m3_kg": [0.82, 0.9],
            "with_constant_dry_temp": True,
            "with_constant_h": True,
            "with_constant_humidity": True,
            "with_constant_rh": True,
            "with_constant_v": True,
            "with_constant_wet_temp": True,
            "with_zones": False,
        },
        "constant_dry_temp": {
            "color": [0.855, 0.145, 0.114, 0.7],
            "linestyle": ":",
            "linewidth": 0.75,
        },
        "constant_h": {
            "color": [0.251, 0.0, 0.502, 0.7],
            "linestyle": "-",
            "linewidth": 2,
        },
        "constant_h_annotation": {
            "fontsize": 15,
            "bbox": {
                "boxstyle": "square,pad=-0.1",
                "color": [1, 1, 1, 0.9],
                "lw": 0.5,
            },
        },
        "constant_humidity": {
            "color": [0.0, 0.125, 0.376, 0.7],
            "linestyle": ":",
            "linewidth": 0.75,
        },
        "constant_rh": {
            "color": [0.0, 0.498, 1.0, 0.7],
            "linestyle": "-.",
            "linewidth": 2,
        },
        "constant_v": {
            "color": [0.0, 0.502, 0.337, 0.7],
            "linestyle": "-",
            "linewidth": 1,
        },
        "constant_v_annotation": {
            "color": [0.2, 0.2, 0.2],
            "fontsize": 12,
            "bbox": {
                "boxstyle": "square,pad=-0.2",
                "color": [1, 1, 1, 0.9],
                "lw": 0.5,
            },
        },
        "constant_wet_temp": {
            "color": [0.498, 0.875, 1.0, 0.7],
            "linestyle": "-",
            "linewidth": 1,
        },
        "figure": TEST_EXAMPLE_FIG_CONFIG,
        "limits": {
            "range_humidity_g_kg": [2.5, 20],
            "range_temp_c": [15, 35],
            "step_temp": 0.5,
            "pressure_kpa": 101.42,
        },
        "saturation": {
            "color": [0.855, 0.145, 0.114],
            "linestyle": "-",
            "linewidth": 5,
        },
    }
    chart = PsychroChart.create(custom_style)
    store_test_chart(chart, "test_custom_psychrochart_2.svg")

    for p in np.arange(90.0, 105.0):
        custom_style["limits"]["pressure_kpa"] = p  # type: ignore[index]
        PsychroChart.create(custom_style)


def test_custom_style_psychrochart_3():
    """Test the plot custom styling with dicts, negative temperatures."""
    custom_style = {
        "chart_params": {
            "constant_h_label": None,
            "constant_h_labels": [-25, -15, 0, 10, 15],
            "constant_h_step": 5,
            "constant_humid_label": None,
            "constant_humid_label_include_limits": False,
            "constant_humid_label_step": 1,
            "constant_humid_step": 0.5,
            "constant_rh_curves": [10, 20, 40, 50, 60, 80, 90],
            "constant_rh_label": None,
            "constant_rh_labels": [20, 40, 60],
            "constant_rh_labels_loc": 0.8,
            "constant_temp_label": None,
            "constant_temp_label_include_limits": False,
            "constant_temp_label_step": 5,
            "constant_temp_step": 5,
            "constant_v_label": None,
            "constant_v_labels": [0.74, 0.76, 0.78, 0.8],
            "constant_v_labels_loc": 0.01,
            "constant_v_step": 0.01,
            "constant_wet_temp_label": None,
            "constant_wet_temp_labels": [-15, -10, -5, 0],
            "constant_wet_temp_step": 5,
            "range_wet_temp": [-25, 5],
            "range_h": [-30, 20],
            "range_vol_m3_kg": [0.7, 0.82],
            "with_constant_dry_temp": True,
            "with_constant_h": True,
            "with_constant_humidity": True,
            "with_constant_rh": True,
            "with_constant_v": True,
            "with_constant_wet_temp": True,
            "with_zones": False,
        },
        "constant_dry_temp": {
            "color": [0.855, 0.145, 0.114, 0.7],
            "linestyle": ":",
            "linewidth": 0.75,
        },
        "constant_h": {
            "color": [0.251, 0.0, 0.502, 0.7],
            "linestyle": "-",
            "linewidth": 2,
        },
        "constant_humidity": {
            "color": [0.0, 0.125, 0.376, 0.7],
            "linestyle": ":",
            "linewidth": 0.75,
        },
        "constant_rh": {
            "color": [0.0, 0.498, 1.0, 0.7],
            "linestyle": "-.",
            "linewidth": 2,
        },
        "constant_v": {
            "color": [0.0, 0.502, 0.337, 0.7],
            "linestyle": "-",
            "linewidth": 1,
        },
        "constant_wet_temp": {
            "color": [0.498, 0.875, 1.0, 0.7],
            "linestyle": "-",
            "linewidth": 1,
        },
        "figure": TEST_EXAMPLE_FIG_CONFIG,
        "limits": {
            "range_humidity_g_kg": [0, 3],
            "range_temp_c": [-30, 10],
            "step_temp": 0.5,
            "pressure_kpa": 101.42,
        },
        "saturation": {
            "color": [0.855, 0.145, 0.114],
            "linestyle": "-",
            "linewidth": 5,
        },
        "zones": TEST_EXAMPLE_ZONES,
    }
    chart = PsychroChart.create(custom_style)
    store_test_chart(chart, "test_custom_psychrochart_3.svg")

    for p in np.arange(90.0, 105.0):
        custom_style["limits"]["pressure_kpa"] = p  # type: ignore[index]
        PsychroChart.create(custom_style)


def test_default_styles_psychrochart():
    """Test the plot custom styling with other preset styles."""
    chart = PsychroChart.create("interior")
    chart.plot()
    chart.plot_legend(
        markerscale=0.7, frameon=False, fontsize=10, labelspacing=1.2
    )
    store_test_chart(chart, "test_interior_psychrochart.svg")
