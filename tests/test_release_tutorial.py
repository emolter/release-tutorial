import release_tutorial


def test_release_tutorial_version():
    from importlib.metadata import version

    assert release_tutorial.__version__ == version("release_tutorial")
