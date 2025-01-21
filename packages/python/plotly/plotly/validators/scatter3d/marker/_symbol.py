import _plotly_utils.basevalidators as _bv


class SymbolValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="symbol", parent_name="scatter3d.marker", **kwargs):
        super(SymbolValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values",
                [
                    "circle",
                    "circle-open",
                    "cross",
                    "diamond",
                    "diamond-open",
                    "square",
                    "square-open",
                    "x",
                ],
            ),
            **kwargs,
        )
