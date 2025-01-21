import _plotly_utils.basevalidators


class ChoroplethmapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="choroplethmapbox", parent_name="", **kwargs):
        super(ChoroplethmapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Choroplethmapbox"),
            **kwargs,
        )
