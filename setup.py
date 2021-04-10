import setuptools

setuptools.setup(
    name="diagnose",
    version="1.0",
    author="Christopher Sullivan",
    author_email="csullivannet@users.noreply.github.com",
    description="Diagnoses issues with pods running on a kubernetes cluster",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["diagnose = diagnose.diagnose:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
