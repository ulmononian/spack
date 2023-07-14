# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class UfsHurricaneAppEnv(BundlePackage):
    """Development environment for the UFS Hurricane Application"""

    homepage = "https://github.com/hafs-community/HAFS"
    git = "https://github.com/hafs-community/HAFS.git"

    maintainers("ulmononian")

    version("1.0.0")

    depends_on("jasper")
    depends_on("zlib")
    depends_on("libpng")
    depends_on("hdf5")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("parallelio")
    depends_on("esmf")
    depends_on("mapl")
    depends_on("fms")
    depends_on("bufr")
    depends_on("bacio")
    depends_on("g2")
    depends_on("g2tmpl")
    depends_on("w3emc")
    depends_on("w3nco")
    depends_on("gftl-shared")
    depends_on("yafyaml")
    depends_on("prod_util")
    depends_on("grib_util")
    depends_on("wgrib2")
    depends_on("gempak")
    depends_on("szip")
    depends_on("sp")
    depends_on("ip")
    depends_on("sigio")
    depends_on("sfcio")
    depends_on("nemsio")
    depends_on("wrf-io")
    depends_on("crtm@2.4.0")
    depends_on("ncio")
    depends_on("nco")
    depends_on("cdo")
    depends_on("gsi-ncdiag")

    # There is no need for install() since there is no code.
