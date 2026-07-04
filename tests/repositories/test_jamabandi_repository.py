from hrtk.repositories.jamabandi_repository import (
    JamabandiRepository,
)


def test_repository_exists():

    repository = JamabandiRepository()

    assert repository is not None