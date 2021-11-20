# Bio-SystemII-Tokyo-Tech
This is the bio-system II lecture provided by Tokyo Tech 2021. This repo is using feet data for muscle analysis.  

A work of L.Zihua, L.yanshuo, W.Zuofeng,Y.yucheng,L.keye

## Model Discriptions:

we only consider the left leg model for analysis.
Joint structure model is considerd,
If there are multiple markers for the same joint, choose one for simpification.
#### Use L.ankle and L.knee

#### Center of Gravity:
Because there is no toe data, usetreat thenar as toe

* Thenar-heel=foot CG

* L.ankle-L.knee=leg CG

* L.ankle=joint ankle

* L.knee=joint knee

Ignore the angle between the moving path and x axis, so we can delete the y axis to make the model to 2D
#### Only consider time 1.16-1.496s
The coordinate system of the marker and the force file is the same
## How to get the original data(marker and CG position)? 
YOU can try see the *simple code* of how to obtain origianl data in a numpy form at `acceleration_computation\simple_code_original_data.py`

Just invoke the `get_original_data` in `excel_io.py` by given the *min_time(etc.1.16)* and *max_time(etc.1.496)* and *excel file_path*
```
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
    
```
You can also direct use *pickle* to load the **original data file** which I saved in `data/original_data_dict` by using the *example* above to get the numpy-like data dict in your selected time stamp.
## How to get the acceleration data?  
the details are in `acceleration_compuation\compute_the_acce.py`   
the API is :
```
def cal_the_acceleration(file_path,type,min_time,max_time):
    '''
    file_path: the orginal excel path
    type: what kind of marker of CG you want to calculate from
    {'heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG', 'Angle1', 'Angle2'}
    
    min_time: beigin time stamp
    max_time: ending time stamp
    '''
```

exmaple of how to use this in `acceleration_compuation\simple_load_acc_data.py`