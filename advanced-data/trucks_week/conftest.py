from pytest import fixture

import pandas as pd

@fixture
def fixed_number():
    return 1

@fixture
def give_panda():
    data = {
        'ID': [101, 102, 103, 104],
        'Score': [88, 92, 79, 85],
        'Passed': [True, True, False, True]
    }
    return pd.DataFrame(data)