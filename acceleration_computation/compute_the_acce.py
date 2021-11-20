from excel_io import get_original_data
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.signal import savgol_filter
import pickle
#from sklearn.linear_model import LinearRegression

# Filtering
def move_average_filtering(data,kernel_size=3,stride=1):
    n=np.ones(kernel_size)
    weights=n/kernel_size
    sma=np.convolve(weights, data, mode='valid')
    return sma

def medium_filtering(data,kernel_size=3):
    return signal.medfilt(data,kernel_size=kernel_size)

def savitzky_golay_filtering(data,kernel_size=3):
    y = savgol_filter(data, kernel_size, kernel_size-1, mode= 'nearest')
    return y

# Choose the filtering methods
def filtering(data,kernel_size=3,type=0):
    '''
    type 0 :move_average_filtering
    type 1: medium_filtering
    type 2: savitzky_golay_filtering
    '''
    if type==0:
        filtered_data = move_average_filtering(data,kernel_size=3,stride=1)
    elif type==1:
        filtered_data = medium_filtering(data,kernel_size=3)
    elif type==2:
        filtered_data = savitzky_golay_filtering(data,kernel_size=3)
    else:
        raise NotImplementedError
    return filtered_data


def data_processing(data,mean=None):
    # first-order diff
    reduce_data = np.diff(data,n=1,axis=-1)
    # get the speed
    linear_speed = reduce_data*1.0/0.008
    # filtering: choose a mode and kernel size
    filtered_linear_speed = filtering(linear_speed,kernel_size=3,type=1)

    # Second diff of position, first diff of speed
    reduce_linear_speed = np.diff(filtered_linear_speed,n=1,axis=-1)
    acc = reduce_linear_speed*1.0/0.008
    filtered_acc = filtering(acc,kernel_size=3,type=1)

    # if mean!=None:
    #     if mean=='normal':
    #         acc_mean = np.mean(filtered_acc)
    #         print(acc_mean)
    #     elif mean=='fit':
    #         x_range = list(range(1,len(reduce_linear_speed)+1))
    #         model = LinearRegression()
    #         model = model.fit(np.array(x_range).reshape(-1,1), np.array(reduce_linear_speed).reshape(-1,1))
    #         y_infer = model.predict(np.array(x_range).reshape(-1,1))
    #         plt.plot(x_range,y_infer,'-')
    #         print('slope:', model.coef_/0.008)
    
    return filtered_acc

    



def cal_the_acceleration(file_path,type,min_time,max_time):
    '''
    file_path: the orginal excel path
    type: what kind of marker of CG you want to calculate from
    {'heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG', 'Angle1', 'Angle2'}
    
    min_time: beigin time stamp
    max_time: ending time stamp
    '''
    # get the orginal data dict
    data_dict = get_original_data(file_path,min_time=1.16,max_time=1.496)

    if type=='heel':
        data = data_dict['heel']
        data_X = data[:,0]
        data_Y = data[:,1]
        data_Z = data[:,2]
        
        acc_x = data_processing(data_X,mean=None)
        acc_y = data_processing(data_Y,mean=None)
        acc_z = data_processing(data_Z,mean=None)
        acc = np.concatenate((acc_x[:,np.newaxis],acc_y[:,np.newaxis],acc_z[:,np.newaxis]),axis=1)
    
    elif type=='thenar':
        data = data_dict['thenar']
        data_X = data[:,0]
        data_Y = data[:,1]
        data_Z = data[:,2]
        acc_x = data_processing(data_X,mean=None)
        acc_y = data_processing(data_Y,mean=None)
        acc_z = data_processing(data_Z,mean=None)
        acc = np.concatenate((acc_x[:,np.newaxis],acc_y[:,np.newaxis],acc_z[:,np.newaxis]),axis=1)

    elif type=='foot_CG':
        data = data_dict['foot_CG']
        data_X = data[:,0]
        data_Y = data[:,1]
        data_Z = data[:,2]
        acc_x = data_processing(data_X,mean=None)
        acc_y = data_processing(data_Y,mean=None)
        acc_z = data_processing(data_Z,mean=None)
        acc = np.concatenate((acc_x[:,np.newaxis],acc_y[:,np.newaxis],acc_z[:,np.newaxis]),axis=1)
    
    elif type=='L_ankle':
        data = data_dict['L_ankle']
        data_X = data[:,0]
        data_Y = data[:,1]
        data_Z = data[:,2]
        acc_x = data_processing(data_X,mean=None)
        acc_y = data_processing(data_Y,mean=None)
        acc_z = data_processing(data_Z,mean=None)
        acc = np.concatenate((acc_x[:,np.newaxis],acc_y[:,np.newaxis],acc_z[:,np.newaxis]),axis=1)
    
    elif type=='L_knee':
        data = data_dict['L_knee']
        data_X = data[:,0]
        data_Y = data[:,1]
        data_Z = data[:,2]
        acc_x = data_processing(data_X,mean=None)
        acc_y = data_processing(data_Y,mean=None)
        acc_z = data_processing(data_Z,mean=None)
        acc = np.concatenate((acc_x[:,np.newaxis],acc_y[:,np.newaxis],acc_z[:,np.newaxis]),axis=1)

    elif type=='calf_CG':
        data = data_dict['calf_CG']
        data_X = data[:,0]
        data_Y = data[:,1]
        data_Z = data[:,2]
        acc_x = data_processing(data_X,mean=None)
        acc_y = data_processing(data_Y,mean=None)
        acc_z = data_processing(data_Z,mean=None)
        acc = np.concatenate((acc_x[:,np.newaxis],acc_y[:,np.newaxis],acc_z[:,np.newaxis]),axis=1)
    
    elif type =='Angle1':
        data = data_dict['Angle1']
        acc = data_processing(data)
    
    elif type =='Angle2':
        data = data_dict['Angle2']
        acc = data_processing(data)
    else:
        raise NotImplementedError

    return acc

        


if __name__=="__main__":
    file_path = "../data/captureddatareduced.xlsx"
    
    # cal the accelearation
    # shape:[nums,3]
    acc_heal = cal_the_acceleration(file_path,type='heel',min_time=1.16,max_time=1.496)
    acc_thenar = cal_the_acceleration(file_path,type='thenar',min_time=1.16,max_time=1.496)
    acc_foot_cg = cal_the_acceleration(file_path,type='foot_CG',min_time=1.16,max_time=1.496)
    acc_L_ankle = cal_the_acceleration(file_path,type='L_ankle',min_time=1.16,max_time=1.496)
    acc_L_knee = cal_the_acceleration(file_path,type='L_knee',min_time=1.16,max_time=1.496)
    acc_calf_CG = cal_the_acceleration(file_path,type='calf_CG',min_time=1.16,max_time=1.496)
    
    # shapes[nums,1]
    acc_angle1 = cal_the_acceleration(file_path,type='Angle1',min_time=1.16,max_time=1.496)
    acc_angle2 = cal_the_acceleration(file_path,type='Angle2',min_time=1.16,max_time=1.496)


    # Save It into a pickle file(optional)
    acc_dict ={"heel":acc_heal,"thenar":acc_thenar,"foot_CG":acc_foot_cg,"L_ankle":acc_L_ankle,
                "L_knee": acc_L_knee,"calf_CG":acc_calf_CG,"Angle1":acc_angle1,
                "Angle2":acc_angle2}
    with open('../data/acc_data_dict','wb') as f1:
        pickle.dump(acc_dict,f1)

    
