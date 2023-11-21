# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMetomiIsodatetime(PythonPackage):
    """Python ISO 8601 date time parser and data model/manipulation utilities"""

    homepage = "https://github.com/metomi/isodatetime"
    pypi = "metomi-isodatetime/metomi-isodatetime-1!3.1.0.tar.gz"

    maintainers("climbfuji")

    version("3.1.0", sha256="2ec15eb9c323d5debd0678f33af99bc9a91aa0b534ee5f65f3487aed518ebf2d")
    depends_on("py-setuptools", type="build")
