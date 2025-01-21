import _plotly_utils.basevalidators


class TickfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self,
        plotly_name="tickfont",
        parent_name="scattercarpet.marker.colorbar",
        **kwargs,
    ):
        super(TickfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickfont"),
            **kwargs,
        )
