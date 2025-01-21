import _plotly_utils.basevalidators as _bv


class ValueformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name="valueformat", parent_name="sankey", **kwargs):
        super(ValueformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
