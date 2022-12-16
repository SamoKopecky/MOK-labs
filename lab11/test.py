import ex1

import numpy as np
import pytest


@pytest.mark.parametrize(
    "lang,expected",
    [
        ('CZE', np.array([3339, 4766, 3353, 1604, 1731, 1444, 1061, 1408])),
        ('GRE', np.array([6558.8, 6857.7, 6466.2, 1203.0, 1206.0, 1441.0, 743.0, 1189.0])),
        ('BUL', np.array([322, 534, 1021, 283, 236, 304, 288, 87])),
    ],
)
def test_students_per_year(lang: str, expected):
    data = ex1.load_dataset()

    students_per_year = ex1.students_per_year(data, lang)

    np.testing.assert_almost_equal(students_per_year, expected, decimal=1)