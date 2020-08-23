import io
import unittest
import unittest.mock

from main import print_results, hash_file, find_dups


class TestDuplicates(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, dups_dict, expected_output, mock_stdout):
        print_results(dups_dict)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_results(self):
        self.assert_stdout({'mnbv123erty': ['file1.txt']}, 'No duplicate files found.\n')
        self.assert_stdout({'wert345dfgp': ['file1.txt', 'file2.txt']},
                           'Duplicate files found in the input directory.\n==================================\nfile1.txt\tfile2.txt\t\n==================================\n')

    def test_hash_file(self):
        self.assertEqual(hash_file('./sample_dir/aqua1.png'), 'de1960c7b3ca3cb9fa7a527f1037683e')

    def test_find_dups(self):
        self.assertEqual(find_dups('sample_dir'), {'5227d84b5860356debe376dc41ad3c68': ['file2.txt', 'file1.txt'], '275b353001beffe4c51158584636f0ab': ['file3.txt'], 'de1960c7b3ca3cb9fa7a527f1037683e': [
                         'aqua1.png', 'aqua2.png'], '7aad2e68646284ff1c4e3308ecdf1756': ['aqua3.png'], '2f9ac2da4e0c11189dd677ca7551ecd3': ['compress2.zip', 'compress1.zip'], 'afe805e5a3c3ec7fa05645a6a2a6e607': ['file4.csv', 'file5.csv']})
