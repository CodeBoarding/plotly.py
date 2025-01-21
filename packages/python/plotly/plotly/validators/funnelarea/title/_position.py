import _plotly_utils.basevalidators as _bv


class PositionValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="position", parent_name="funnelarea.title", **kwargs
    ):
        super(PositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["top left", "top center", "top right"]),
            **kwargs,
        )
