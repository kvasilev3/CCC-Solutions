import subprocess
import os

def test(problem):
    testsFolder = './junior_data'
    for inputFilename in sorted(os.listdir("{0}/{1}".format(testsFolder, problem))):
        if inputFilename.startswith("{0}.".format(problem)) and inputFilename.endswith(".in"):
            inputFile = open("{0}/{1}/{2}".format(testsFolder, problem, inputFilename), 'r')
            stdoutLines = subprocess.run(['python3', '{0}.py'.format(problem)], stdin=inputFile, capture_output=True).stdout.splitlines()
            stdoutLines = [l.decode('utf-8') for l in stdoutLines]

            outputFilename = inputFilename.replace('.in', '.out')
            expectedResult = open("{0}/{1}/{2}".format(testsFolder, problem, outputFilename), 'r').readlines()
            expectedResult = [l.strip() for l in expectedResult]
            if len(stdoutLines) != len(expectedResult):
                print('Test {0} failed: Expected {1} lines, but got {2}.'.format(inputFilename, len(expectedResult), len(stdoutLines)))
                return
            for i in range(len(expectedResult)):
                if stdoutLines[i] != expectedResult[i]:
                    print('Test {0} failed: At line {1} expected {2}, but got {3}.'.format(inputFilename, i+1, expectedResult[i], stdoutLines[i]))
                    return
            print('Test {0} passed'.format(inputFilename))

if __name__ == '__main__':
    test('j1')
    test('j2')
    test('j3')
    test('j4')
    test('j5')
