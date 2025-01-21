import _plotly_utils.basevalidators as _bv


class AutosizeValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="autosize", parent_name="layout", **kwargs):
        super(AutosizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
