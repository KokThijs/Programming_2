'''
main file to read the csv and convert to json
'''
import linecache

from CsvConverter import CsvConverter

FILEPATH = 'dSST.csv'


class Reader(CsvConverter):
    '''
    this class contains methods to read the csv file
    '''
    def __init__(self, file_path):
        self.file_path = file_path
        self.cached_lines = []
        self.current_line = 1
        self.total_lines = 0

    def get_lines(self):
        '''
        open the file and read it
        '''
        # get the header only when the pointer is at 1 (first line)
        if self.current_line == 1:
            header = linecache.getline(self.file_path, self.current_line).strip()
            self.header = header
            self.json_writer = CsvConverter(header)
            self.current_line += 1
            self.total_lines += 1

        # get the 5 following lines
        count = 0

        while count < 5:
            self.cached_lines.append(linecache.getline(self.file_path, self.current_line).strip())
            self.current_line += 1
            self.total_lines += 1
            count += 1
        
        # get next 5 lines and convert them to json as well
        self.csv_to_json(self.cached_lines)

def main():
    file = Reader(FILEPATH)
    file.get_lines() # get line 2 to 7
    file.get_lines() # get line 8 to 13
    file.get_lines() # get line 14 to 19
    file.get_lines() # etc
    file.get_lines() # etc
    file.get_lines() # etc
    print(len(FILEPATH))
    # file.write_to_file() # write all the cached json to an output file

if __name__ == '__main__':
    main()
