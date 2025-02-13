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
#     spack install py-trainax
#
# You can edit this file again by typing:
#
#     spack edit py-trainax
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyTrainax(PythonPackage, CudaPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://files.pythonhosted.org/packages/d3/f9/747a4d67dcbb0e6925a0902abf9239ba9f80aeb672501db416459e9c77ec/trainax-0.0.2-py3-none-any.whl"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("Ceyron")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.0.2", sha256="402a798beb17534c61ca383ce354a2325c395e8fe6125603a73cdc85f30b8f0c")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.8:3.12", type=("build", "run"))

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.

    # FIXME: Add additional dependencies if required.
    for arch in CudaPackage.cuda_arch_values:
        cuda_specs = f"cuda_arch={arch}"
        depends_on(f"py-jaxlib +cuda {cuda_specs}", type="run", when=f"{cuda_specs}")

    depends_on("py-jax@0.4.13:", type="run")
    depends_on("py-jaxtyping@0.2.20:", type="run")
    depends_on("py-typing-extensions@4.5.0:", type="run")
    depends_on("py-tqdm@4.63.2:", type="run")
    depends_on("py-optax@0.2.0:", type="run")
    depends_on("py-equinox@0.11.3:", type="run")
