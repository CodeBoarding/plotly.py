from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Smith(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout"
    _path_str = "layout.smith"
    _valid_props = {"bgcolor", "domain", "imaginaryaxis", "realaxis"}

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Set the background color of the subplot

        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.smith.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

        Returns
        -------
        plotly.graph_objs.layout.smith.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # imaginaryaxis
    # -------------
    @property
    def imaginaryaxis(self):
        """
        The 'imaginaryaxis' property is an instance of Imaginaryaxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.smith.Imaginaryaxis`
          - A dict of string/value properties that will be passed
            to the Imaginaryaxis constructor

        Returns
        -------
        plotly.graph_objs.layout.smith.Imaginaryaxis
        """
        return self["imaginaryaxis"]

    @imaginaryaxis.setter
    def imaginaryaxis(self, val):
        self["imaginaryaxis"] = val

    # realaxis
    # --------
    @property
    def realaxis(self):
        """
        The 'realaxis' property is an instance of Realaxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.smith.Realaxis`
          - A dict of string/value properties that will be passed
            to the Realaxis constructor

        Returns
        -------
        plotly.graph_objs.layout.smith.Realaxis
        """
        return self["realaxis"]

    @realaxis.setter
    def realaxis(self, val):
        self["realaxis"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Set the background color of the subplot
        domain
            :class:`plotly.graph_objects.layout.smith.Domain`
            instance or dict with compatible properties
        imaginaryaxis
            :class:`plotly.graph_objects.layout.smith.Imaginaryaxis
            ` instance or dict with compatible properties
        realaxis
            :class:`plotly.graph_objects.layout.smith.Realaxis`
            instance or dict with compatible properties
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        domain=None,
        imaginaryaxis=None,
        realaxis=None,
        **kwargs,
    ):
        """
        Construct a new Smith object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Smith`
        bgcolor
            Set the background color of the subplot
        domain
            :class:`plotly.graph_objects.layout.smith.Domain`
            instance or dict with compatible properties
        imaginaryaxis
            :class:`plotly.graph_objects.layout.smith.Imaginaryaxis
            ` instance or dict with compatible properties
        realaxis
            :class:`plotly.graph_objects.layout.smith.Realaxis`
            instance or dict with compatible properties

        Returns
        -------
        Smith
        """
        super(Smith, self).__init__("smith")

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
The first argument to the plotly.graph_objs.layout.Smith
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Smith`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("imaginaryaxis", None)
        _v = imaginaryaxis if imaginaryaxis is not None else _v
        if _v is not None:
            self["imaginaryaxis"] = _v
        _v = arg.pop("realaxis", None)
        _v = realaxis if realaxis is not None else _v
        if _v is not None:
            self["realaxis"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
