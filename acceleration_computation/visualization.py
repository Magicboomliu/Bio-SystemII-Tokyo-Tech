import matplotlib.pyplot as plt
from excel_io import read_execl



def visual_the_original_data(file_path,min_time,max_time):
    position_marker_dict = read_execl(file_path,1,min_time=min_time,max_time=max_time)
    print(position_marker_dict.keys())
    angle_marker_dict= read_execl(file_path,0,min_time=min_time,max_time=max_time)
    print(angle_marker_dict.keys())

    heels_data = position_marker_dict['heel']
    print(heels_data.shape)
    # Get the heal data at X axis
    heels_data_X = heels_data[:,1]
    print("heel X data from {}s to {}s: \n".format(min_time,max_time),heels_data_X)
    
    
    






if __name__=="__main__":
    file_path = "../data/captureddatareduced.xlsx"
    visual_the_original_data(file_path,min_time=1.16,max_time=1.496)