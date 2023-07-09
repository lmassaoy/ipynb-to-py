import json
import os
import sys


export_line = '# export to .py\n'
output_dir = './output'


class MissingNotebooksException(Exception):
    "Raised when no notebooks were informed in the arguments"
    pass


def main(notebooks):
    try:
        if len(notebooks) == 0:
            raise MissingNotebooksException
    except MissingNotebooksException:
        print('Missing notebooks for extraction')
        print('Try running: $ python3 converter.py notebook_number_one.ipynb notebook_number_two.ipynb notebook_number_etc.ipynb')


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    for notebook in notebooks:
        try:
            notebook_dict = json.load(open(notebook))
            new_python_file = f'./output/{notebook.split("/")[-1].replace(".ipynb",".py").lower()}'
            python_file = open(new_python_file, 'w')

            for cell in notebook_dict['cells']:
                if 'source' in cell.keys() and cell['cell_type'] == 'code':
                    if export_line in cell['source']:
                        for block in cell['source']:
                            if block != export_line:
                                python_file.writelines(block)
                    python_file.writelines('\n')

            python_file.close()
        except Exception as e:
            print(f'An error happened: {e}')
        else:
            print(f'{notebook} was converted successfully. Python file created at {new_python_file}')
        

if __name__ == '__main__':
    main(sys.argv[1:])