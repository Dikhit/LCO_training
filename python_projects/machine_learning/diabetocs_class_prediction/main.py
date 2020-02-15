from sklearn.model_selection import train_test_split
import math
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Diabetestype.csv')
train_data = df.drop(['Type', 'Class'], axis=1)
output = df.Class
x_train, x_test, y_train, y_test = train_test_split(train_data, output, test_size=0.10, random_state = 42)
l = LinearRegression()
l.fit(x_train, y_train)

print("Accuracy percentage : " + str(l.score(x_test,y_test)*100) + "%")

predict = l.predict([x_test.values[63]])
predict_class = math.floor(predict)
print("class is  " + str(predict_class))