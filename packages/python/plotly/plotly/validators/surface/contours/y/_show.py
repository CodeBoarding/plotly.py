import _plotly_utils.basevalidators as _bv


class ShowValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="show", parent_name="surface.contours.y", **kwargs):
        super(ShowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
