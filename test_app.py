import os
import pytest

import app


@pytest.fixture
def client():
    client = app.create_app()
    return client.test_client()


def test_simple(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"ok" in res.data
 
