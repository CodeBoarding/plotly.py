import _plotly_utils.basevalidators as _bv


class YsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="ysrc", parent_name="mesh3d", **kwargs):
        super(YsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
