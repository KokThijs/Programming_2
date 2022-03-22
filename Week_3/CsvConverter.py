'''
csv to json class
'''
import json

class CsvConverter():
    '''
    Converts Csv to JSON and write to file
    '''
    def __init__(self, header):
        self.header = header


    def csv_to_json(self, data_lines):
        '''
        this method converts the CSV lines to Json lines by turning the column names into keys
        '''
        # get the first line of the csv file, which contains the headers
        self.data = data_lines
        json_file = []
        for line in self.data:
            if len(self.header.split(',')) != len(line.split(',')):
                raise ValueError('the amount of headers is not equal to the datacolumns')
            else:
                json_file.append(dict(zip(self.header.split(','), [float(x) for x in line.split(',')])))
        self.json_file = json_file


    def write_to_file(self, output_name = 'dSST.json'):
        '''
        Writes the json data to a file
        '''
        with open(file=output_name, mode = 'w') as output_file:
            json.dump(self.json_file, output_file)