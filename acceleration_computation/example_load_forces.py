from get_force import read_position_and_force

if __name__=="__main__":
    file_path = '../data/reactionforce.forces'
    dicts = read_position_and_force(file_path,min_time=1.16,max_time=1.496)

    force = dicts["Force"]  # [nums,3]
    print(force.shape)
    position = dicts["Position"] #[nums,3]
    print(position.shape)
    MZ7 = dicts["MZ7"] #