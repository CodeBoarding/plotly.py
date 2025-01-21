import _plotly_utils.basevalidators


class LightingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="lighting", parent_name="mesh3d", **kwargs):
        super(LightingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Lighting"),
            **kwargs,
        )
