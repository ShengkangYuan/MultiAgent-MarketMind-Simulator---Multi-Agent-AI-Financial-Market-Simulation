import io
import os
import re

import setuptools


def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "description.txt"), encoding="utf-8") as f:
        return f.read()


def _parse_requirements(filename):
    """Return package specs from a pip requirements file.

    Skips comments, blank lines and pip directives (``-r`` / ``-e``)
    which are not valid entries for setuptools ``install_requires``.
    """
    reqs = []
    with open(filename, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith(("-r", "-e")):
                continue
            reqs.append(line)
    return reqs


def get_requirements():
    """Core runtime requirements (see requirements.txt)."""
    return _parse_requirements("requirements.txt")


def get_rag_requirements():
    """Optional RAG extras (llama-index stack, see requirements-rag.txt)."""
    return _parse_requirements("requirements-rag.txt")


def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, "masim", "__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


setuptools.setup(
    name="multiagent-simulation",
    version=get_version(),
    author="",
    license="Apache-2.0",
    description="Packaged version of financial trend tracer for visual language models",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/AgenticFinLab/multiagent-simulation",
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.11,<3.14",
    install_requires=get_requirements(),
    extras_require={
        "tests": ["pytest"],
        "rag": get_rag_requirements(),
    },
    include_package_data=True,
    options={"bdist_wheel": {"python_tag": "py311"}},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="multiagent, simulation, large language models",
)
