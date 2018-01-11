HOST=127.0.0.1

# uncomment if external packages are required
# init:
# 	pip install -r requirements.txt

test:
	# Run a full test suite
	python -m unittest -v tests.tests_sample
	# Run a precise test
	# python -m unittest -v tests.tests_sample.BasicTestSuite.test_if_true_is_true