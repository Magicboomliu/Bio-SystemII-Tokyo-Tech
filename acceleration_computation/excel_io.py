# author ="Liu"
'''
This file is used for reading the excel or .xlsx files
'''
from types import new_class
import numpy as np
import pandas as pd
import io

from pandas.io.pytables import performance_doc

def read_column_data(df,column_name,dicts,min_id=None,max_id=None):
    if min_id==None and max_id==None:
        data = df.iloc[:,dicts[column_name]]
    else:
        max_id = max_id+1
        data= df.iloc[min_id:max_id,dicts[column_name]]
    return data

def find_idx(df,min,max):
    min_idx = 0
    max_idx = len(df)-1
    
    for idx in range(len(df)):
        if isinstance(df[idx],str) or df[idx]==None:
            continue
        elif df[idx]==min or (df[idx]<min and df[idx+1]>min):
            min_idx = idx
        elif df[idx]==max or (df[idx]<max and df[idx+1]>max):
            max_idx = idx

    return min_idx,max_idx

# Read the Excel data
def read_execl(file_path,sheet_id,min_time,max_time):
    data = pd.read_excel(file_path,sheet_name=sheet_id)

    if sheet_id==1:
        num_rows = len(data.index.values)
        num_columns = len(data.columns.values)

        colume_names = data.columns.values
        colume_index = list(range(num_columns))
        # rename_the_columes
        colume_names[2] ='heel_X'
        colume_names[3]='heel_Y'
        colume_names[4]='heel_Z'
        colume_names[5]='thenar_X'
        colume_names[6]='thenar_Y'
        colume_names[7]='thenar_Z'
        colume_names[9]='foot_length'
        colume_names[10]="foot_CG_X"
        colume_names[11]="foot_CG_Y"
        colume_names[12]="foot_CG_Z"
        colume_names[13]="L_ankle_X"
        colume_names[14]="L_ankle_Y"
        colume_names[15]="L_ankle_Z"
        colume_names[16]='L_knee_X'
        colume_names[17]='L_knee_Y'
        colume_names[18]='L_knee_Z'
        colume_names[19]='calf_length'
        colume_names[20]='calf_CG_X'
        colume_names[21]='calf_CG_Y'
        colume_names[22]='calf_CG_Z'
        column_refering_dict = dict(zip(colume_names,colume_index))
        Time = read_column_data(data,"Time",column_refering_dict)
        # Spiltation
        time_min_index,time_max_index = find_idx(Time,min=min_time,max=max_time)

        # Gathering the data here
        heel_X_data = read_column_data(data,"heel_X",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        heel_Y_data = read_column_data(data,"heel_Y",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        heel_Z_data = read_column_data(data,"heel_Z",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values        
        heel_data = np.concatenate((heel_X_data[:,np.newaxis],heel_Y_data[:,np.newaxis],heel_Z_data[:,np.newaxis]),axis=1)


        thenar_X_data = read_column_data(data,"thenar_X",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        thenar_Y_data = read_column_data(data,"thenar_Y",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        thenar_Z_data = read_column_data(data,"thenar_Z",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        thenar_data = np.concatenate((thenar_X_data[:,np.newaxis],thenar_Y_data[:,np.newaxis],thenar_Z_data[:,np.newaxis]),axis=1)
        foot_length_data = read_column_data(data,"foot_length",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        

        foot_CG_X_data = read_column_data(data,"foot_CG_X",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        foot_CG_Y_data = read_column_data(data,"foot_CG_Y",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        foot_CG_Z_data = read_column_data(data,"foot_CG_Z",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        foot_CG_data = np.concatenate((foot_CG_X_data[:,np.newaxis],foot_CG_Y_data[:,np.newaxis],foot_CG_Z_data[:,np.newaxis]),axis=1)

        L_ankle_X_data = read_column_data(data,"L_ankle_X",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        L_ankle_Y_data = read_column_data(data,"L_ankle_Y",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        L_ankle_Z_data = read_column_data(data,"L_ankle_Z",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        L_ankle_data = np.concatenate((L_ankle_X_data[:,np.newaxis],L_ankle_Y_data[:,np.newaxis],L_ankle_Z_data[:,np.newaxis]),axis=1)

        L_knee_X_data = read_column_data(data,"L_knee_X",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        L_knee_Y_data = read_column_data(data,"L_knee_Y",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        L_knee_Z_data = read_column_data(data,"L_knee_Z",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        L_knee_data = np.concatenate((L_knee_X_data[:,np.newaxis],L_knee_Y_data[:,np.newaxis],L_knee_Z_data[:,np.newaxis]),axis=1)

        calf_length_data = read_column_data(data,"calf_length",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        
        calf_CG_X_data = read_column_data(data,"calf_CG_X",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        calf_CG_Y_data = read_column_data(data,"calf_CG_Y",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        calf_CG_Z_data = read_column_data(data,"calf_CG_Z",column_refering_dict,min_id=time_min_index,max_id=time_max_index).values
        calf_CG_data = np.concatenate((calf_CG_X_data[:,np.newaxis],calf_CG_Y_data[:,np.newaxis],calf_CG_Z_data[:,np.newaxis]),axis=1)

        
        return {"heel":heel_data,"thenar":thenar_data,"foot_length":foot_length_data,"foot_CG":foot_CG_data,
                "L_ankle":L_ankle_data,"L_knee":L_knee_data,"calf_length":calf_length_data,
                "calf_CG":calf_CG_data}
    
    if sheet_id==0:
        num_rows = len(data.index.values)
        num_columns = len(data.columns.values)
        column_name_angle1 = data.iloc[1,-1]
        column_name_angle2 = data.iloc[1,-2]
        time = data.iloc[:,1]
        time_min_idx,time_max_idx = find_idx(time,min_time,max_time)
        angle1 = data.iloc[time_min_idx:time_max_idx+1,-2].values
        angle2 = data.iloc[time_min_idx:time_max_idx+1,-1].values
        
        return {"Angle1":angle1,"Angle2":angle2}


if __name__=="__main__":
    file_path = "../data/captureddatareduced.xlsx"
    data_dict = read_execl(file_path=file_path,sheet_id=0,min_time=1.16,max_time=1.496)