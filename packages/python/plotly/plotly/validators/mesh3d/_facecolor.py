import _plotly_utils.basevalidators as _bv


class FacecolorValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="facecolor", parent_name="mesh3d", **kwargs):
        super(FacecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
