from modules import *


print("please wait ...")
df = pd.read_csv('oyo_data.csv')


lr = LinearRegression()

# data 
output = df['offered price']
training_data = df.drop(['Unnamed: 0','oyo hotel', 'address', 'offered price'], axis=1)


# model
x_train, x_test, y_train, y_test = train_test_split(training_data, output, test_size=0.10, random_state = 42)
lr = LinearRegression()
lr.fit(x_train, y_train)

print("modal ready")
score = lr.score(x_test,y_test)
print("Accuracy is "+str(score) + "%")

ratings = float(input("Enter the ratings of the oyo room : "))
original_price = int(input("Enter the original price : "))

predicted_offered = lr.predict([[ratings,original_price]])
print("May be ", predicted_offered[0])