import os
import sys


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  # exc.info is a tuple which gives 3 values, we are ignoring the first two values and taking the third which is stored in exc_tb.
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = "error occured and the file name is [{0}] and the line number is [{1}] and error is [{2}]".format(filename,exc_tb.tb_lineno,str(error))

    return(error_message)



class SensorException(Exception):

    def __init__(self,error_message,error_detail:sys):

        super().__init__(error_message) # Super is used so that we can use Exception class, which is a concept of inheritense

        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message