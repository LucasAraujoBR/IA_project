import argparse
import json
from dataset import DataSet
from model import MEPModel

if __name__ == "__main__":
    # get the data file
    data_set_name = "IA_project\datasets\sertanejo.csv"
    python_file_name = "pythonResposta.py"
 
    with open("IA_project/config/config.json") as config_file:
        config = json.load(config_file)

    data_set = DataSet(data_set_name, config['number_of_partitions'])

    model = MEPModel(float(config["feature_variables_probability"]), int(config["code_length"]),
                     int(config["population_size"]), float(config["operators_probability"]),
                     int(config["num_generations"]))
    model.fit(data_set.data_matrix, data_set.target)

    if python_file_name:
        python_program = model.to_python()
        with open(python_file_name, 'w') as python_file:
            python_file.write(python_program)

