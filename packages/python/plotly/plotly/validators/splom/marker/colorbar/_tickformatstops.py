import _plotly_utils.basevalidators


class TickformatstopsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(
        self,
        plotly_name="tickformatstops",
        parent_name="splom.marker.colorbar",
        **kwargs,
    ):
        super(TickformatstopsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickformatstop"),
            **kwargs,
        )
