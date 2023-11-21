# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAnsimarkup(PythonPackage):
    """Produce colored terminal text with an xml-like markup"""

    homepage = "https://github.com/gvalkov/python-ansimarkup"
    pypi = "ansimarkup/ansimarkup-2.1.0.tar.gz"

    maintainers("climbfuji")

    version("2.1.0", sha256="7b3e3d93fecc5b64d23a6e8eb96dbc8b0b576a211829d948afb397d241a8c51b")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-colorama", type=("build", "run"))
