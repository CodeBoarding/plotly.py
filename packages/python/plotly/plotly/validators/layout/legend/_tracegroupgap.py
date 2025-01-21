import _plotly_utils.basevalidators as _bv


class TracegroupgapValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="tracegroupgap", parent_name="layout.legend", **kwargs
    ):
        super(TracegroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
