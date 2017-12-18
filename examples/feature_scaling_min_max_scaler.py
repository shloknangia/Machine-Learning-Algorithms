from sklearn.preprocessing import MinMaxScaler
import numpy

# numpy accepts floating point numbers only
weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()

# does 2 things
# find xmin and xmax
# and apply it to all items
rescaled_weight = scaler.fit_transform(weights)

print rescaled_weight