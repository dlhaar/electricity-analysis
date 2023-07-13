import pandas as pd 
import yaml

def read_yaml(file_name:str):
	"""
	Function reads yaml file
	
	Input
	file: string with relative path of the yaml file

	example yaml str "./../config.yaml"

	"""

	try:
	    with open(file_name, 'r') as file: 
	        config = yaml.safe_load(file)
	    return config
	
	except Exception as e:
	    print('Error reading the config file')




if __name__=="__main__":

	read_yaml()