import _plotly_utils.basevalidators


class ScattermapValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattermap", parent_name="", **kwargs):
        super(ScattermapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattermap"),
            **kwargs,
        )
