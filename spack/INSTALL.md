# Spack installation

## Pre-requisites

* spack - downloaded from [github.com/spack/spack](https://github.com/spack/spack)

## Build instructions

It is recommended to use a **spack environment** to build the benchmark,
adding the supplemental repository from this directory, which
contains the package definition.

```
spack env create fenics-benchmark
spack env activate fenics-benchmark
spack repo add ./repo
```

It may be necessary to add extra configuration for the machine you are
running on, including specifying compilers and external libraries
(e.g. MPI). See the [spack
documentation](https://spack.readthedocs.io/en/latest/) for details on
how to do this.

Add the benchmark to the environment, e.g. for NVIDIA A100 use:

`spack add fenics-gpu-benchmark+cuda cuda_arch=80`

and for AMD MI250X use:

`spack add fenics-gpu-bencmark+rocm amdgpu_target=gfx90a`

followed by `spack install`. Once installed, the tests can be run as
described in the main README. For 32-bit floating point builds, add the flag `+fp32` to the spack specification.

### Note

The spack installation is under development. If you have any problems, please report them in the issue tracker.
