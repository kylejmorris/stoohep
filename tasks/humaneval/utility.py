import numpy as np
from pebble import ThreadPool
import time

def utility(algorithm_str: str, test_cases: list):
    """
    Evaluates the algorithm based on human-labeled test cases.
    Each test case in the list should be a tuple (input, expected_output).
    The algorithm must be extremely fast. If it takes more than 500 milliseconds to run, it is a failure.
    Your algorithm function must be named 'algorithm' and take a single argument (input for the test case),
    and it should return the output that will be compared against the expected_output.
    """
    pool = ThreadPool()
    total_tests = len(test_cases)
    passed_tests = 0

    try:
        exec(algorithm_str, globals())
    except Exception as e:
        print(f"Error in loading algorithm: {e}")
        return 0

    for input, expected_output in test_cases:
        try:
            start_time = time.time()
            result_future = pool.schedule(algorithm, args=(input,))
            result = result_future.result(timeout=0.5)  # 500 milliseconds timeout
            total_time = time.time() - start_time

            if total_time > 0.5:
                continue  # Skip this test case as it took too long

            if result == expected_output:
                passed_tests += 1
        except Exception as e:
            print(f"Error during test case: {e}")

    correctness_score = passed_tests / total_tests
    return correctness_score

# Example usage
# test_cases = [((input1), expected_output1), ((input2), expected_output2), ...]
# utility_score = utility(algorithm_str, test_cases)
