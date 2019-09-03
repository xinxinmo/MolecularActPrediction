import os
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import make_scorer

# helper
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

MLMODEL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def randomForrestModel(feature, feature_num):
    pkl_filename = "best_model_corr.pkl"
    file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "merckchallengeapp","materials", pkl_filename)
    f = feature.split(',')
    if len(f) != feature_num: return -1
    X = np.asarray(f)
    X = X.reshape(1, -1)
    with open(file_dir, 'rb') as file:
        pickle_model = pickle.load(file)
    Y = pickle_model.predict(X)
    return Y
