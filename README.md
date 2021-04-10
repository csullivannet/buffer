# buffer

## Setting up your environment

### Prerequisites

This CLI tool was designed for use with python3. Please ensure you have python3
v3.9+ installed. [Get it here.](https://www.python.org/downloads/_

`pip` is also required. You probably already have it on your system, but just in
case you don't you can follow instructions on how to install it
[here](https://pip.pypa.io/en/stable/installing/). There may be other more
convenient options depending upon your operating system.

### Python Dependencies

Dependencies can be installed by running:

```
pip install --user pipenv
pipenv shell
pipenv install
```

### Installation

While in the virtualenv (activated with `pipenv shell`):

```
python3 setup.py install
```

You may now run the command `diagnose` within the python virtual environment.
This is the preferred approach as it is easier to clean up and control the
environment.

If desired, you may also place an alias to the binary on the PATH. While in the
virtualenv, run:

```
sudo ln -s $(which diagnose) /usr/local/bin/diagnose
```

You may also install globally in one step (available anywhere):

```
sudo python3 setup.py install
```

This method is not recommended as it is harder to clean up and has a higher risk
of mismatched dependencies with other tools and libraries.
