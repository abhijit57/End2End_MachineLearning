# This program creates custom exception handling

import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()    # Throws which file and which line an exception is occurring in
    file_name=exc_tb.tb_frame.f_code.co_filename    # Gets the file name
    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    


if __name__ == "__main__":

    try:
        a=1/0
    except Exception as e:
        logging.error("Divide by Zero Exception Error")
        raise CustomException(e, sys)