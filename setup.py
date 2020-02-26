from setuptools import setup, Extension

try:
    from Cython.Distutils import build_ext
except:
    use_cython = False
else:
    use_cython = True

cmdclass = {}
ext_modules = []

sources = []
if use_cython:
    sources = ["reeds_shepp/src/reeds_shepp.cpp", "reeds_shepp/reeds_shepp.pyx"]
    cmdclass.update({'build_ext': build_ext})
else:
    sources = ["reeds_shepp/src/reeds_shepp.cpp", "reeds_shepp/reeds_shepp.cpp"]

ext_modules = [
    Extension("reeds_shepp",
              sources=sources,
              language="c++",
              include_dirs=["reeds_shepp/include"])
]


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="reeds_shepp",
    version="1.0.7",
    description="Code to calculate analytic Reeds Shepp path",
    long_description=long_description,
    author="Gabel Liemann",
    author_email="troubleli233@gmail.com",
    url='https://github.com/liespace/pyReedsShepp',
    license="MIT",
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        'Topic :: Scientific/Engineering :: Mathematics'],
)
