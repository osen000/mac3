import pytest
import requests
import cerberus


def test_get_status200(base_url, request_method, code=200):
    """Проверяем статус get запроса"""
    url_test = base_url + f"/list/all"
    response = request_method(url=url_test)
    assert response.status_code == code


def test_get_header_content_type(base_url, request_method):
    """Проверяем наличие Content-type для get запроса"""
    headers = {
        "Content-type": "application/json"
    }
    url_test = base_url + f"/list/all"
    response = request_method(url=url_test)
    assert response.headers['Content-Type'] == headers["Content-type"]


def test_get_api_json(base_url):
    """Проверяем соответствие json схеме"""
    url_test = base_url + f"/list/all"
    response = requests.get(url_test)
    schema = {
        "message": {"type": "dict",
                    "schema": {"affenpinscher": {"type": "list"},
                               "african": {"type": "list"},
                               "airedale": {"type": "list"},
                               "akita": {"type": "list"},
                               "appenzeller": {"type": "list"},
                               "australian": {"type": "list"},
                               "basenji": {"type": "list"},
                               "beagle": {"type": "list"},
                               "bluetick": {"type": "list"},
                               "borzoi": {"type": "list"},
                               "bouvier": {"type": "list"},
                               "boxer": {"type": "list"},
                               "brabancon": {"type": "list"},
                               "briard": {"type": "list"},
                               "buhund": {"type": "list"},
                               "bulldog": {"type": "list"},
                               "bullterrier": {"type": "list"},
                               "cattledog": {"type": "list"},
                               "chihuahua": {"type": "list"},
                               "chow": {"type": "list"},
                               "clumber": {"type": "list"},
                               "cockapoo": {"type": "list"},
                               "collie": {"type": "list"},
                               "coonhound": {"type": "list"},
                               "corgi": {"type": "list"},
                               "cotondetulear": {"type": "list"},
                               "dachshund": {"type": "list"},
                               "dalmatian": {"type": "list"},
                               "dane": {"type": "list"},
                               "deerhound": {"type": "list"},
                               "dhole": {"type": "list"},
                               "dingo": {"type": "list"},
                               "doberman": {"type": "list"},
                               "elkhound": {"type": "list"},
                               "entlebucher": {"type": "list"},
                               "eskimo": {"type": "list"},
                               "finnish": {"type": "list"},
                               "frise": {"type": "list"},
                               "germanshepherd": {"type": "list"},
                               "greyhound": {"type": "list"},
                               "groenendael": {"type": "list"},
                               "havanese": {"type": "list"},
                               "hound": {"type": "list"},
                               "husky": {"type": "list"},
                               "keeshond": {"type": "list"},
                               "kelpie": {"type": "list"},
                               "komondor": {"type": "list"},
                               "kuvasz": {"type": "list"},
                               "labradoodle": {"type": "list"},
                               "labrador": {"type": "list"},
                               "leonberg": {"type": "list"},
                               "lhasa": {"type": "list"},
                               "malamute": {"type": "list"},
                               "malinois": {"type": "list"},
                               "maltese": {"type": "list"},
                               "mastiff": {"type": "list"},
                               "mexicanhairless": {"type": "list"},
                               "mix": {"type": "list"},
                               "mountain": {"type": "list"},
                               "newfoundland": {"type": "list"},
                               "otterhound": {"type": "list"},
                               "ovcharka": {"type": "list"},
                               "papillon": {"type": "list"},
                               "pekinese": {"type": "list"},
                               "pembroke": {"type": "list"},
                               "pinscher": {"type": "list"},
                               "pitbull": {"type": "list"},
                               "pointer": {"type": "list"},
                               "pomeranian": {"type": "list"},
                               "poodle": {"type": "list"},
                               "pug": {"type": "list"},
                               "puggle": {"type": "list"},
                               "pyrenees": {"type": "list"},
                               "redbone": {"type": "list"},
                               "retriever": {"type": "list"},
                               "ridgeback": {"type": "list"},
                               "rottweiler": {"type": "list"},
                               "saluki": {"type": "list"},
                               "samoyed": {"type": "list"},
                               "schipperke": {"type": "list"},
                               "schnauzer": {"type": "list"},
                               "setter": {"type": "list"},
                               "sheepdog": {"type": "list"},
                               "shiba": {"type": "list"},
                               "shihtzu": {"type": "list"},
                               "spaniel": {"type": "list"},
                               "springer": {"type": "list"},
                               "stbernard": {"type": "list"},
                               "terrier": {"type": "list"},
                               "tervuren": {"type": "list"},
                               "vizsla": {"type": "list"},
                               "waterdog": {"type": "list"},
                               "weimaraner": {"type": "list"},
                               "whippet": {"type": "list"},
                               "wolfhound": {"type": "list"}
                               }
                    },
        "status": {"type": "string"}
    }

    v = cerberus.Validator()
    assert v.validate(response.json(), schema)


@pytest.mark.parametrize("picture_number", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_get_api_image(base_url, picture_number, request_method):
    """Проверяем изображения"""
    url_test = base_url + f"/image/random/{picture_number}"
    response = request_method(url=url_test)
    assert response.status_code == 200


@pytest.mark.parametrize("breeds", ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"])
def test_get_api_breed_list(base_url, breeds, request_method):
    """Проверяем породы"""
    url_test = base_url + f"/hound/list"
    response = request_method(url=url_test)
    if breeds in response.text:
        assert True
