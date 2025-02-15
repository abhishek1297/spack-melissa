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
#     spack install py-exponax
#
# You can edit this file again by typing:
#
#     spack edit py-exponax
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyExponax(PythonPackage, CudaPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://files.pythonhosted.org/packages/9f/a3/481311930def9fe06b53694afb0172b15d3134cbc38929978e012d5165f8/exponax-0.1.0-py3-none-any.whl"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("Ceyron")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.1.0", sha256="a8033244769c2cb126a700aa9f39d4d793ba25ed2c9d0bc1fa81c96ba277b770")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.10:3.12", type=("build", "run"))

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # FIXME: Add additional dependencies if required.
    for arch in CudaPackage.cuda_arch_values:
        cuda_specs = f"+cuda cuda_arch={arch}"
        depends_on(f"py-jaxlib@0.4.13: {cuda_specs}", type="run", when=f"{cuda_specs}")

    depends_on("py-jax@0.4.13:", type="run")
    depends_on("py-jaxtyping@0.2.20:", type="run")
    depends_on("py-typing-extensions@4.5.0:", type="run")
    depends_on("py-matplotlib@3.8.1:", type="run")
    depends_on("py-equinox@0.11.3:", type="run")
