import _plotly_utils.basevalidators as _bv


class TextValidator(_bv.StringValidator):
    def __init__(
        self,
        plotly_name="text",
        parent_name="histogram2dcontour.colorbar.title",
        **kwargs,
    ):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            **kwargs,
        )
