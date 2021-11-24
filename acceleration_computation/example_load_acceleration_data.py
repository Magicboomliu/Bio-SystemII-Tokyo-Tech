import pickle
from compute_the_acce import cal_the_acceleration
import matplotlib.pyplot as plt

def visualization(data_dict,name):
    
    plt.title("{} data".format(name))
    plt.plot(data_dict[:,0],label="X")
    plt.plot(data_dict[:,1],label="Y")
    plt.plot(data_dict[:,2],label="Y")
    plt.legend()
    plt.show()

def unpickle(file):
    with open(file, 'rb') as fo:
        dct = pickle.load(fo, encoding='bytes')
    return dct


'''
{'heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 
'calf_length', 'calf_CG', 'Angle1', 'Angle2'}
'''


def example_load_acc_data():
    file_path = "../data/captureddatareduced.xlsx"
    # cal the accelearation
    # shape:[nums,3]
    acc_heal = cal_the_acceleration(file_path, type='heel', min_time=1.16, max_time=1.496)
    acc_thenar = cal_the_acceleration(file_path, type='thenar', min_time=1.16, max_time=1.496)
    acc_foot_cg = cal_the_acceleration(file_path, type='foot_CG', min_time=1.16, max_time=1.496)
    acc_L_ankle = cal_the_acceleration(file_path, type='L_ankle', min_time=1.16, max_time=1.496)
    acc_L_knee = cal_the_acceleration(file_path, type='L_knee', min_time=1.16, max_time=1.496)
    acc_calf_CG = cal_the_acceleration(file_path, type='calf_CG', min_time=1.16, max_time=1.496)

    # shapes[nums,1]
    acc_angle1 = cal_the_acceleration(file_path, type='Angle1', min_time=1.16, max_time=1.496)
    acc_angle2 = cal_the_acceleration(file_path, type='Angle2', min_time=1.16, max_time=1.496)

    visualization(acc_heal,"acc_heel")
    visualization(acc_thenar,"acc_thenar")
    visualization(acc_foot_cg,"acc_foot_cg")
    visualization(acc_L_ankle,"acc_L_ankle")
    visualization(acc_L_knee,"acc_L_knee")
    visualization(acc_calf_CG,"acc_calf_CG")
    plt.title("angle-acceleration speed")
    plt.plot(acc_angle1,label='angle1')
    plt.plot(acc_angle2,label='angle2')
    plt.legend()
    plt.show()

def example_load_pickle_acc():
    acc_data_dict = unpickle("../data/acc_data_dict")

    return acc_data_dict


if __name__ == "__main__":

    example_load_acc_data()
