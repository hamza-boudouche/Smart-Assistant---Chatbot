import io
import json
from snips_nlu import SnipsNLUEngine

from nlu.helpers import NluModel

with io.open("./dataset2.json") as f:
    sample_dataset = json.load(f)

nlu_model = NluModel()
nlu_model.fitToData(sample_dataset)

parsed = nlu_model.parse(
    "get all the tasks due before next week that are assigned to hamza boudouche")

# "get all the tasks due before next week that are assigned to hamza boudouche"
# "can you insert a new task due next friday assigned to hamza boudouche"
print(json.dumps(parsing, indent=2))
