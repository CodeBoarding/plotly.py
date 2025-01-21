import _plotly_utils.basevalidators as _bv


class GroupValidator(_bv.StringValidator):
    def __init__(self, plotly_name="group", parent_name="frame", **kwargs):
        super(GroupValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs
        )
