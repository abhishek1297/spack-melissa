# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Melissa(CMakePackage):
    """Melissa is a file-avoiding, adaptive, fault-tolerant and elastic
    framework, to run large-scale sensitivity analysis on supercomputers.
    """

    homepage = "https://gitlab.inria.fr/melissa/melissa"
    git = "https://gitlab.inria.fr/melissa/melissa.git"
    # attention: Git**Hub**.com accounts
    maintainers("abhishekp1297", "viperML", "raffino")

    version("develop", branch="develop", preferred=True)

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.15:", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("libzmq@4.2:4", type=("build", "run"))
    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("mpi", type=("build", "run"))
