# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-pdequinox
#
# You can edit this file again by typing:
#
#     spack edit py-pdequinox
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPdequinox(PythonPackage, CudaPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://files.pythonhosted.org/packages/49/7e/e0d36d65a5495eb71e1a3ce2e5f2027f9b9c86d0ab2f41a43c2735f83ebb/pdequinox-0.1.2-py3-none-any.whl"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("Ceyron")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.1.2", sha256="b022b38eb03fa7ce4d20622cb9dd2b36f1b80730f082cd2b757279bb7d1111fa")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.8:3.12", type=("build", "run"))

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.

    # FIXME: Add additional dependencies if required.
    for arch in CudaPackage.cuda_arch_values:
        cuda_specs = f"+cuda cuda_arch={arch}"
        depends_on(f"py-jaxlib@0.4.13: {cuda_specs}", type="run", when=f"{cuda_specs}")

    depends_on("py-jax@0.4.13:", type="run")
    depends_on("py-jaxtyping@0.2.20:", type="run")
    depends_on("py-typing-extensions@4.5.0:", type="run")
    depends_on("py-equinox@0.11.3:", type="run")
