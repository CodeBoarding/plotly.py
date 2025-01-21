from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Polar(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout"
    _path_str = "layout.polar"
    _valid_props = {
        "angularaxis",
        "bargap",
        "barmode",
        "bgcolor",
        "domain",
        "gridshape",
        "hole",
        "radialaxis",
        "sector",
        "uirevision",
    }

    # angularaxis
    # -----------
    @property
    def angularaxis(self):
        """
        The 'angularaxis' property is an instance of AngularAxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.AngularAxis`
          - A dict of string/value properties that will be passed
            to the AngularAxis constructor

        Returns
        -------
        plotly.graph_objs.layout.polar.AngularAxis
        """
        return self["angularaxis"]

    @angularaxis.setter
    def angularaxis(self, val):
        self["angularaxis"] = val

    # bargap
    # ------
    @property
    def bargap(self):
        """
        Sets the gap between bars of adjacent location coordinates.
        Values are unitless, they represent fractions of the minimum
        difference in bar positions in the data.

        The 'bargap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["bargap"]

    @bargap.setter
    def bargap(self, val):
        self["bargap"] = val

    # barmode
    # -------
    @property
    def barmode(self):
        """
        Determines how bars at the same location coordinate are
        displayed on the graph. With "stack", the bars are stacked on
        top of one another With "overlay", the bars are plotted over
        one another, you might need to reduce "opacity" to see multiple
        bars.

        The 'barmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['stack', 'overlay']

        Returns
        -------
        Any
        """
        return self["barmode"]

    @barmode.setter
    def barmode(self, val):
        self["barmode"] = val

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
          - An instance of :class:`plotly.graph_objs.layout.polar.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

        Returns
        -------
        plotly.graph_objs.layout.polar.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # gridshape
    # ---------
    @property
    def gridshape(self):
        """
        Determines if the radial axis grid lines and angular axis line
        are drawn as "circular" sectors or as "linear" (polygon)
        sectors. Has an effect only when the angular axis has `type`
        "category". Note that `radialaxis.angle` is snapped to the
        angle of the closest vertex when `gridshape` is "circular" (so
        that radial axis scale is the same as the data scale).

        The 'gridshape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circular', 'linear']

        Returns
        -------
        Any
        """
        return self["gridshape"]

    @gridshape.setter
    def gridshape(self, val):
        self["gridshape"] = val

    # hole
    # ----
    @property
    def hole(self):
        """
        Sets the fraction of the radius to cut out of the polar
        subplot.

        The 'hole' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["hole"]

    @hole.setter
    def hole(self, val):
        self["hole"] = val

    # radialaxis
    # ----------
    @property
    def radialaxis(self):
        """
        The 'radialaxis' property is an instance of RadialAxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.RadialAxis`
          - A dict of string/value properties that will be passed
            to the RadialAxis constructor

        Returns
        -------
        plotly.graph_objs.layout.polar.RadialAxis
        """
        return self["radialaxis"]

    @radialaxis.setter
    def radialaxis(self, val):
        self["radialaxis"] = val

    # sector
    # ------
    @property
    def sector(self):
        """
            Sets angular span of this polar subplot with two angles (in
            degrees). Sector are assumed to be spanned in the
            counterclockwise direction with 0 corresponding to rightmost
            limit of the polar subplot.

            The 'sector' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'sector[0]' property is a number and may be specified as:
              - An int or float
        (1) The 'sector[1]' property is a number and may be specified as:
              - An int or float

            Returns
            -------
            list
        """
        return self["sector"]

    @sector.setter
    def sector(self, val):
        self["sector"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in axis attributes,
        if not overridden in the individual axes. Defaults to
        `layout.uirevision`.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        angularaxis
            :class:`plotly.graph_objects.layout.polar.AngularAxis`
            instance or dict with compatible properties
        bargap
            Sets the gap between bars of adjacent location
            coordinates. Values are unitless, they represent
            fractions of the minimum difference in bar positions in
            the data.
        barmode
            Determines how bars at the same location coordinate are
            displayed on the graph. With "stack", the bars are
            stacked on top of one another With "overlay", the bars
            are plotted over one another, you might need to reduce
            "opacity" to see multiple bars.
        bgcolor
            Set the background color of the subplot
        domain
            :class:`plotly.graph_objects.layout.polar.Domain`
            instance or dict with compatible properties
        gridshape
            Determines if the radial axis grid lines and angular
            axis line are drawn as "circular" sectors or as
            "linear" (polygon) sectors. Has an effect only when the
            angular axis has `type` "category". Note that
            `radialaxis.angle` is snapped to the angle of the
            closest vertex when `gridshape` is "circular" (so that
            radial axis scale is the same as the data scale).
        hole
            Sets the fraction of the radius to cut out of the polar
            subplot.
        radialaxis
            :class:`plotly.graph_objects.layout.polar.RadialAxis`
            instance or dict with compatible properties
        sector
            Sets angular span of this polar subplot with two angles
            (in degrees). Sector are assumed to be spanned in the
            counterclockwise direction with 0 corresponding to
            rightmost limit of the polar subplot.
        uirevision
            Controls persistence of user-driven changes in axis
            attributes, if not overridden in the individual axes.
            Defaults to `layout.uirevision`.
        """

    def __init__(
        self,
        arg=None,
        angularaxis=None,
        bargap=None,
        barmode=None,
        bgcolor=None,
        domain=None,
        gridshape=None,
        hole=None,
        radialaxis=None,
        sector=None,
        uirevision=None,
        **kwargs,
    ):
        """
        Construct a new Polar object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Polar`
        angularaxis
            :class:`plotly.graph_objects.layout.polar.AngularAxis`
            instance or dict with compatible properties
        bargap
            Sets the gap between bars of adjacent location
            coordinates. Values are unitless, they represent
            fractions of the minimum difference in bar positions in
            the data.
        barmode
            Determines how bars at the same location coordinate are
            displayed on the graph. With "stack", the bars are
            stacked on top of one another With "overlay", the bars
            are plotted over one another, you might need to reduce
            "opacity" to see multiple bars.
        bgcolor
            Set the background color of the subplot
        domain
            :class:`plotly.graph_objects.layout.polar.Domain`
            instance or dict with compatible properties
        gridshape
            Determines if the radial axis grid lines and angular
            axis line are drawn as "circular" sectors or as
            "linear" (polygon) sectors. Has an effect only when the
            angular axis has `type` "category". Note that
            `radialaxis.angle` is snapped to the angle of the
            closest vertex when `gridshape` is "circular" (so that
            radial axis scale is the same as the data scale).
        hole
            Sets the fraction of the radius to cut out of the polar
            subplot.
        radialaxis
            :class:`plotly.graph_objects.layout.polar.RadialAxis`
            instance or dict with compatible properties
        sector
            Sets angular span of this polar subplot with two angles
            (in degrees). Sector are assumed to be spanned in the
            counterclockwise direction with 0 corresponding to
            rightmost limit of the polar subplot.
        uirevision
            Controls persistence of user-driven changes in axis
            attributes, if not overridden in the individual axes.
            Defaults to `layout.uirevision`.

        Returns
        -------
        Polar
        """
        super(Polar, self).__init__("polar")

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
The first argument to the plotly.graph_objs.layout.Polar
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Polar`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("angularaxis", None)
        _v = angularaxis if angularaxis is not None else _v
        if _v is not None:
            self["angularaxis"] = _v
        _v = arg.pop("bargap", None)
        _v = bargap if bargap is not None else _v
        if _v is not None:
            self["bargap"] = _v
        _v = arg.pop("barmode", None)
        _v = barmode if barmode is not None else _v
        if _v is not None:
            self["barmode"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("gridshape", None)
        _v = gridshape if gridshape is not None else _v
        if _v is not None:
            self["gridshape"] = _v
        _v = arg.pop("hole", None)
        _v = hole if hole is not None else _v
        if _v is not None:
            self["hole"] = _v
        _v = arg.pop("radialaxis", None)
        _v = radialaxis if radialaxis is not None else _v
        if _v is not None:
            self["radialaxis"] = _v
        _v = arg.pop("sector", None)
        _v = sector if sector is not None else _v
        if _v is not None:
            self["sector"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
