import os
import sys
import hashlib


def find_dups(input_directory):
    '''
    Takes path to a directory as input.
    Returns a dictionary grouping the files with same content in lists.
    '''
    # dups data structure => {hash:[file_names]}
    dups = {}
    print('Scanning the directory %s :::' % input_directory)
    for item in os.listdir(input_directory):
        item_path = os.path.join(input_directory, item)
        if os.path.isfile(item_path):
            # calculate hash of the file
            file_hash = hash_file(item_path)
            # add or append the file path
            if file_hash in dups:
                dups[file_hash].append(item)
            else:
                dups[file_hash] = [item]
    return dups


def hash_file(file_path, blocksize=65536):
    '''
    Reads content of a file and calculates md5 sum.
    Contents are read in chunks of 64KB at a time.
    A buffer is maintained before the hexdigest is calculated based on total bytes of the file.
    '''
    hasher = hashlib.md5()
    with open(file_path, 'rb') as afile:
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
    return hasher.hexdigest()


def print_results(dups_dict):
    '''
    Takes {hash:[file_names]} dictionary as input.
    It loops through the dictionary and prints the results to the console.
    '''
    results = list(filter(lambda x: len(x) > 1, dups_dict.values()))
    if len(results) > 0:
        print('Duplicate files found in the input directory.')
        print('==================================')
        for result in results:
            for file in result:
                print('%s' % file, end='\t')
            print('\n==================================')
    else:
        print('No duplicate files found.')


# driver code
if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_directory = sys.argv[1]
        if os.path.exists(input_directory):
            dups = find_dups(input_directory)
            print_results(dups)
        else:
            print('%s is not a valid directory path. Please provide a valid path as argument.' % input_directory)
            sys.exit()
    else:
        print('The program expects exactly one directory path as argument.\nUsage: python main.py dir_path')
