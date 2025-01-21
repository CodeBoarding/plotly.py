from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "sunburst"
    _path_str = "sunburst.marker"
    _valid_props = {
        "autocolorscale",
        "cauto",
        "cmax",
        "cmid",
        "cmin",
        "coloraxis",
        "colorbar",
        "colors",
        "colorscale",
        "colorssrc",
        "line",
        "pattern",
        "reversescale",
        "showscale",
    }

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `marker.colorscale`. Has an effect only if colors is set to a
        numerical array. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.

        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here colors) or the bounds set in
        `marker.cmin` and `marker.cmax` Has an effect only if colors is
        set to a numerical array. Defaults to `false` when
        `marker.cmin` and `marker.cmax` are set by the user.

        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cauto"]

    @cauto.setter
    def cauto(self, val):
        self["cauto"] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain. Has an effect only if
        colors is set to a numerical array. Value should have the same
        units as colors and if set, `marker.cmin` must be set as well.

        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmax"]

    @cmax.setter
    def cmax(self, val):
        self["cmax"] = val

    # cmid
    # ----
    @property
    def cmid(self):
        """
        Sets the mid-point of the color domain by scaling `marker.cmin`
        and/or `marker.cmax` to be equidistant to this point. Has an
        effect only if colors is set to a numerical array. Value should
        have the same units as colors. Has no effect when
        `marker.cauto` is `false`.

        The 'cmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmid"]

    @cmid.setter
    def cmid(self, val):
        self["cmid"] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain. Has an effect only if
        colors is set to a numerical array. Value should have the same
        units as colors and if set, `marker.cmax` must be set as well.

        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmin"]

    @cmin.setter
    def cmin(self, val):
        self["cmin"] = val

    # coloraxis
    # ---------
    @property
    def coloraxis(self):
        """
        Sets a reference to a shared color axis. References to these
        shared color axes are "coloraxis", "coloraxis2", "coloraxis3",
        etc. Settings for these shared color axes are set in the
        layout, under `layout.coloraxis`, `layout.coloraxis2`, etc.
        Note that multiple color scales can be linked to the same color
        axis.

        The 'coloraxis' property is an identifier of a particular
        subplot, of type 'coloraxis', that may be specified as the string 'coloraxis'
        optionally followed by an integer >= 1
        (e.g. 'coloraxis', 'coloraxis1', 'coloraxis2', 'coloraxis3', etc.)

        Returns
        -------
        str
        """
        return self["coloraxis"]

    @coloraxis.setter
    def coloraxis(self, val):
        self["coloraxis"] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sunburst.marker.ColorBar`
          - A dict of string/value properties that will be passed
            to the ColorBar constructor

        Returns
        -------
        plotly.graph_objs.sunburst.marker.ColorBar
        """
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    # colors
    # ------
    @property
    def colors(self):
        """
        Sets the color of each sector of this trace. If not specified,
        the default trace color set is used to pick the sector colors.

        The 'colors' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["colors"]

    @colors.setter
    def colors(self, val):
        self["colors"] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. Has an effect only if colors is set to a
        numerical array. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use `marker.cmin` and
        `marker.cmax`. Alternatively, `colorscale` may be a palette
        name string of the following list: Blackbody,Bluered,Blues,Civi
        dis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow
        ,RdBu,Reds,Viridis,YlGnBu,YlOrRd.

        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1),
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl',
                 'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn',
                 'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu',
                 'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar',
                 'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn',
                 'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
                 'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr',
                 'ylorrd'].
            Appending '_r' to a named colorscale reverses it.

        Returns
        -------
        str
        """
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    # colorssrc
    # ---------
    @property
    def colorssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `colors`.

        The 'colorssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["colorssrc"]

    @colorssrc.setter
    def colorssrc(self, val):
        self["colorssrc"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sunburst.marker.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.sunburst.marker.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # pattern
    # -------
    @property
    def pattern(self):
        """
        Sets the pattern within the marker.

        The 'pattern' property is an instance of Pattern
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sunburst.marker.Pattern`
          - A dict of string/value properties that will be passed
            to the Pattern constructor

        Returns
        -------
        plotly.graph_objs.sunburst.marker.Pattern
        """
        return self["pattern"]

    @pattern.setter
    def pattern(self, val):
        self["pattern"] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. Has an effect only if
        colors is set to a numerical array. If true, `marker.cmin` will
        correspond to the last color in the array and `marker.cmax`
        will correspond to the first color.

        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace. Has an effect only if colors is set to a numerical
        array.

        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showscale"]

    @showscale.setter
    def showscale(self, val):
        self["showscale"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if colors is
            set to a numerical array. In case `colorscale` is
            unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here colors) or the
            bounds set in `marker.cmin` and `marker.cmax` Has an
            effect only if colors is set to a numerical array.
            Defaults to `false` when `marker.cmin` and
            `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if colors is set to a numerical array. Value
            should have the same units as colors and if set,
            `marker.cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if colors is set to a
            numerical array. Value should have the same units as
            colors. Has no effect when `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if colors is set to a numerical array. Value
            should have the same units as colors and if set,
            `marker.cmax` must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.sunburst.marker.ColorBar`
            instance or dict with compatible properties
        colors
            Sets the color of each sector of this trace. If not
            specified, the default trace color set is used to pick
            the sector colors.
        colorscale
            Sets the colorscale. Has an effect only if colors is
            set to a numerical array. The colorscale must be an
            array containing arrays mapping a normalized value to
            an rgb, rgba, hex, hsl, hsv, or named color string. At
            minimum, a mapping for the lowest (0) and highest (1)
            values are required. For example, `[[0,
            'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
            bounds of the colorscale in color space, use
            `marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Blackbody,Bluered,Blues,Cividis,Earth,E
            lectric,Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,Rd
            Bu,Reds,Viridis,YlGnBu,YlOrRd.
        colorssrc
            Sets the source reference on Chart Studio Cloud for
            `colors`.
        line
            :class:`plotly.graph_objects.sunburst.marker.Line`
            instance or dict with compatible properties
        pattern
            Sets the pattern within the marker.
        reversescale
            Reverses the color mapping if true. Has an effect only
            if colors is set to a numerical array. If true,
            `marker.cmin` will correspond to the last color in the
            array and `marker.cmax` will correspond to the first
            color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if colors is set to a
            numerical array.
        """

    def __init__(
        self,
        arg=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colors=None,
        colorscale=None,
        colorssrc=None,
        line=None,
        pattern=None,
        reversescale=None,
        showscale=None,
        **kwargs,
    ):
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.sunburst.Marker`
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if colors is
            set to a numerical array. In case `colorscale` is
            unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here colors) or the
            bounds set in `marker.cmin` and `marker.cmax` Has an
            effect only if colors is set to a numerical array.
            Defaults to `false` when `marker.cmin` and
            `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if colors is set to a numerical array. Value
            should have the same units as colors and if set,
            `marker.cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if colors is set to a
            numerical array. Value should have the same units as
            colors. Has no effect when `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if colors is set to a numerical array. Value
            should have the same units as colors and if set,
            `marker.cmax` must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.sunburst.marker.ColorBar`
            instance or dict with compatible properties
        colors
            Sets the color of each sector of this trace. If not
            specified, the default trace color set is used to pick
            the sector colors.
        colorscale
            Sets the colorscale. Has an effect only if colors is
            set to a numerical array. The colorscale must be an
            array containing arrays mapping a normalized value to
            an rgb, rgba, hex, hsl, hsv, or named color string. At
            minimum, a mapping for the lowest (0) and highest (1)
            values are required. For example, `[[0,
            'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
            bounds of the colorscale in color space, use
            `marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Blackbody,Bluered,Blues,Cividis,Earth,E
            lectric,Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,Rd
            Bu,Reds,Viridis,YlGnBu,YlOrRd.
        colorssrc
            Sets the source reference on Chart Studio Cloud for
            `colors`.
        line
            :class:`plotly.graph_objects.sunburst.marker.Line`
            instance or dict with compatible properties
        pattern
            Sets the pattern within the marker.
        reversescale
            Reverses the color mapping if true. Has an effect only
            if colors is set to a numerical array. If true,
            `marker.cmin` will correspond to the last color in the
            array and `marker.cmax` will correspond to the first
            color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if colors is set to a
            numerical array.

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__("marker")

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
The first argument to the plotly.graph_objs.sunburst.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.sunburst.Marker`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("autocolorscale", None)
        _v = autocolorscale if autocolorscale is not None else _v
        if _v is not None:
            self["autocolorscale"] = _v
        _v = arg.pop("cauto", None)
        _v = cauto if cauto is not None else _v
        if _v is not None:
            self["cauto"] = _v
        _v = arg.pop("cmax", None)
        _v = cmax if cmax is not None else _v
        if _v is not None:
            self["cmax"] = _v
        _v = arg.pop("cmid", None)
        _v = cmid if cmid is not None else _v
        if _v is not None:
            self["cmid"] = _v
        _v = arg.pop("cmin", None)
        _v = cmin if cmin is not None else _v
        if _v is not None:
            self["cmin"] = _v
        _v = arg.pop("coloraxis", None)
        _v = coloraxis if coloraxis is not None else _v
        if _v is not None:
            self["coloraxis"] = _v
        _v = arg.pop("colorbar", None)
        _v = colorbar if colorbar is not None else _v
        if _v is not None:
            self["colorbar"] = _v
        _v = arg.pop("colors", None)
        _v = colors if colors is not None else _v
        if _v is not None:
            self["colors"] = _v
        _v = arg.pop("colorscale", None)
        _v = colorscale if colorscale is not None else _v
        if _v is not None:
            self["colorscale"] = _v
        _v = arg.pop("colorssrc", None)
        _v = colorssrc if colorssrc is not None else _v
        if _v is not None:
            self["colorssrc"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("pattern", None)
        _v = pattern if pattern is not None else _v
        if _v is not None:
            self["pattern"] = _v
        _v = arg.pop("reversescale", None)
        _v = reversescale if reversescale is not None else _v
        if _v is not None:
            self["reversescale"] = _v
        _v = arg.pop("showscale", None)
        _v = showscale if showscale is not None else _v
        if _v is not None:
            self["showscale"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
