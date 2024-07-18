from sensor.exception import SensorException 
from sensor.logger import logging
import os
import sys

def test_exception():
    try:
        logging.info("This is 1 divided by 0 error bro...")
        a = 1/0
    except Exception as e:
        raise SensorException(e,sys)
      


if __name__ == "__main__":  # module execution control/ to prevent execution on import 
    try:
       test_exception()
    except SensorException as e:
       print(e)
 
