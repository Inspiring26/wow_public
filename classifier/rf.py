from sklearn.ensemble import RandomForestClassifier
X = [[0, 0, 0], [1, 1, 1]]
Y = [0, 1]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, Y)
print(clf.predict([[0, 1, 0]]))
print(clf.feature_importances_)