import pandas as pd
import numpy as np
import math as mt
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score

from sklearn.metrics import precision_recall_curve,auc,accuracy_score,roc_auc_score

from sklearn.neighbors import KNeighborsClassifier


def calc_result(tans, answer):
    # precision_score = precision_score(tans,answer,zero_division=1)
    # print("Precision: ",precision_score)
    # recall_score = recall_score(tans,answer)
    # print("Recall:    ",recall_score)
    # f1_score = f1_score(tans,answer)
    # print("f1Score:   ",f1_score)
    Tn = 0
    Fp = 0
    Fn = 0
    Tp = 0
    for i in range(len(answer)):
        if (tans[i] == 0 and answer[i] == 0):
            Tn = Tn + 1  # 2e4
        if (tans[i] == 1 and answer[i] == 0):
            Fp = Fp + 1  # 0
        if (tans[i] == 0 and answer[i] == 1):
            Fn = Fn + 1  # 500
        if (tans[i] == 1 and answer[i] == 1):
            Tp = Tp + 1  # 0
    print(Tp)
    Tn, Tp = Tp, Tn
    Fn, Fp = Fp, Fn
    precision = Tp / (Tp + Fp)
    print("Precision: ", precision)
    recall = Tp / (Tp + Fn)
    print("Recall:    ", recall)
    F1 = 2 * precision * recall / (precision + recall)
    print("F1Score:   ", F1)
    precision, recall, thresholds = precision_recall_curve(tans, answer)
    ###使用AUC函数计算出PR-auc值
    auc_precision_recall = auc(recall, precision)
    print("auc", auc_precision_recall)
    ####'''计算ROC-AUC值'''#####
    roc_auc = roc_auc_score(tans, answer)
    print("roc_auc", roc_auc)

def solve_svc(feature,label,test):
    svm_trainer = SVC(C=1, kernel='rbf', gamma='auto', coef0=0.0, tol=1e-3)
    # sklearn.svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001,
    #                cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None,random_state=None)
    svm_trainer.fit(feature, label)
    return svm_trainer.predict(test)

def solve_knn(feature,label,test):
    kNN_classifier = KNeighborsClassifier(n_neighbors=6)

    # kNN_classifier做一遍fit(拟合)的过程，没有返回值，模型就存储在kNN_classifier实例中
    kNN_classifier.fit(feature, label)

    # kNN进行预测predict，需要传入一个矩阵，而不能是一个数组。reshape()成一个二维数组，第一个参数是1表示只有一个数据，第二个参数-1，numpy自动决定第二维度有多少
    return kNN_classifier.predict(np.array(test).reshape(1, -1))

## main

feature_path = r"data\train\constructed_trainset.csv"
feature = pd.read_csv(feature_path)
label_path = r'data\train\enhanced_feature_label_3_1.csv'
label = pd.read_csv(label_path)
label = label.values
label=label.ravel()
print(label)
label = np.transpose(label)
#label = label.ravel()
#feature = feature.drop(columns=["APPLICATION_ID"])
test_path = r"data\test\constructed_testset.csv"
test = pd.read_csv(test_path)
tans_path = r"data\test\label.csv"
tans = pd.read_csv(tans_path)
tans = tans.drop(columns=["APPLICATION_ID","APPLICATION_DATE"])
tans = tans.values
tans = tans.ravel()
#test = test.drop(columns=["APPLICATION_ID"])
##answer = solve_knn(feature,label,test)
answer = solve_svc(feature,label,test)
calc_result(tans, answer)
print(np.sum(answer==1))

    #np.savetxt(r"predict.txt",answer)