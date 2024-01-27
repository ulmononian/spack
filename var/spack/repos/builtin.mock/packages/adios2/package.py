<<<<<<< HEAD
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
=======
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
>>>>>>> 29d784e5fa4651e3a47af766057ebc06ee558420
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Adios2(Package):
    """This packagae has the variants shared and
    bzip2, both defaulted to True"""

    homepage = "https://example.com"
    url = "https://example.com/adios2.tar.gz"

    version("2.9.1", sha256="ddfa32c14494250ee8a48ef1c97a1bf6442c15484bbbd4669228a0f90242f4f9")

    variant("shared", default=True, description="Build shared libraries")
    variant("bzip2", default=True, description="Enable BZip2 compression")

    depends_on("bzip2")
