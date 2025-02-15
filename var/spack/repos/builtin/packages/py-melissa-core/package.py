# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMelissaCore(PythonPackage, CudaPackage):
    """Melissa is a file-avoiding, adaptive, fault-tolerant and elastic
    framework, to run large-scale sensitivity analysis or deep-surrogate
    training on supercomputers.
    This package builds the launcher and server modules.
    """

    homepage = "https://gitlab.inria.fr/melissa/melissa"
    git = "https://gitlab.inria.fr/melissa/melissa.git"
    maintainers("abhishekp1297", "viperML", "raffino")

    license("BSD-3-Clause")

    version("develop", branch="develop", preferred=True)
    version("acdevelop", branch="active-sampling-develop")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # define variants for the deep learning server (torch, tf)
    variant(
        "torch", default=False, description="Install Deep Learning requirements with Pytorch only"
    )
    variant(
        "tf", default=True, when="~torch",
        description="Install Deep Learning requirements with TensorFlow only"
    )
    variant(
        "cuda", default=False,
        description="Install cuda and cudnn for the specified deep learning framework."
    )
    # ==============================
    #       Base dependencies
    # ==============================
    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools@46.4:", type="build")
    depends_on("py-pyzmq@22.3.0:", type="run")
    depends_on("py-mpi4py@3.1.3:3", type="run")
    depends_on("py-numpy@1.21:1", type="run")
    depends_on("py-jsonschema@4.5:", type="run")
    depends_on("py-python-rapidjson@1.8:", type="run")
    depends_on("py-scipy@1.10.0:1", type="run")
    depends_on("py-plotext@5.2.8:", type="run")
    depends_on("py-cloudpickle@2.2.0:", type="run")
    depends_on("py-iterative-stats@0.1:", type="run")
    depends_on("py-psutil@5:", type="run")
    # ==============================
    #       DL dependencies
    # ==============================
    depends_on("py-tensorboard@2.10.0:2", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-pandas", type="run")

    # by default, install tensorflow
    depends_on("py-tensorflow@2.8.0:2 ~cuda", type="run", when="+tf ~cuda")
    depends_on("py-torch@1.12.1:2 ~cuda", type="run", when="+torch ~cuda")

    # ==============================
    #       CUDA dependencies
    # ==============================
    conflicts(
        "+tf +torch +cuda",
        msg="TensorFlow and PyTorch cannot both be enabled with CUDA due to compatibility issues. "
        "Try to disable one of them."
    )
    for arch in CudaPackage.cuda_arch_values:
        # Support beyond ampere (A100) GPUs hasn't been tested yet.
        if arch.isdigit() and 60 <= int(arch) <= 80:
            cuda_specs = f"+cuda cuda_arch={arch}"
            depends_on(f"nccl {cuda_specs}", when=cuda_specs)
            depends_on(f"py-torch@1.12.1:2 {cuda_specs}", type="run", when=f"+torch {cuda_specs}")
            depends_on(f"py-tensorflow@2.8.0:2 {cuda_specs}", type="run", when=f"+tf {cuda_specs}")
        else:
            conflicts(
                f"+cuda cuda_arch={arch}",
                msg="Support beyond Ampere GPUs has not been tested yet. "
                "Accepted values are between 60 and 80 inclusive."
            )
