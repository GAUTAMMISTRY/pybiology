import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Science/Research',
  "Operating System :: OS Independent",
  "License :: Freely Distributable",
  'Programming Language :: Python :: 3',
  "Programming Language :: Python :: 3.6",
  "Programming Language :: Python :: 3.7",
  "Programming Language :: Python :: 3.8",
  "Topic :: Scientific/Engineering",
  "Topic :: Scientific/Engineering :: Bio-Informatics",
  "Topic :: Software Development :: Libraries :: Python Modules",
]

setuptools.setup(
    name="pybiology", # GAUTAMMISTRY
    version="0.0.1",
    author="GAUTAM PARMAR",
    author_email="gautammistry48@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GAUTAMMISTRY/pybiology",
    packages=setuptools.find_packages(),
    classifiers=classifiers,
    python_requires='>=3.6',
)
