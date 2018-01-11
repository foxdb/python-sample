# uncomment if external packages are required
# init:
# 	pip install -r requirements.txt

test:
	python -m unittest -v tests.unit_tests

# python -m unittest -v tests.tests_sample.BasicTestSuite.test_if_true_is_true