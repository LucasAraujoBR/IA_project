import argparse
import json
from dataset import DataSet
from model import MEPModel

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the MEP model.\nExample: 'python -m mep.main datasets/data1.csv test.py", allow_abbrev=False)
    parser.add_argument("data_set_name", help="The name (full path) to the data file to train on.")
    parser.add_argument("python_file_name", help="The name (full path) to the python file to write the output program.")
    args = parser.parse_args()

    # get the data file
    data_set_name = args.data_set_name
    python_file_name = args.python_file_name
    data_set = DataSet(data_set_name)

    with open("mep/config/config.json") as config_file:
        config = json.load(config_file)


    model = MEPModel(int(config["num_constants"]), float(config["constants_min"]), float(config["constants_max"]),
                     float(config["feature_variables_probability"]), int(config["code_length"]),
                     int(config["population_size"]), float(config["operators_probability"]),
                     int(config["num_generations"]))
    model.fit(data_set.data_matrix, data_set.target)

    if python_file_name:
        python_program = model.to_python()
        with open(python_file_name, 'w') as python_file:
            python_file.write(python_program)

