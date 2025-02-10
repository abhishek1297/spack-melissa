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

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # define variants for the deep learning server (torch, tf)
    variant(
        "torch", default=False, description="Install Deep Learning requirements with Pytorch only"
    )
    variant(
        "tf", default=False, description="Install Deep Learning requirements with TensorFlow only"
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
    depends_on("py-tensorboard@2.10.0:2", type="run", when="+torch")
    depends_on("py-tensorboard@2.10.0:2", type="run", when="+tf")
    depends_on("py-matplotlib", type="run", when="+torch")
    depends_on("py-matplotlib", type="run", when="+tf")
    depends_on("py-pandas", type="run", when="+torch")
    depends_on("py-pandas", type="run", when="+tf")

    depends_on("py-torch@1.12.1:2", type="run", when="+torch")
    depends_on("py-tensorflow@2.8.0:2", type="run", when="+tf")

    # ==============================
    #       CUDA dependencies
    # ==============================
    for arch in CudaPackage.cuda_arch_values:
        cuda_specs = f"+cuda cuda_arch={arch}"
        depends_on(f"nccl {cuda_specs}", when=cuda_specs)
        depends_on(f"py-torch@1.12.1:2 {cuda_specs}", type="run", when=f"+torch {cuda_specs}")
        depends_on(f"py-tensorflow@2.8.0:2 {cuda_specs}", type="run", when=f"+tf {cuda_specs}")
