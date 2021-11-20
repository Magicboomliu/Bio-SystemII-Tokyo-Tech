import matplotlib.pyplot as plt
from excel_io import get_original_data
import pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        dct = pickle.load(fo, encoding='bytes')
    return dct

def read_data_example():
    file_path = "../data/captureddatareduced.xlsx"
    data_dict = get_original_data(file_path,min_time=1.16,max_time=1.496)
    print(data_dict.keys())
    #dict_keys(['heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG', 'Angle1', 'Angle2'])
    
    # if you want to use one specific data
    print(data_dict['heel'].shape)
    #[43,3] , 0~2 for: X,Y,Z
    heel_X_data = data_dict['heel'][:,0]
    print(heel_X_data)

def save_data_example():
    file_path = "../data/captureddatareduced.xlsx"
    data_dict = get_original_data(file_path,min_time=1.16,max_time=1.496,save='../data/original_data_dict')

def load_data_example():
    data_dict = unpickle('../data/original_data_dict')
    print(data_dict.keys())
    #dict_keys(['heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG', 'Angle1', 'Angle2'])



if __name__=="__main__":

    # example of reading original data from a excel
    read_data_example()

    # exmaple of saving into pickle file 
    #save_data_example()

    # example of loading the pickle file
    #load_data_example()
    






    