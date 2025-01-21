from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Template(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout"
    _path_str = "layout.template"
    _valid_props = {"data", "layout"}

    # data
    # ----
    @property
    def data(self):
        """
        The 'data' property is an instance of Data
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.template.Data`
          - A dict of string/value properties that will be passed
            to the Data constructor

        Returns
        -------
        plotly.graph_objs.layout.template.Data
        """
        return self["data"]

    @data.setter
    def data(self, val):
        self["data"] = val

    # layout
    # ------
    @property
    def layout(self):
        """
        The 'layout' property is an instance of Layout
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.Layout`
          - A dict of string/value properties that will be passed
            to the Layout constructor

        Returns
        -------
        plotly.graph_objs.layout.template.Layout
        """
        return self["layout"]

    @layout.setter
    def layout(self, val):
        self["layout"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        data
            :class:`plotly.graph_objects.layout.template.Data`
            instance or dict with compatible properties
        layout
            :class:`plotly.graph_objects.Layout` instance or dict
            with compatible properties
        """

    def __init__(self, arg=None, data=None, layout=None, **kwargs):
        """
        Construct a new Template object

        Default attributes to be applied to the plot. This should be a
        dict with format: `{'layout': layoutTemplate, 'data':
        {trace_type: [traceTemplate, ...], ...}}` where
        `layoutTemplate` is a dict matching the structure of
        `figure.layout` and `traceTemplate` is a dict matching the
        structure of the trace with type `trace_type` (e.g. 'scatter').
        Alternatively, this may be specified as an instance of
        plotly.graph_objs.layout.Template.  Trace templates are applied
        cyclically to traces of each type. Container arrays (eg
        `annotations`) have special handling: An object ending in
        `defaults` (eg `annotationdefaults`) is applied to each array
        item. But if an item has a `templateitemname` key we look in
        the template array for an item with matching `name` and apply
        that instead. If no matching `name` is found we mark the item
        invisible. Any named template item not referenced is appended
        to the end of the array, so this can be used to add a watermark
        annotation or a logo image, for example. To omit one of these
        items on the plot, make an item with matching
        `templateitemname` and `visible: false`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Template`
        data
            :class:`plotly.graph_objects.layout.template.Data`
            instance or dict with compatible properties
        layout
            :class:`plotly.graph_objects.Layout` instance or dict
            with compatible properties

        Returns
        -------
        Template
        """
        super(Template, self).__init__("template")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.Template
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Template`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("data", None)
        _v = data if data is not None else _v
        if _v is not None:
            self["data"] = _v
        _v = arg.pop("layout", None)
        _v = layout if layout is not None else _v
        if _v is not None:
            self["layout"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
