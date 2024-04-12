import pytest
from stuff.accum import Accumulator
@pytest.fixture
def accum(scope = 'function'):
    yield Accumulator() # Generator - everything before will be the setup
    print("DONE with the test!")#Everyting after will be the cleanup steps

@pytest.fixture
def accum2():
    return Accumulator()

#python3 -m pytest --verbose gives more information about the tests
#python -m pytest --maxfail=1
#python -m pytest --junit-xml report.xml

#Filtering Tests
#python3 -m pytest tests/test_accum.py
#python3 - m pytest -k one to filter tests to a filter
#markers are tags for tests
#@pytest.mark.skip skips a test case

#A plugin is an optional package that adds new capabilities to the framework
#pip3 install pytest-html
#python3 -m pytest --html=report.html

#pip3 install pytest-cov
#python3 -m pytest --cov
#python3 -m pytest --cov=stuff --cov-report html
# The obove statemetn is found in htmlcov/index.html

#python3 -m pytest --cov=stuff --cov-branch

#pip3 install pytest-xdist
#Running test suites in parellel makes it faster with the above statement
#python3 -m pytest -n 3

#pytest bdd - behavior-driven development


