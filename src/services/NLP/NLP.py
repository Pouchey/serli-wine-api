

# NLP abstract class
class NLP:
    def __init__(self, model_path = None, data_path = None, verbose = False):
        self.verbose = verbose
        self.data = []
        self.model = None

        if model_path is not None:
            self.model = self.load_model(model_path)

        if data_path is not None:
            self.data = self.load_data(data_path)

    # load a model method
    # param: path
    # return: model
    def load_model(self, path):
        pass 

    # abstract method predict
    # param: text
    # return: string[]
    def predict(self, text):
        pass

    # method to load the data from csv file
    # param: path
    # return: data
    def load_data(self, path):
        self.debug("[INFO] loading data from csv file:", path, "...")
        # load data from csv file to get each line 
        csv_file = open(path, 'r', encoding='utf-8')
        # read the csv file line by line
        data = []
        for line in csv_file:
            # append the line to the data list
            data.append(line)
        # close the file
        csv_file.close()

        return data

    # function to debug if verbose is true
    # param: args
    def debug(self, *args):
        if self.verbose:
            print(*args)