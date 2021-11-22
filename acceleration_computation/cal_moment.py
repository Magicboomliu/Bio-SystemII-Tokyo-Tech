from excel_io import get_original_data
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.signal import savgol_filter
import pickle
from example_load_original_data import read_data_example
from example_load_forces import read_position_and_force
from example_load_acceleration_data import example_load_pickle_acc
from compute_the_acce import filtering

# counterclockwise is the positive direction

def calForceX(m, GRFx, accx):
    return m*accx - GRFx

def calForceZ(m, GRFz, accz, g):
    return m*accz + m*g - GRFz

def calDistanceXZ(Point1, Point2):
    x = Point1[:-2,0]-Point2[:-2,0]
    z = Point1[:-2,0]-Point2[:-2,0]
    return abs(x/1000), abs(z/1000)

def calMoment(m, g, reactionForce, accdata, origianlData):
    ankle = origianlData["L_ankle"]
    footCG = origianlData["foot_CG"]
    GRF = reactionForce["Position"]
    dis_GRF_ankle_x,  dis_GRF_ankle_z = calDistanceXZ(GRF, ankle)
    dis_footCG_ankle_x, dis_footCG_ankle_z = calDistanceXZ(footCG, ankle)

    acc_foot = accdata["foot_CG"]
    acc_angle = accdata["Angle1"]
    I = 0.0035

    # print(np.shape(GRF[:-2,0]*dis_GRF_ankle_z))
    # print(np.shape(GRF[:-2,0]*dis_GRF_ankle_x))
    # print(np.shape(m*g*dis_footCG_ankle_x))
    # print(np.shape(acc_foot[:,0]/1000*m*dis_footCG_ankle_z))
    # print(np.shape(acc_foot[:,0]/1000*m*dis_footCG_ankle_x))
    # print(np.shape(I*acc_angle/1000))

    return -GRF[:-2,0]*dis_GRF_ankle_z - GRF[:-2,0]*dis_GRF_ankle_x + m*g*dis_footCG_ankle_x - acc_foot[:,0]/1000*m*dis_footCG_ankle_z - acc_foot[:,0]/1000*m*dis_footCG_ankle_x + I*acc_angle/1000


if __name__=="__main__":

    # prepare data
    originalData = read_data_example()

    file_path = '../data/reactionforce.forces'
    forceData = read_position_and_force(file_path,min_time=1.16,max_time=1.496)
    GRFx = forceData["Force"][:-2,0]
    GRFz = forceData["Force"][:-2, 2]

    accData = example_load_pickle_acc()
    accx = accData['foot_CG'][:,0]
    accz = accData['foot_CG'][:, 2]

    # join force
    Fx = calForceX(0.76, GRFx, accx/1000)
    Fz = calForceZ(0.76, GRFz, accz/1000, 9.8)

    # moment
    moment = calMoment(0.76, 9.8, forceData, accData, originalData)

    # filtering for moment
    filtered_moment = filtering(moment)
    print(filtered_moment)

    #graph for moment
    x = [i for i in range(len(filtered_moment))]
    plt.plot(x, -filtered_moment)
    # plt.plot(x, -moment)
    plt.show()


