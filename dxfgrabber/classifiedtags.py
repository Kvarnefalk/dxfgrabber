# Purpose: handle classified tags
# Created: 21.07.2012, taken from my ezdxf project
# Copyright (C) 2012, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals
__author__ = "mozman <mozman@gmx.at>"

from .tags import Tags, StringIterator, DXFStructureError, DXFTag, NONE_TAG

APP_DATA_MARKER = 102
SUBCLASS_MARKER = 100
XDATA_MARKER = 1001


class ClassifiedTags:
    """ Manage Subclasses, AppData and Extended Data """

    def __init__(self, iterable=None):
        self.appdata = list()  # code == 102, keys are "{<arbitrary name>", values are Tags()
        self.subclasses = list()  # code == 100, keys are "subclassname", values are Tags()
        self.xdata = list()  # code >= 1000, keys are "APPNAME", values are Tags()
        if iterable is not None:
            self._setup(iterable)

    @property
    def noclass(self):
        return self.subclasses[0]

    def _setup(self, iterable):
        tagstream = iter(iterable)

        def collect_subclass(start_tag):
            """ a subclass can contain appdata, but not xdata, ends with
            SUBCLASSMARKER or XDATACODE.
            """
            data = Tags() if start_tag is None else Tags([start_tag])
            try:
                while True:
                    tag = next(tagstream)
                    if tag.code == APP_DATA_MARKER and tag.value[0] == '{':
                        app_data_pos = len(self.appdata)
                        data.append(DXFTag(tag.code, app_data_pos))
                        collect_appdata(tag)
                    elif tag.code in (SUBCLASS_MARKER, XDATA_MARKER):
                        self.subclasses.append(data)
                        return tag
                    else:
                        data.append(tag)
            except StopIteration:
                pass
            self.subclasses.append(data)
            return NONE_TAG

        def collect_appdata(starttag):
            """ appdata, can not contain xdata or subclasses """
            data = Tags([starttag])
            while True:
                try:
                    tag = next(tagstream)
                except StopIteration:
                    raise DXFStructureError("Missing closing DXFTag(102, '}') for appdata structure.")
                data.append(tag)
                if tag.code == APP_DATA_MARKER:
                    break
            self.appdata.append(data)

        def collect_xdata(starttag):
            """ xdata are always at the end of the entity and can not contain
            appdata or subclasses
            """
            data = Tags([starttag])
            try:
                while True:
                    tag = next(tagstream)
                    if tag.code == XDATA_MARKER:
                        self.xdata.append(data)
                        return tag
                    else:
                        data.append(tag)
            except StopIteration:
                pass
            self.xdata.append(data)
            return NONE_TAG

        tag = collect_subclass(None)  # preceding tags without a subclass
        while tag.code == SUBCLASS_MARKER:
            tag = collect_subclass(tag)
        while tag.code == XDATA_MARKER:
            tag = collect_xdata(tag)

        if tag is not NONE_TAG:
            raise DXFStructureError("Unexpected tag '%r' at end of entity." % tag)

    def __iter__(self):
        for subclass in self.subclasses:
            for tag in subclass:
                if tag.code == APP_DATA_MARKER and isinstance(tag.value, int):
                    for subtag in self.appdata[tag.value]:
                        yield subtag
                else:
                    yield tag

        for xdata in self.xdata:
            for tag in xdata:
                yield tag

    def get_subclass(self, name):
        for subclass in self.subclasses:
            if len(subclass) and subclass[0].value == name:
                return subclass
        raise KeyError("Subclass '%s' does not exist." % name)

    def get_xdata(self, appid):
        for xdata in self.xdata:
            if xdata[0].value == appid:
                return xdata
        raise ValueError("No extended data for APPID '%s'" % appid)

    def get_appdata(self, name):
        for appdata in self.appdata:
            if appdata[0].value == name:
                return appdata
        raise ValueError("Application defined group '%s' does not exist." % name)

    def get_type(self):
        return self.noclass[0].value

    @staticmethod
    def from_text(text):
        return ClassifiedTags(StringIterator(text))
