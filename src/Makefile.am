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

backlight_PYTHON = \
	application.py \
	main.py \
	backlight.py \
	window.py \
	$(NULL)
BUILT_SOURCES = package.py
nodist_backlight_PYTHON = package.py
backlightdir = $(pkgdatadir)/src

bin_SCRIPTS = backlight-gui

dist_desktop_DATA = backlight-gui.desktop
desktopdir = $(datadir)/applications

CLEANFILES = \
	backlight-gui \
	backlight-gui.in \
	package.py \
	package.py.in \
	$(NULL)

EXTRA_DIST = \
	backlight-gui.in.in \
	package.py.in.in \
	$(NULL)

package.py: package.py.in
	$(AM_V_GEN) \
	( \
		pkgdatadir=${pkgdatadir}; \
		localedir=${localedir}; \
		s=`cat $<`; \
		eval "echo \"$${s}\""; \
	) > $@

backlight-gui: backlight-gui.in
	$(AM_V_GEN) \
	( \
		pkgdatadir=${pkgdatadir}; \
		s=`cat $<`; \
		eval "echo \"$${s}\""; \
	) > $@
	chmod +x $@

uninstall-hook:
	-rmdir $(backlightdir)/__pycache__
	-rmdir $(backlightdir)
