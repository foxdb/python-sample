# uncomment if external packages are required
# init:
# 	pip install -r requirements.txt

test:
	python -m unittest -v tests

# python -m unittest -v tests.test_sample.TestSuite.test_if_true_is_true