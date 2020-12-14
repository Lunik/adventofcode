import time
import warnings

def calculate_duration(func):
  start = time.time()
  result = func()
  duration = time.time() - start

  if duration > 1:
    warnings.warn(
      UserWarning(
        "Solution execution time is greater than 1 seconds. Duration :",
        duration))

  return result
