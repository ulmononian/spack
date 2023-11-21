# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCylcFlow(PythonPackage):
    """A workflow engine for cycling systems"""

    homepage = "https://cylc.github.io"
    pypi = "cylc-flow/cylc-flow-8.2.3.tar.gz"

    maintainers("climbfuji")

    version("8.2.3", sha256="dd5bea9e4b8dad00edd9c3459a38fb778e5a073da58ad2725bc9b84ad718e073")

    # Python dependencies
    depends_on("python@3.7:", type=("build", "run"))
    #tomli>=2; python_version < "3.11" - is the following correct?
    depends_on("py-tomli@2:", type="build", when="^python@:3.10")
    depends_on("py-ansimarkup@1:", type=("build", "run"))
    depends_on("py-async-timeout@3:", type=("build", "run"))
    depends_on("py-colorama@0.4:0", type=("build", "run"))
    depends_on("py-graphene@2.1:2", type=("build", "run"))
    depends_on("py-jinja2@3", type=("build", "run"))
    depends_on("py-metomi-isodatetime@3:3.1", type=("build", "run"))
    depends_on("py-protobuf@4.21.2:4.21", type=("build", "run"))
    depends_on("py-psutil@5.6:", type=("build", "run"))
    depends_on("py-pyzmq@22:", type=("build", "run"))
    depends_on("py-setuptools@49:", type="build")
    conflicts("py-setuptools@67")
    #importlib_metadata; python_version < "3.8" - is the following correct?
    depends_on("py-importlib-metadata", type=("build", "run"), when="^python@:3.7")
    depends_on("py-urwid@2", type=("build", "run"))
    depends_on("py-rx", type=("build", "run"))
    depends_on("py-promise", type=("build", "run"))

    # Non-Python dependencies
    depends_on("graphviz", type="run")
