#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import project_add


@project_add
class Glibmm(Tarball, Meson):
    def __init__(self):
        Meson.__init__(
            self,
            "glibmm",
            prj_dir="glibmm",
            version="2.76.0",
            lastversion_even=True,
            repository="https://gitlab.gnome.org/GNOME/glibmm",
            archive_url="https://download.gnome.org/sources/glibmm/{major}.{minor}/glibmm-{version}.tar.xz",
            hash="8637d80ceabd94fddd6e48970a082a264558d4ab82684e15ffc87e7ef3462ab2",
            dependencies=[
                "meson",
                "ninja",
                "libsigc++",
            ],
        )

    def build(self):
        Meson.build(
            self,
            meson_params="-Dbuild-examples=false -Dbuild-documentation=false",
        )

        self.install(r".\COPYING share\doc\glibmm")
