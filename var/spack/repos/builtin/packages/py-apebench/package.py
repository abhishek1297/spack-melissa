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
#     spack install py-apebench
#
# You can edit this file again by typing:
#
#     spack edit py-apebench
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyApebench(PythonPackage, CudaPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://files.pythonhosted.org/packages/36/6c/811b2dd61da9caecbb9b967dab09314303274ec08e3ed77143098070c438/apebench-0.1.1-py3-none-any.whl"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("Ceyron")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.1.1", sha256="ad06abd3adfc4aa9c497a53650bc5eed86abe56ab24c7c523a31cd6ef9278731")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.10:3.12", type=("build", "run"))

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
    depends_on("py-matplotlib@3.8.1:", type="run")
    depends_on("py-pandas@2.2.0:", type="run")
    depends_on("py-seaborn@0.13.0:", type="run")
    depends_on("py-optax@0.2.0:", type="run")
    # specific to apebench
    for c in ["~cuda", "+cuda"]:
        depends_on(f"py-equinox@0.11.3 {c}", type="run", when=c)
        depends_on(f"py-exponax@0.1.0 {c}", type="run", when=c)
        depends_on(f"py-pdequinox@0.1.2 {c}", type="run", when=c)
        depends_on(f"py-trainax@0.0.2 {c}", type="run", when=c)
