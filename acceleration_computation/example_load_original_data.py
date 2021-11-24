from types import LambdaType
import matplotlib.pyplot as plt
from excel_io import get_original_data
import pickle
import matplotlib.pyplot as plt


def unpickle(file):
    with open(file, 'rb') as fo:
        dct = pickle.load(fo, encoding='bytes')
    return dct


def read_data_example():
    file_path = "../data/captureddatareduced.xlsx"
    data_dict = get_original_data(file_path, min_time=1.16, max_time=1.496)
    # print(data_dict.keys())
    # #dict_keys(['heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG', 'Angle1', 'Angle2'])
    #
    # # if you want to use one specific data
    # print(data_dict['heel'].shape)
    # #[43,3] , 0~2 for: X,Y,Z
    # heel_X_data = data_dict['thenar'][:,2]
    # print(heel_X_data)
    return data_dict


def save_data_example():
    file_path = "../data/captureddatareduced.xlsx"
    data_dict = get_original_data(file_path, min_time=1.16, max_time=1.496, save='../data/original_data_dict')


def load_data_example():
    data_dict = unpickle('../data/original_data_dict')
    print(data_dict.keys())
    # dict_keys(['heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG', 'Angle1', 'Angle2'])


def visualization(name,data_dict):
    
    plt.title("{} data".format(name))
    plt.plot(data_dict[name][:,0],label="X")
    plt.plot(data_dict[name][:,1],label="Y")
    plt.plot(data_dict[name][:,2],label="Y")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # example of reading original data from a excel
    data_dict = read_data_example()

    # plt.title("{} data".format('heel'))
    # plt.plot(data_dict['heel'][:,0],label="X")
    # plt.plot(data_dict['heel'][:,1],label="Y")
    # plt.plot(data_dict['heel'][:,2],label="Y")
    # plt.legend()
    # plt.show()
    # #dict_keys(['heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG', 'Angle1', 'Angle2'])

    # visualization('heel',data_dict)
    # visualization('thenar',data_dict)
    # visualization('foot_CG',data_dict)
    # visualization("L_ankle",data_dict)
    # visualization("L_knee",data_dict)
    # visualization('calf_CG',data_dict)
    plt.title("Angle1:thenar-L.ankle-L.ankle-L.knee")
    plt.plot(data_dict["Angle1"])
    plt.show()
    plt.title("Angle2:L.ankle-L.knee-L.knee-trochanter major")
    plt.plot(data_dict["Angle2"])
    plt.show()







