import _plotly_utils.basevalidators as _bv


class ColorwayValidator(_bv.ColorlistValidator):
    def __init__(self, plotly_name="colorway", parent_name="layout", **kwargs):
        super(ColorwayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
