import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Prediction on records
def predict_KNN():
    df = pd.read_csv('Voice.csv')
    # get 0-3 columns in jumps of 2
    X = df.iloc[:, 0:19].to_numpy()
    y = df.iloc[:, 19].to_numpy()

    # split the data into train and test
    X_train = X
    y_train = y

    df1 = pd.read_csv('voiceTest.csv')
    X_test = df1.iloc[:, 0:19]
    y_test = df1.iloc[:, 19]

    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X_train,y_train)

    y_pred = classifier.predict(X_test)


    for i in range(len(y_pred)):
        if y_pred[i] == "male":
            y_pred[i] = "female"
        else:
            y_pred[i] = "male"

    if len(y_test) == 1:
        gender = y_test[0]
        print("Gender: {} ".format(y_pred), (y_pred == gender))
    else:
        print("Score Test: {} ".format(1 - classifier.score(X_test, y_test)))

    print("Score Train: {} ".format(classifier.score(X_train, y_train)))

# Prediction on dataset Voice
def KNN():
    df = pd.read_csv('Voice.csv')
    # get 0-19
    X = df.iloc[:, 0:19].to_numpy()
    y = df.iloc[:, 19].to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X_train,y_train)

    print("Score Train: {} ".format(classifier.score(X_train, y_train)))
    print("Score Test: {} ".format(classifier.score(X_test, y_test)))


