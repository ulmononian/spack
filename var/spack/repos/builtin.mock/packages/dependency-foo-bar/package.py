<<<<<<< HEAD
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
=======
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
>>>>>>> 29d784e5fa4651e3a47af766057ebc06ee558420
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class DependencyFooBar(Package):
    """This package has a variant "bar", which is False by default, and
    variant "foo" which is True by default.
    """

    homepage = "http://www.example.com"
    url = "http://www.example.com/dependency-foo-bar-1.0.tar.gz"

    version("1.0", md5="1234567890abcdefg1234567890098765")

    variant("foo", default=True, description="")
    variant("bar", default=False, description="")
