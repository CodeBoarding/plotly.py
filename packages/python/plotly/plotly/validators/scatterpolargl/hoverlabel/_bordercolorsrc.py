import _plotly_utils.basevalidators as _bv


class BordercolorsrcValidator(_bv.SrcValidator):
    def __init__(
        self,
        plotly_name="bordercolorsrc",
        parent_name="scatterpolargl.hoverlabel",
        **kwargs,
    ):
        super(BordercolorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
