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
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk, Gio, GLib, Gtk, GObject

from window import Window

import gettext
import logging


_ = lambda a : gettext.dgettext(package.get_name(), a)
logger = logging.getLogger(__name__)


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         application_id="com.esrille.backlight-gui",
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
                         **kwargs)

        self.window = None
        self.brightness = None
        self.dec = None
        self.inc = None

        self.add_main_option("dec", 0, GLib.OptionFlags.NONE, GLib.OptionArg.INT, _("Decrease brightness"), _("percent"))
        self.add_main_option("inc", 0, GLib.OptionFlags.NONE, GLib.OptionArg.INT, _("Increase brightness"), _("percent"))
        self.add_main_option("set", 0, GLib.OptionFlags.NONE, GLib.OptionArg.INT, _("Set brightness"), _("percent"))

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)
        self.set_accels_for_action("app.quit", ["<Primary>q", "Escape", "Return"])

    def do_activate(self):
        logger.info('do_activate')
        print(self.window)
        if not self.window:
            self.window = Window(self,
                                 brightness=self.brightness, inc=self.inc, dec=self.dec)
            self.window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
            self.window.show_all()
        else:
            self.window.set_brightness(brightness=self.brightness, inc=self.inc, dec=self.dec)
        self.window.present()

    def do_command_line(self, command_line):
        # call the default commandline handler
        Gtk.Application.do_command_line(self, command_line)

        logger.info('do_command_line')
        options = command_line.get_options_dict()
        value = options.lookup_value('set', GLib.VariantType.new('i'))
        self.brightness = value.get_int32() if value else None
        value = options.lookup_value('ded', GLib.VariantType.new('i'))
        self.dec = value.get_int32() if value else None
        value = options.lookup_value('inc', GLib.VariantType.new('i'))
        self.inc = value.get_int32() if value else None

        args = command_line.get_arguments()[1:]
        if args:
            files = list()
            for pathname in args:
                files.append(command_line.create_file_for_arg(pathname))
            self.do_open(files, '')
        else:
            self.do_activate()
        return 0

    def do_open(self, files, *hint):
        logger.info('do_open')
        if self.window:
            if files:
                self.window.set_file(files[0])
        else:
            self.window = Window(self, files[0] if files else None,
                                 brightness=self.brightness, inc=self.inc, dec=self.dec)
            self.window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
            self.window.show_all()
        self.window.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def on_quit(self, *args):
        if self.window:
            self.window.destroy()
