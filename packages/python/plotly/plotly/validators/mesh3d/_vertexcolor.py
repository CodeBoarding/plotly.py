import _plotly_utils.basevalidators as _bv


class VertexcolorValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="vertexcolor", parent_name="mesh3d", **kwargs):
        super(VertexcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
