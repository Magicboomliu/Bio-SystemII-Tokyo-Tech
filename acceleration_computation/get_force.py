import numpy as np

def read_position_and_force(file_path,min_time,max_time):
    min_time_stamp = min_time
    max_time_stamp = max_time
    FX7_list=[]
    FY7_list=[]
    FZ7_list=[]
    X7_list=[]
    Y7_list=[]
    Z7_list=[]
    MZ7_list=[]

    with open(file_path,'r') as f:
        line_idx = 0 
        for line in f.readlines():
            
            if line_idx==0:
                line_idx = line_idx+1
                continue
            line_idx = line_idx+1
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            contents = line.split()


        # judge the time
            time_stamp = float(contents[2])

            if (time_stamp >=min_time_stamp) and (time_stamp<=max_time_stamp):
                
                MZ7_list.append(float(contents[-1]))
                
                Z7_list.append(float(contents[-2]))
                Y7_list.append(float(contents[-3]))
                X7_list.append(float(contents[-4]))

                FZ7_list.append(float(contents[-5]))
                FY7_list.append(float(contents[-6]))
                FX7_list.append(float(contents[-7]))
        
        FX7_list= np.array(FX7_list)
        FY7_list= np.array(FY7_list)
        FZ7_list= np.array(FZ7_list)
        Force = np.concatenate((FX7_list[:,np.newaxis],FY7_list[:,np.newaxis],FZ7_list[:,np.newaxis]),axis=1)
        #print(Force.shape)
        #[43,3]

        X7_list= np.array(X7_list)
        Y7_list= np.array(Y7_list)
        Z7_list= np.array(Z7_list)
        Position = np.concatenate((X7_list[:,np.newaxis],Y7_list[:,np.newaxis],Z7_list[:,np.newaxis]),axis=1)
        #print(Position.shape)
        #[43,3]

        MZ7_list = np.array(MZ7_list)

        return {"Force": Force,"Position":Position,"MZ7":MZ7_list}



    

    
    

    

            

        