from hrtk.services.jamabandi_service import (
    JamabandiService,
)

from hrtk.repositories.jamabandi_repository import (
    JamabandiRepository,
)


def test_service_exists():

    repository = JamabandiRepository()

    service = JamabandiService(
        repository,
    )

    assert service is not None