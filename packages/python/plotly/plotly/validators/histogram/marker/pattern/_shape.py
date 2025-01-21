import _plotly_utils.basevalidators as _bv


class ShapeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="shape", parent_name="histogram.marker.pattern", **kwargs
    ):
        super(ShapeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            values=kwargs.pop("values", ["", "/", "\\", "x", "-", "|", "+", "."]),
            **kwargs,
        )
