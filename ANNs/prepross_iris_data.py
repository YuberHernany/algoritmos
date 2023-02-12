import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

def label_binary(y, kind='setosa'):
    """INPUT: kind (str) label for flower
    OUTPUT: y_binary 1d array of 1's (positive class) and 0 (negative)"""
    if kind == 'setosa':    
        y_binary = (y==0).astype(int)
        return y_binary
    elif kind == 'versicolor':
        y_binary = (y==1).astype(int)
        return y_binary
    elif kind == 'virginica':
        y_binary = (y==2).astype(int)
        return y_binary
    else: 
        print('The unique options are setosa, versicolor and virginica')

def only_sepal_or_petal(X, kind='petal'):
    """INPUT: X 2d array that correspond to iris.data, kind (str) 'petal' or 'sepal'
    OUTPUT: 2d array (only two columns)"""
    if kind == 'sepal':
        return X[:, (0,1)]
    elif kind == 'petal':
        return X[:, (2,3)]
    else:
        print('Only "petal" or "sepal" are allowed')

def mins_and_maxs_per_feature(X, kind='petal'):
    """INPUTS: X 2d array (that is iris.data). kind (str) just 'petal' or 'sepal' allowed
    OUTPUTS: length_min, width_min, length_max, width_max for petal or sepal"""
    X2cols = only_sepal_or_petal(X, kind=kind)
    length_min, width_min = X2cols.min(axis=0)
    length_max, width_max = X2cols.max(axis=0)
    return length_min, width_min, length_max, width_max

def meshgrid_petal_or_sepal(X, kind='petal'):
    """INPUTS: X 2d array (that is iris.data). kind (str) just 'petal' or 'sepal' allowed
    OUTPUTS: Lengths, Widths np.arrays matrices like output of meshgrid"""
    l_min, w_min, l_max, w_max = mins_and_maxs_per_feature(X, kind=kind)
    lengths = np.linspace(l_min, l_max)
    widths = np.linspace(w_min, w_max)
    Lengths, Widths = np.meshgrid(lengths, widths)
    return Lengths, Widths

def full_points_petal_or_sepal(X, kind='petal'):
    """INPUTS: X 2d array (that is iris.data). kind (str) just 'petal' or 'sepal' allowed
    OUTPUTS: points 2d array that represents plane of ficticius flowers"""
    Lengths, Widths = meshgrid_petal_or_sepal(X, kind=kind)
    points = np.hstack([Lengths.ravel().reshape(-1,1), Widths.ravel().reshape(-1,1)])
    return points

def means_sepal_or_petal(X, kind='petal'):
    X2cols = only_sepal_or_petal(X, kind=kind)
    length_mean, width_mean = X2cols.mean(axis=0)
    return length_mean, width_mean

def traslate_data(data, x_value, y_value):
    """INPUTS: data 2darray, x_value, y_value (floats)
    OUTPUTS: new_data resulting after traslate data col1 by x_value and data col2 by y_value"""
    new_col1 = data[:, 0] - x_value
    new_col2 = data[:, 1] - y_value
    new_data = np.hstack([new_col1.reshape(-1,1), new_col2.reshape(-1,1)])
    return new_data
if __name__ == "__main__":
    pass
    
