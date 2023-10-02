(installation)=

# Installation Guide

## Using pip

The easiest way to install the most recent stable version of release-tutorial
is with [pip](https://pip.pypa.io):

```bash
python -m pip install release-tutorial
```

## From source

Alternatively, you can get the source:

```bash
git clone https://github.com/emolter/release-tutorial
cd tinygp
python -m pip install -e .
```

## Tests

If you installed from source, you can run the unit tests. From the root of the
source directory, run:

```bash
python -m pip install nox
python -m nox -s tests
```
