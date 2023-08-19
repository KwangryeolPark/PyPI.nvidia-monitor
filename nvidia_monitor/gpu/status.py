import os
import subprocess
import csv
from queries import STATUS_QUERY


class Status(object):
    def __init__(
        self
    ):
        self._str_query = self._get_status_query()
        
    def _get_status_query(
        self,
    )->str:
        _str_query = ','.join(STATUS_QUERY)
        _str_query = f"nvidia-smi --query-gpu={_str_query} --format=csv"
        return _str_query
    
    def get_gpu_status(
        self,
        verbose:bool=False
    )->list:
        outputs = subprocess.check_output(self._str_query, shell=True)
        outputs = outputs.decode('utf-8')
        if verbose:
            print(outputs)
        
        outputs = outputs.split('\n')[:-1]
        outputs = [output.split(',') for output in outputs]
        queries = STATUS_QUERY  # outputs[0]
        outputs = outputs[1:]
        
        dict_outputs = []
        for output in outputs:
            dict_output = {}
            for query, value in zip(queries, output):
                dict_output[query] = value.strip()
            dict_outputs.append(dict_output)
        
        return dict_outputs
