# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMepo(PythonPackage):
    """Tool to manage (m)ultiple git r(epo)sitories"""

    homepage = "https://github.com/GEOS-ESM/mepo"
    url = "https://github.com/GEOS-ESM/mepo/archive/refs/tags/v1.51.1.tar.gz"

    maintainers("mathomp4", "climbfuji")

    version("1.51.1", sha256="543c1e7487afb2d62e5e8c8a2f69a85af1b1951f588f3dfc7471763e90847360")

    depends_on("py-pyyaml@5.4:", type=("build", "run"))
