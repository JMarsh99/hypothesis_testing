import importlib
import os
import sys

import project.complicated_maths_functions
import hypothesis.extra.ghostwriter


def main(module_path):
    # module_path should be the module name as if imported
    # E.g. 'constantine.scripts.push_statkraft_data'
    try:
        module = importlib.import_module(module_path)
    except Exception:
        print('Module ' + module_path + ' does not exist, exiting...')
        return
    file_string = hypothesis.extra.ghostwriter.fuzz(module)
    hypothesis_folder = os.path.join('hypothesis_tests')
    if not os.path.isdir(hypothesis_folder):
        os.mkdir(hypothesis_folder)

    module_name = '_'.join(module_path.split('.')[1:])
    with open(os.path.join(hypothesis_folder, module_name + '.py'), 'w+') as test_file:
        test_file.write(file_string)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('USAGE: python generate_hypothesis.py constantine.path.to.module')
