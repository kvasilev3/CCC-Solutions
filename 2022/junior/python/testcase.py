import os
import subprocess
import time

def test(problem):
    tests_folder = './junior_data'
    tests_subfolders = {'j1':'j1', 'j2':'j2', 'j3':'j3', 'j4':'s2j4', 'j5':'j5', }
    tests_prefixes = {'j1':'j1', 'j2':'j2', 'j3':'j3', 'j4':'s2', 'j5':'j5', }

    start_time = time.time()
    files_list = os.listdir("{0}/{1}".format(tests_folder, tests_subfolders[problem]))
    files_list = sorted(files_list, key=lambda a: a if "sample" in a else "~"+a)    
    for input_filename in files_list:
        if input_filename.startswith("{0}.".format(tests_prefixes[problem])) and input_filename.endswith(".in"):
            inputFile = open("{0}/{1}/{2}".format(tests_folder, tests_subfolders[problem], input_filename), 'r')
            stdout_lines = subprocess.run(['python3', '{0}.py'.format(problem)], stdin=inputFile, capture_output=True).stdout.splitlines()
            stdout_lines = [l.decode('utf-8') for l in stdout_lines]

            output_filename = input_filename.replace('.in', '.out')
            expected_result = open("{0}/{1}/{2}".format(tests_folder, tests_subfolders[problem], output_filename), 'r').readlines()
            expected_result = [l.strip() for l in expected_result]
            if len(stdout_lines) != len(expected_result):
                print('Test {0} failed: Expected {1} lines, but got {2}.'.format(input_filename, len(expected_result), len(stdout_lines)))
                return
            for i in range(len(expected_result)):
                if stdout_lines[i] != expected_result[i]:
                    print('Test {0} failed: At line {1} expected {2}, but got {3}.'.format(input_filename, i+1, expected_result[i], stdout_lines[i]))
                    return
            print('Test {0} passed'.format(input_filename))

    end_time = time.time()
    print("Elapsed time: {0} seconds".format(end_time - start_time))
    print()


if __name__ == '__main__':
    test('j1')
    test('j2')
    test('j3')
    test('j4')
    test('j5')
