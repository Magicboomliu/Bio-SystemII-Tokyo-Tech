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
### using `read_excel` in `acceleration_compuation\excel_io.py`   
```
def read_execl(file_path,sheet_id,min_time,max_time):  
    
    file_path: the xlsx file path
    sheet id : 0 for angle computation, 1 for marker and CG poistion  
    min_time: beigin time 
    max_time: end time

```
for exmaple 
```
from excel_io import read_execl 

file_path = "../data/captureddatareduced.xlsx"
max_time = 1.496
min_time = 1.16
position_marker_dict=read_execl(file_path,1,min_time=min_time,max_time=max_time)
angle_marker_dict=read_execl(file_path,0,min_time=min_time,max_time=max_time)
print(angle_marker_dict.keys())
print(position_marker_dict.keys())

```
the output will be: 
```
dict_keys(['heel', 'thenar', 'foot_length','foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG'])  
dict_keys(['Angle1', 'Angle2'])
``` 
each item is a 3-dim shape numpy array: [nums,3] , 3 for `X`,`Y`,`Z`, for example
```
position_marker_dict = read_execl(file_path,1,min_time=min_time,max_time=max_time)
print(position_marker_dict.keys())
angle_marker_dict= read_execl(file_path,0,min_time=min_time,max_time=max_time)
print(angle_marker_dict.keys())
    
heels_data = position_marker_dict['heel']
print(heels_data.shape)
# Get the heal data at X axis
heels_data_X = heels_data[:,1]
print("heel X data from {}s to {}s: \n".format(min_time,max_time),heels_data_X)

```
the output will be: 
```
dict_keys(['heel', 'thenar', 'foot_length', 'foot_CG', 'L_ankle', 'L_knee', 'calf_length', 'calf_CG'])
dict_keys(['Angle1', 'Angle2'])
(43, 3)
heel X data from 1.16s to 1.496s:
 [392.34521 394.26282 396.43082 396.50372 396.5 397.10303 396.87396
 397.84613 398.11047 398.11322 398.40311 398.81226 398.40411 398.77634
 398.98218 398.68817 398.33551 398.52612 398.17261 398.38739 398.2738
 397.27057 395.79999 394.7121 393.37231 391.12659 389.51682 387.47107
 386.3479 384.46823 382.53531 381.84268 379.83423 377.91901 375.77573
 373.34027 369.88196 368.14035 364.76047 361.69989 358.96875 355.98157
 354.46838]
```
YOU can try see the *simple code* of how to obtain origianl data in a numpy form at `acceleration_computation\simple_code_original_data.py`