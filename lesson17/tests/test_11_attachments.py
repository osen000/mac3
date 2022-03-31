import allure
import pytest


@pytest.fixture
def attach_file(request):
    allure.attach(
        body='A text attachment init',
        name='init attach',
        attachment_type=allure.attachment_type.TEXT
    )

    def fin():
        allure.attach(
            body='A text attacment finalizer',
            name='finalizer attach',
            attachment_type=allure.attachment_type.TEXT
        )
    request.addfinalizer(fin)


def test_with_attachments_in_fixture(attach_file):
    pass


def test_multiple_attachments():
    allure.attach.file(
        source='data/snake.jpg',
        attachment_type=allure.attachment_type.JPG
    )
    allure.attach(
        body='<head></head><body> a page </body>',
        name='Attach with HTML type',
        attachment_type=allure.attachment_type.HTML
    )
