import json
import azure.functions as func
from function_app import hello


def test_hello_with_name():
    req = func.HttpRequest(
        method="GET", url="/api/hello", params={"name": "Pardhu"}, body=b""
    )
    response = hello(req)

    assert response.status_code == 200
    assert json.loads(response.get_body()) == {"message": "Hello, Pardhu!"}


def test_hello_without_name():
    req = func.HttpRequest(
        method="GET", url="/api/hello", params={}, body=b""
    )
    response = hello(req)

    assert json.loads(response.get_body()) == {"message": "Hello, World!"}
