from joblib import load
from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
load(reg, 'data/model.joblib')
reg.predict(your_data)
