from unittest.mock import patch


def test_home_route_returns_200(test_api):

    response = test_api.get("/")

    assert response.status_code == 200


"""
Scenarios:

- It's an actual company
- It's a dict
- It's a dict with the correct keys
- The route returns 200
- If we call it a bunch of times, it's not always the same
"""


@patch("main.load_companies")
def test_companies_random_route_returns_from_data(fake_load_companies, test_api):

    # Set up a magic mock so that it returns a controlled list of companies
    fake_company_list = [{"id": 1}, {"id": 2}]
    fake_load_companies.return_value = fake_company_list

    # Attempt to get a random one
    response = test_api.get("/company/random")
    data = response.json

    # Check that the result is one of the controlled list
    assert data in fake_company_list


@patch("main.load_companies")
def test_companies_random_route_returns_different_things_sometimes(fake_load_companies, test_api):

    # Set up a magic mock so that it returns a controlled list of companies
    fake_company_list = [{"id": 1}, {"id": 2}]
    fake_load_companies.return_value = fake_company_list

    # Attempt to get random options a bunch of times
    results = []
    for i in range(100):
        response = test_api.get("/company/random")
        data = response.json
        results.append(data["id"])

    assert len(set(results)) != 1


@patch("main.add_new_company")
@patch("main.load_companies")
def test_companies_rejects_invalid_with_400(fake_load, fake_add, test_api):

    # Set up the mocks
    fake_add.return_value = {}

    # Access the API
    response = test_api.post("/company", json={})

    assert response.status_code == 400
    assert "error" in response.json
    assert response.json["error"]


@patch("main.is_valid_company")
@patch("main.add_new_company")
@patch("main.load_companies")
def test_companies_calls_add_new_on_valid(fake_load, fake_add, fake_is_valid, test_api):

    # Set up the mocks
    fake_add.return_value = {}
    fake_is_valid.return_value = True

    # Access the API
    response = test_api.post("/company", json={})

    assert fake_add.call_count == 1
