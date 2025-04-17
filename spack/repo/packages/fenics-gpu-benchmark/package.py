# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class FenicsGpuBenchmark(CMakePackage, CudaPackage, ROCmPackage):
    "A weak-scaling performance test for the FEniCS Finite Element Package with GPU support"

    homepage = "https://github.com/ukri-bench/fenics-benchmark"
    git = "https://github.com/ukri-bench/fenics-benchmark.git"

    depends_on("fenics-dolfinx@main")
    depends_on("py-fenics-ffcx@main", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-fenics-ufl@main", type="build")
    depends_on("mpi")
    depends_on("hip", when="+rocm")
    depends_on("cuda", when="+cuda")

    conflicts("+cuda", when="+rocm", msg="Cannot build for both ROCm and CUDA")

    variant("fp32", default=False, description="Build for float32 scalar type")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with when("+rocm"):
        depends_on("rocm-core")
        depends_on("rocsparse")
        depends_on("rocrand")
        depends_on("rocthrust")
        depends_on("rocprim")

    version("main", tag="main")

    def cmake_args(self):
        args = [self.define("SCALAR_TYPE", "float32" if "+fp32" in self.spec else "float64")]
        if "+rocm" in self.spec:
            args += [self.define("HIP_ARCH", self.spec.variants["amdgpu_target"].value)]
        if "+cuda" in self.spec:
            args += [self.define("CUDA_ARCH", self.spec.variants["cuda_arch"].value)]
        return args
