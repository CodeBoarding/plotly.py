import _plotly_utils.basevalidators as _bv


class ColorssrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="colorssrc", parent_name="icicle.marker", **kwargs):
        super(ColorssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
