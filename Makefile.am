# Copyright (c) 2020 Esrille Inc.
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

SUBDIRS = \
	icons \
	po \
	src\
	$(NULL)

EXTRA_DIST = \
	debian/backlight-gui.backlight-gui.udev \
	debian/changelog \
	debian/compat \
	debian/control \
	debian/copyright \
	debian/rules \
	debian/source/format \
	autogen.sh \
	CONTRIBUTING.md \
	COPYING \
	NOTICE\
	README.md \
	screenshot.png \
	$(NULL)

DISTCLEANFILES = \
	po/stamp-it \
	$(NULL)

uninstall-hook:
	-rmdir $(pkgdatadir)
