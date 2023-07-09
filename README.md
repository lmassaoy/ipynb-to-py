# ipynb to py

Export python script from Jupyter Notebook to runnable .py file

## Set up

### Collecting data from the notebooks' cells 

To make the cells of your notebook extractable to the Python file, remember to put a commentary as the following example:
```
# export to .py
from pyspark.sql import *
from pyspark.sql.functions import *
```

### Configuring the commentary string in the converter

Rename the value of the variable `export_line`:
```
export_line = '# export to .py\n'
```

### Configuring output directory

Rename the value of the variable `output_dir`:
```
output_dir = './output'
```

## Running

To execute this converter, just run the job with the list of notebooks for convertion as the arguments:
```
$ python3 converter.py notebook_number_one.ipynb notebook_number_two.ipynb notebook_number_etc.ipynb
```