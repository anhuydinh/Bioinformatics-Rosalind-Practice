'''
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''

outputFile = [] #store value that we read from a file as a list

with open('/home/haro/Documents/Desktop 2/Workspace/Bioinformatics/Practice/Bioinformatics-Rosalind-Practice/Python Village/sample_input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()
    ) if pos%2 != 0]

with open('/home/haro/Documents/Desktop 2/Workspace/Bioinformatics/Practice/Bioinformatics-Rosalind-Practice/Python Village/sample_output.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))


