from unittest.mock import MagicMock

from main import get_bucket_names


def test_get_bucket_names_returns_list_of_strings():

    fake_s3 = MagicMock()
    fake_s3.list_buckets.return_value = {
        "Buckets": [
            { "Name": "A" },
            { "Name": "B" },
        ]
    }

    result = get_bucket_names(s3_client=fake_s3)

    assert isinstance(result, list)
    assert all(isinstance(x, str) for x in result)