from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Streamtube(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ""
    _path_str = "streamtube"
    _valid_props = {
        "autocolorscale",
        "cauto",
        "cmax",
        "cmid",
        "cmin",
        "coloraxis",
        "colorbar",
        "colorscale",
        "customdata",
        "customdatasrc",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "ids",
        "idssrc",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "lighting",
        "lightposition",
        "maxdisplayed",
        "meta",
        "metasrc",
        "name",
        "opacity",
        "reversescale",
        "scene",
        "showlegend",
        "showscale",
        "sizeref",
        "starts",
        "stream",
        "text",
        "type",
        "u",
        "uhoverformat",
        "uid",
        "uirevision",
        "usrc",
        "v",
        "vhoverformat",
        "visible",
        "vsrc",
        "w",
        "whoverformat",
        "wsrc",
        "x",
        "xhoverformat",
        "xsrc",
        "y",
        "yhoverformat",
        "ysrc",
        "z",
        "zhoverformat",
        "zsrc",
    }

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `colorscale`. In case `colorscale` is unspecified or
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
        respect to the input data (here u/v/w norm) or the bounds set
        in `cmin` and `cmax` Defaults to `false` when `cmin` and `cmax`
        are set by the user.

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
        Sets the upper bound of the color domain. Value should have the
        same units as u/v/w norm and if set, `cmin` must be set as
        well.

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
        Sets the mid-point of the color domain by scaling `cmin` and/or
        `cmax` to be equidistant to this point. Value should have the
        same units as u/v/w norm. Has no effect when `cauto` is
        `false`.

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
        Sets the lower bound of the color domain. Value should have the
        same units as u/v/w norm and if set, `cmax` must be set as
        well.

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
          - An instance of :class:`plotly.graph_objs.streamtube.ColorBar`
          - A dict of string/value properties that will be passed
            to the ColorBar constructor

        Returns
        -------
        plotly.graph_objs.streamtube.ColorBar
        """
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use `cmin` and `cmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Blackbody,Bluered,Blues,Cividis,Earth,Electric,
        Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,RdBu,Reds,Viridis,
        YlGnBu,YlOrRd.

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

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements

        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'u', 'v', 'w', 'norm', 'divergence', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hoverinfo`.

        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hoverinfosrc"]

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self["hoverinfosrc"] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.streamtube.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.streamtube.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    # hovertemplate
    # -------------
    @property
    def hovertemplate(self):
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available. Finally, the
        template string has access to variables `tubex`, `tubey`,
        `tubez`, `tubeu`, `tubev`, `tubew`, `norm` and `divergence`.
        Anything contained in tag `<extra>` is displayed in the
        secondary box, for example "<extra>{fullData.name}</extra>". To
        hide the secondary box completely, use an empty tag
        `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

    # hovertemplatesrc
    # ----------------
    @property
    def hovertemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertemplatesrc"]

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self["hovertemplatesrc"] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Same as `text`.

        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.

        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `ids`.

        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

    # legend
    # ------
    @property
    def legend(self):
        """
        Sets the reference to a legend to show this trace in.
        References to these legends are "legend", "legend2", "legend3",
        etc. Settings for these legends are set in the layout, under
        `layout.legend`, `layout.legend2`, etc.

        The 'legend' property is an identifier of a particular
        subplot, of type 'legend', that may be specified as the string 'legend'
        optionally followed by an integer >= 1
        (e.g. 'legend', 'legend1', 'legend2', 'legend3', etc.)

        Returns
        -------
        str
        """
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces and shapes part of
        the same legend group hide/show at the same time when toggling
        legend items.

        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    # legendgrouptitle
    # ----------------
    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.streamtube.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.streamtube.Legendgrouptitle
        """
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

    # legendrank
    # ----------
    @property
    def legendrank(self):
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        "reversed" `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items. When
        having unranked or equal rank items shapes would be displayed
        after traces i.e. according to their order in data and layout.

        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["legendrank"]

    @legendrank.setter
    def legendrank(self, val):
        self["legendrank"] = val

    # legendwidth
    # -----------
    @property
    def legendwidth(self):
        """
        Sets the width (in px or fraction) of the legend for this
        trace.

        The 'legendwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["legendwidth"]

    @legendwidth.setter
    def legendwidth(self, val):
        self["legendwidth"] = val

    # lighting
    # --------
    @property
    def lighting(self):
        """
        The 'lighting' property is an instance of Lighting
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.streamtube.Lighting`
          - A dict of string/value properties that will be passed
            to the Lighting constructor

        Returns
        -------
        plotly.graph_objs.streamtube.Lighting
        """
        return self["lighting"]

    @lighting.setter
    def lighting(self, val):
        self["lighting"] = val

    # lightposition
    # -------------
    @property
    def lightposition(self):
        """
        The 'lightposition' property is an instance of Lightposition
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.streamtube.Lightposition`
          - A dict of string/value properties that will be passed
            to the Lightposition constructor

        Returns
        -------
        plotly.graph_objs.streamtube.Lightposition
        """
        return self["lightposition"]

    @lightposition.setter
    def lightposition(self, val):
        self["lightposition"] = val

    # maxdisplayed
    # ------------
    @property
    def maxdisplayed(self):
        """
        The maximum number of displayed segments in a streamtube.

        The 'maxdisplayed' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["maxdisplayed"]

    @maxdisplayed.setter
    def maxdisplayed(self, val):
        self["maxdisplayed"] = val

    # meta
    # ----
    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.

        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    # metasrc
    # -------
    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `meta`.

        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appears as the legend item
        and on hover.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the surface. Please note that in the case
        of using high `opacity` values for example a value greater than
        or equal to 0.5 on two surfaces (and 0.25 with four surfaces),
        an overlay of multiple transparent surfaces may not perfectly
        be sorted in depth by the webgl API. This behavior may be
        improved in the near future and is subject to change.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. If true, `cmin` will
        correspond to the last color in the array and `cmax` will
        correspond to the first color.

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

    # scene
    # -----
    @property
    def scene(self):
        """
        Sets a reference between this trace's 3D coordinate system and
        a 3D scene. If "scene" (the default value), the (x,y,z)
        coordinates refer to `layout.scene`. If "scene2", the (x,y,z)
        coordinates refer to `layout.scene2`, and so on.

        The 'scene' property is an identifier of a particular
        subplot, of type 'scene', that may be specified as the string 'scene'
        optionally followed by an integer >= 1
        (e.g. 'scene', 'scene1', 'scene2', 'scene3', etc.)

        Returns
        -------
        str
        """
        return self["scene"]

    @scene.setter
    def scene(self, val):
        self["scene"] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.

        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace.

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

    # sizeref
    # -------
    @property
    def sizeref(self):
        """
        The scaling factor for the streamtubes. The default is 1, which
        avoids two max divergence tubes from touching at adjacent
        starting positions.

        The 'sizeref' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["sizeref"]

    @sizeref.setter
    def sizeref(self, val):
        self["sizeref"] = val

    # starts
    # ------
    @property
    def starts(self):
        """
        The 'starts' property is an instance of Starts
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.streamtube.Starts`
          - A dict of string/value properties that will be passed
            to the Starts constructor

        Returns
        -------
        plotly.graph_objs.streamtube.Starts
        """
        return self["starts"]

    @starts.setter
    def starts(self, val):
        self["starts"] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.streamtube.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

        Returns
        -------
        plotly.graph_objs.streamtube.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets a text element associated with this trace. If trace
        `hoverinfo` contains a "text" flag, this text element will be
        seen in all hover labels. Note that streamtube traces do not
        support array `text` values.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # u
    # -
    @property
    def u(self):
        """
        Sets the x components of the vector field.

        The 'u' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["u"]

    @u.setter
    def u(self, val):
        self["u"] = val

    # uhoverformat
    # ------------
    @property
    def uhoverformat(self):
        """
        Sets the hover text formatting rulefor `u`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format.By
        default the values are formatted using generic number format.

        The 'uhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["uhoverformat"]

    @uhoverformat.setter
    def uhoverformat(self, val):
        self["uhoverformat"] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.

        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # usrc
    # ----
    @property
    def usrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `u`.

        The 'usrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["usrc"]

    @usrc.setter
    def usrc(self, val):
        self["usrc"] = val

    # v
    # -
    @property
    def v(self):
        """
        Sets the y components of the vector field.

        The 'v' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["v"]

    @v.setter
    def v(self, val):
        self["v"] = val

    # vhoverformat
    # ------------
    @property
    def vhoverformat(self):
        """
        Sets the hover text formatting rulefor `v`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format.By
        default the values are formatted using generic number format.

        The 'vhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["vhoverformat"]

    @vhoverformat.setter
    def vhoverformat(self, val):
        self["vhoverformat"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).

        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # vsrc
    # ----
    @property
    def vsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `v`.

        The 'vsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["vsrc"]

    @vsrc.setter
    def vsrc(self, val):
        self["vsrc"] = val

    # w
    # -
    @property
    def w(self):
        """
        Sets the z components of the vector field.

        The 'w' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["w"]

    @w.setter
    def w(self, val):
        self["w"] = val

    # whoverformat
    # ------------
    @property
    def whoverformat(self):
        """
        Sets the hover text formatting rulefor `w`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format.By
        default the values are formatted using generic number format.

        The 'whoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["whoverformat"]

    @whoverformat.setter
    def whoverformat(self, val):
        self["whoverformat"] = val

    # wsrc
    # ----
    @property
    def wsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `w`.

        The 'wsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["wsrc"]

    @wsrc.setter
    def wsrc(self, val):
        self["wsrc"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x coordinates of the vector field.

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xhoverformat
    # ------------
    @property
    def xhoverformat(self):
        """
        Sets the hover text formatting rulefor `x`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `xaxis.hoverformat`.

        The 'xhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["xhoverformat"]

    @xhoverformat.setter
    def xhoverformat(self, val):
        self["xhoverformat"] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `x`.

        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["xsrc"]

    @xsrc.setter
    def xsrc(self, val):
        self["xsrc"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y coordinates of the vector field.

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yhoverformat
    # ------------
    @property
    def yhoverformat(self):
        """
        Sets the hover text formatting rulefor `y`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `yaxis.hoverformat`.

        The 'yhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["yhoverformat"]

    @yhoverformat.setter
    def yhoverformat(self, val):
        self["yhoverformat"] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `y`.

        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["ysrc"]

    @ysrc.setter
    def ysrc(self, val):
        self["ysrc"] = val

    # z
    # -
    @property
    def z(self):
        """
        Sets the z coordinates of the vector field.

        The 'z' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["z"]

    @z.setter
    def z(self, val):
        self["z"] = val

    # zhoverformat
    # ------------
    @property
    def zhoverformat(self):
        """
        Sets the hover text formatting rulefor `z`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `zaxis.hoverformat`.

        The 'zhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["zhoverformat"]

    @zhoverformat.setter
    def zhoverformat(self, val):
        self["zhoverformat"] = val

    # zsrc
    # ----
    @property
    def zsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `z`.

        The 'zsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["zsrc"]

    @zsrc.setter
    def zsrc(self, val):
        self["zsrc"] = val

    # type
    # ----
    @property
    def type(self):
        return self._props["type"]

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here u/v/w norm) or the
            bounds set in `cmin` and `cmax` Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as u/v/w norm. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.streamtube.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.streamtube.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `tubex`, `tubey`, `tubez`, `tubeu`,
            `tubev`, `tubew`, `norm` and `divergence`. Anything
            contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.streamtube.Legendgrouptitl
            e` instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        lighting
            :class:`plotly.graph_objects.streamtube.Lighting`
            instance or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.streamtube.Lightposition`
            instance or dict with compatible properties
        maxdisplayed
            The maximum number of displayed segments in a
            streamtube.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        sizeref
            The scaling factor for the streamtubes. The default is
            1, which avoids two max divergence tubes from touching
            at adjacent starting positions.
        starts
            :class:`plotly.graph_objects.streamtube.Starts`
            instance or dict with compatible properties
        stream
            :class:`plotly.graph_objects.streamtube.Stream`
            instance or dict with compatible properties
        text
            Sets a text element associated with this trace. If
            trace `hoverinfo` contains a "text" flag, this text
            element will be seen in all hover labels. Note that
            streamtube traces do not support array `text` values.
        u
            Sets the x components of the vector field.
        uhoverformat
            Sets the hover text formatting rulefor `u`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        usrc
            Sets the source reference on Chart Studio Cloud for
            `u`.
        v
            Sets the y components of the vector field.
        vhoverformat
            Sets the hover text formatting rulefor `v`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        vsrc
            Sets the source reference on Chart Studio Cloud for
            `v`.
        w
            Sets the z components of the vector field.
        whoverformat
            Sets the hover text formatting rulefor `w`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        wsrc
            Sets the source reference on Chart Studio Cloud for
            `w`.
        x
            Sets the x coordinates of the vector field.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y coordinates of the vector field.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the z coordinates of the vector field.
        zhoverformat
            Sets the hover text formatting rulefor `z`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `zaxis.hoverformat`.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.
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
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lighting=None,
        lightposition=None,
        maxdisplayed=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        sizeref=None,
        starts=None,
        stream=None,
        text=None,
        u=None,
        uhoverformat=None,
        uid=None,
        uirevision=None,
        usrc=None,
        v=None,
        vhoverformat=None,
        visible=None,
        vsrc=None,
        w=None,
        whoverformat=None,
        wsrc=None,
        x=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zhoverformat=None,
        zsrc=None,
        **kwargs,
    ):
        """
        Construct a new Streamtube object

        Use a streamtube trace to visualize flow in a vector field.
        Specify a vector field using 6 1D arrays of equal length, 3
        position arrays `x`, `y` and `z` and 3 vector component arrays
        `u`, `v`, and `w`.  By default, the tubes' starting positions
        will be cut from the vector field's x-z plane at its minimum y
        value. To specify your own starting position, use attributes
        `starts.x`, `starts.y` and `starts.z`. The color is encoded by
        the norm of (u, v, w), and the local radius by the divergence
        of (u, v, w).

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Streamtube`
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here u/v/w norm) or the
            bounds set in `cmin` and `cmax` Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as u/v/w norm. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.streamtube.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.streamtube.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `tubex`, `tubey`, `tubez`, `tubeu`,
            `tubev`, `tubew`, `norm` and `divergence`. Anything
            contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.streamtube.Legendgrouptitl
            e` instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        lighting
            :class:`plotly.graph_objects.streamtube.Lighting`
            instance or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.streamtube.Lightposition`
            instance or dict with compatible properties
        maxdisplayed
            The maximum number of displayed segments in a
            streamtube.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        sizeref
            The scaling factor for the streamtubes. The default is
            1, which avoids two max divergence tubes from touching
            at adjacent starting positions.
        starts
            :class:`plotly.graph_objects.streamtube.Starts`
            instance or dict with compatible properties
        stream
            :class:`plotly.graph_objects.streamtube.Stream`
            instance or dict with compatible properties
        text
            Sets a text element associated with this trace. If
            trace `hoverinfo` contains a "text" flag, this text
            element will be seen in all hover labels. Note that
            streamtube traces do not support array `text` values.
        u
            Sets the x components of the vector field.
        uhoverformat
            Sets the hover text formatting rulefor `u`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        usrc
            Sets the source reference on Chart Studio Cloud for
            `u`.
        v
            Sets the y components of the vector field.
        vhoverformat
            Sets the hover text formatting rulefor `v`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        vsrc
            Sets the source reference on Chart Studio Cloud for
            `v`.
        w
            Sets the z components of the vector field.
        whoverformat
            Sets the hover text formatting rulefor `w`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        wsrc
            Sets the source reference on Chart Studio Cloud for
            `w`.
        x
            Sets the x coordinates of the vector field.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y coordinates of the vector field.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the z coordinates of the vector field.
        zhoverformat
            Sets the hover text formatting rulefor `z`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `zaxis.hoverformat`.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.

        Returns
        -------
        Streamtube
        """
        super(Streamtube, self).__init__("streamtube")

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
The first argument to the plotly.graph_objs.Streamtube
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Streamtube`"""
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
        _v = arg.pop("colorscale", None)
        _v = colorscale if colorscale is not None else _v
        if _v is not None:
            self["colorscale"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("hoverinfo", None)
        _v = hoverinfo if hoverinfo is not None else _v
        if _v is not None:
            self["hoverinfo"] = _v
        _v = arg.pop("hoverinfosrc", None)
        _v = hoverinfosrc if hoverinfosrc is not None else _v
        if _v is not None:
            self["hoverinfosrc"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovertemplate", None)
        _v = hovertemplate if hovertemplate is not None else _v
        if _v is not None:
            self["hovertemplate"] = _v
        _v = arg.pop("hovertemplatesrc", None)
        _v = hovertemplatesrc if hovertemplatesrc is not None else _v
        if _v is not None:
            self["hovertemplatesrc"] = _v
        _v = arg.pop("hovertext", None)
        _v = hovertext if hovertext is not None else _v
        if _v is not None:
            self["hovertext"] = _v
        _v = arg.pop("ids", None)
        _v = ids if ids is not None else _v
        if _v is not None:
            self["ids"] = _v
        _v = arg.pop("idssrc", None)
        _v = idssrc if idssrc is not None else _v
        if _v is not None:
            self["idssrc"] = _v
        _v = arg.pop("legend", None)
        _v = legend if legend is not None else _v
        if _v is not None:
            self["legend"] = _v
        _v = arg.pop("legendgroup", None)
        _v = legendgroup if legendgroup is not None else _v
        if _v is not None:
            self["legendgroup"] = _v
        _v = arg.pop("legendgrouptitle", None)
        _v = legendgrouptitle if legendgrouptitle is not None else _v
        if _v is not None:
            self["legendgrouptitle"] = _v
        _v = arg.pop("legendrank", None)
        _v = legendrank if legendrank is not None else _v
        if _v is not None:
            self["legendrank"] = _v
        _v = arg.pop("legendwidth", None)
        _v = legendwidth if legendwidth is not None else _v
        if _v is not None:
            self["legendwidth"] = _v
        _v = arg.pop("lighting", None)
        _v = lighting if lighting is not None else _v
        if _v is not None:
            self["lighting"] = _v
        _v = arg.pop("lightposition", None)
        _v = lightposition if lightposition is not None else _v
        if _v is not None:
            self["lightposition"] = _v
        _v = arg.pop("maxdisplayed", None)
        _v = maxdisplayed if maxdisplayed is not None else _v
        if _v is not None:
            self["maxdisplayed"] = _v
        _v = arg.pop("meta", None)
        _v = meta if meta is not None else _v
        if _v is not None:
            self["meta"] = _v
        _v = arg.pop("metasrc", None)
        _v = metasrc if metasrc is not None else _v
        if _v is not None:
            self["metasrc"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("reversescale", None)
        _v = reversescale if reversescale is not None else _v
        if _v is not None:
            self["reversescale"] = _v
        _v = arg.pop("scene", None)
        _v = scene if scene is not None else _v
        if _v is not None:
            self["scene"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
        _v = arg.pop("showscale", None)
        _v = showscale if showscale is not None else _v
        if _v is not None:
            self["showscale"] = _v
        _v = arg.pop("sizeref", None)
        _v = sizeref if sizeref is not None else _v
        if _v is not None:
            self["sizeref"] = _v
        _v = arg.pop("starts", None)
        _v = starts if starts is not None else _v
        if _v is not None:
            self["starts"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("u", None)
        _v = u if u is not None else _v
        if _v is not None:
            self["u"] = _v
        _v = arg.pop("uhoverformat", None)
        _v = uhoverformat if uhoverformat is not None else _v
        if _v is not None:
            self["uhoverformat"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("usrc", None)
        _v = usrc if usrc is not None else _v
        if _v is not None:
            self["usrc"] = _v
        _v = arg.pop("v", None)
        _v = v if v is not None else _v
        if _v is not None:
            self["v"] = _v
        _v = arg.pop("vhoverformat", None)
        _v = vhoverformat if vhoverformat is not None else _v
        if _v is not None:
            self["vhoverformat"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("vsrc", None)
        _v = vsrc if vsrc is not None else _v
        if _v is not None:
            self["vsrc"] = _v
        _v = arg.pop("w", None)
        _v = w if w is not None else _v
        if _v is not None:
            self["w"] = _v
        _v = arg.pop("whoverformat", None)
        _v = whoverformat if whoverformat is not None else _v
        if _v is not None:
            self["whoverformat"] = _v
        _v = arg.pop("wsrc", None)
        _v = wsrc if wsrc is not None else _v
        if _v is not None:
            self["wsrc"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xhoverformat", None)
        _v = xhoverformat if xhoverformat is not None else _v
        if _v is not None:
            self["xhoverformat"] = _v
        _v = arg.pop("xsrc", None)
        _v = xsrc if xsrc is not None else _v
        if _v is not None:
            self["xsrc"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("yhoverformat", None)
        _v = yhoverformat if yhoverformat is not None else _v
        if _v is not None:
            self["yhoverformat"] = _v
        _v = arg.pop("ysrc", None)
        _v = ysrc if ysrc is not None else _v
        if _v is not None:
            self["ysrc"] = _v
        _v = arg.pop("z", None)
        _v = z if z is not None else _v
        if _v is not None:
            self["z"] = _v
        _v = arg.pop("zhoverformat", None)
        _v = zhoverformat if zhoverformat is not None else _v
        if _v is not None:
            self["zhoverformat"] = _v
        _v = arg.pop("zsrc", None)
        _v = zsrc if zsrc is not None else _v
        if _v is not None:
            self["zsrc"] = _v

        # Read-only literals
        # ------------------

        self._props["type"] = "streamtube"
        arg.pop("type", None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
