import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

# Prediction on records
def predict_Adaboost():
    # The features of the train
    df = pd.read_csv('voice.csv')
    # get 0-10 columns
    X = df.iloc[:, 0:11].to_numpy()
    # get 11 column
    y = df.iloc[:, 11].to_numpy()

    # split the data into train and test
    X_train = X
    y_train = y

    # The features of the recording
    df1 = pd.read_csv('voiceTest.csv')
    X_test = df1.iloc[:, 0:11]
    y_test = df1.iloc[:, 11]

    clf = AdaBoostClassifier(n_estimators=100, learning_rate=1)
    model = clf.fit(X_train, y_train)

    predict = model.predict(X_test)

    if len(y_test) == 1:
        gender = y_test[0]
        print("Gender: {} ".format(predict), (predict == gender))
    else:
        print("Score Test: {} ".format(model.score(X_test, y_test)))

    print("Score Train: {} ".format(model.score(X_train, y_train)))


# Prediction on dataset Voice
def adaboost():
    df = pd.read_csv('voice.csv')
    # get 0-10 columns
    X = df.iloc[:, 0:11].to_numpy()
    # get 11 column
    y = df.iloc[:, 11].to_numpy()

    # split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Create adaboost classifier object
    clf = AdaBoostClassifier(n_estimators=100, learning_rate=1)
    # Train adaboost classifier
    model = clf.fit(X_train, y_train)
    # Predict the response for test data
    y_pred = model.predict(X_train)

    print("Score Train: {} ".format(model.score(X_train, y_train)))
    print("Score Test: {} ".format(model.score(X_test, y_test)))
