import pandas as pd
from catboost.datasets import titanic


def titanic_create_csv():
    titanic_train, titanic_test = titanic()
    titanic_train = titanic_train[["Pclass", "Sex", "Age"]]
    titanic_train.to_csv('data/titanic_train.csv', index=False)


def titanic_fillna_age():
    titanic_train = pd.read_csv('data/titanic_train.csv')
    titanic_train["Age"] = titanic_train["Age"].fillna(titanic_train["Age"].mean())
    titanic_train.to_csv('data/titanic_train.csv', index=False)


def titanic_ohe_sex():
    titanic_train = pd.read_csv('data/titanic_train.csv')
    titanic_train = pd.get_dummies(titanic_train, columns=["Sex"])
    titanic_train.to_csv('data/titanic_train.csv', index=False)
