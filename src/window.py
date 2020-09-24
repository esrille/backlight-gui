#
# Copyright (c) 2020  Esrille Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <http://www.gnu.org/licenses/>.

import package

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backlight import Backlight

import gettext
import logging


_ = lambda a : gettext.dgettext(package.get_name(), a)
logger = logging.getLogger(__name__)

DEFAULT_WIDTH = 320
DEFAULT_HEIGHT = 72
NDEBUG = True


class Window(Gtk.ApplicationWindow):

    def __init__(self, app, file=None, brightness=None, inc=None, dec=None):
        super().__init__(application=app, title=_("Backlight"))
        self.set_default_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        self.set_default_icon_name(package.get_name())
        self.backlight = Backlight(file.get_path() if file else None)
        if NDEBUG:
            max_brightness = self.backlight.get_max_brightness()
        else:
            max_brightness = 255
        overlay = Gtk.Overlay()
        self.add(overlay)
        try:
            self.scale = Gtk.Scale.new(Gtk.Orientation.HORIZONTAL, None)
            self.scale.set_draw_value(False)
            self.scale.set_range(1, max_brightness)
            self.scale.set_increments(1, max(int(max_brightness / 10), 1))
            self.scale.set_round_digits(0)
            self.set_brightness(brightness, inc, dec)
            self.scale.connect('value-changed', self.value_changed_callback)
            overlay.add(self.scale)
        except Exception as e:
            pass

    def set_brightness(self, brightness=None, inc=None, dec=None):
        logger.info("set_brightness")
        if NDEBUG:
            max_brightness = self.backlight.get_max_brightness()
        else:
            max_brightness = 255
        if brightness is None:
            brightness = self.backlight.get_brightness()
        else:
            brightness = max_brightness * brightness / 100
        if inc:
            logger.info("inc %d", inc)
            brightness += max_brightness * inc / 100
        if dec:
            logger.info("dec %d", dec)
            brightness -= max_brightness * dec / 100
        brightness = int(min(max(0, brightness), max_brightness))
        self.backlight.set_brightness(brightness)
        self.scale.set_value(brightness)
        return brightness

    def set_file(self, file):
        self.backlight.set_path(file.get_path())
        max_brightness = self.backlight.get_max_brightness()
        self.scale.set_range(1, max_brightness)
        self.scale.set_increments(1, max(int(max_brightness / 10), 1))
        self.scale.set_value(self.backlight.get_brightness())

    def value_changed_callback(self, range):
        print(int(range.get_value()))
        self.backlight.set_brightness(int(range.get_value()))
