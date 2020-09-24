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

import logging
import os
from pathlib import Path


logger = logging.getLogger(__name__)


SYS_CLASS_PATH = '/sys/class/backlight'


class Backlight:
    def __init__(self, path):
        if not path:
            controllers = self.get_controllers()
            if controllers:
                path = controllers[0]
        if path:
            self.path = Path(path)
        else:
            self.path = None
            logger.error("No backlight device")

    def get_brightness(self):
        try:
            return int((self.path / 'brightness').read_text())
        except Exception as e:
            logger.error(e)
        return 0

    def set_brightness(self, value):
        try:
            (self.path / 'brightness').write_text(str(value))
        except Exception as e:
            logger.error(e)

    def get_controllers(self):
        controllers = list()
        for name in os.listdir(SYS_CLASS_PATH):
            controllers.append(os.path.join(SYS_CLASS_PATH, name))
        return controllers

    def get_max_brightness(self):
        try:
            return int((self.path / 'max_brightness').read_text())
        except Exception as e:
            logger.error(e)
        return 0

    def set_path(self, path):
        if path:
            self.path = Path(path)
