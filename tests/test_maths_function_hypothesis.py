# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import project.complicated_maths_functions as cmf
from hypothesis import given, strategies as st


@given(a=st.floats(), b=st.floats(), c=st.floats(), d=st.floats())
def test_fuzz_run_complicated_maths_function_1(
    a: float, b: float, c: float, d: float
) -> None:
    cmf.run_complicated_maths_function_1(a=a, b=b, c=c, d=d)


@given(a=st.floats(), b=st.floats(), c=st.floats(), d=st.floats())
def test_fuzz_run_complicated_maths_function_2(
    a: float, b: float, c: float, d: float
) -> None:
    cmf.run_complicated_maths_function_2(a=a, b=b, c=c, d=d)


@given(a=st.floats(), b=st.floats(), c=st.floats(), d=st.floats())
def test_fuzz_run_complicated_maths_function_3(
    a: float, b: float, c: float, d: float
) -> None:
    cmf.run_complicated_maths_function_3(a=a, b=b, c=c, d=d)


@given(a=st.floats(), b=st.floats(), c=st.floats(), d=st.floats())
def test_fuzz_run_complicated_maths_function_4(
    a: float, b: float, c: float, d: float
) -> None:
    cmf.run_complicated_maths_function_4(a=a, b=b, c=c, d=d)
