#pyflyte run --remote flytetest.py my_workflow --a 10 --b 6
from flytekit import workflow
from flytekitplugins.domino.decorator import dominotask
import math

@dominotask(use_latest=True)
def add_numbers(first_value: int, second_value: int) -> int:
    return first_value + second_value

@dominotask(use_latest=True)
def square_root(value: int) -> float:
    return math.sqrt(value)

@workflow
def my_workflow(a: int, b: int) -> float:
    sum_result = add_numbers(first_value=a, second_value=b)
    return square_root(value=sum_result)