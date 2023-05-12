def cal_distance(means_1, means_2, vars_1, vars_2):
    #select the Distance Metric
    pdist = CosineSimilarity()
    # pdist =PairwiseDistance()
    dis = 0
    for (mean_1, mean_2, var_1, var_2) in zip(means_1, means_2, vars_1, vars_2):
        dis += (pdist(mean_1.reshape(1, mean_1.shape[0]), mean_2.reshape(1, mean_2.shape[0])) + pdist(var_1.reshape(1, var_1.shape[0]), var_2.reshape(1, var_2.shape[0])))
    return dis.item()