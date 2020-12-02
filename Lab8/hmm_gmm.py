from hmmlearn import hmm
from python_speech_features import mfcc
from scipy.io import wavfile
import numpy as np
import joblib
import RPi.GPIO as GPIO
import time

# 特征提取，feat = compute_mfcc(wadict[wavid])
wavdict={'1_1': '1_1.wav', '1_2': '1_2.wav','1_3': '1_3.wav', '1_4': '1_4.wav','1_5':'1_5.wav',
         '2_1': '2_1.wav', '2_2': '2_2.wav','2_3': '2_3.wav', '2_4': '1_4.wav','2_5':'2_5.wav',
         '3_1': '3_1.wav', '3_2': '3_2.wav','3_3': '3_3.wav', '3_4': '3_4.wav','3_5':'3_5.wav',
         '4_1': '4_1.wav', '4_2': '4_2.wav','4_3': '4_3.wav', '4_4': '4_4.wav','4_5':'4_5.wav'
         }
labeldict={'1_1': '1', '1_2': '1', '1_3': '1', '1_4': '1','1_5':'1',
           '2_1': '2', '2_2': '2', '2_3': '2', '2_4': '2','2_5':'2',
           '3_1': '3', '3_2': '3', '3_3': '3', '3_4': '3','3_5':'3',
           '4_1': '4', '4_2': '4', '4_3': '4', '4_4': '4','4_5':'4'}

LED=26
GPIO.setmode(GPIO.BCM)

def compute_mfcc(file):
    fs, audio = wavfile.read(file)
    mfcc_feat = mfcc(audio)
    return mfcc_feat



class Model():
    def __init__(self, CATEGORY=None, n_comp=3, n_mix = 3, cov_type='diag', n_iter=1000):
        super(Model, self).__init__()
        self.CATEGORY = CATEGORY
        self.category = len(CATEGORY)
        self.n_comp = n_comp
        self.n_mix = n_mix
        self.cov_type = cov_type
        self.n_iter = n_iter
        # 关键步骤，初始化models，返回特定参数的模型的列表
        self.models = []
        for k in range(self.category):
            model = hmm.GMMHMM(n_components=self.n_comp, n_mix = self.n_mix, covariance_type=self.cov_type, n_iter=self.n_iter)
            self.models.append(model)
            
    def train(self,wavdict=None,labeldict=None):
            print("start training")
            for k in range(len(self.CATEGORY)):
                model=self.models[k]
                for x in wavdict:
                    if labeldict[x]==self.CATEGORY[k]:
                        # 提取声学特征
                        mfcc_feat = compute_mfcc(wavdict[x])
                        # hmm-gmm 模型训练
                        model.fit(mfcc_feat)
        
    def test(self,filepath):
            result=[]
            for k in range(self.category):
                model=self.models[k]
                mfcc_feat=compute_mfcc(filepath)
                # 生成每个数据在当前模型下的得分情况
                re = model.score(mfcc_feat)
                result.append(re)
            #选取得分最高的种类
            result=np.array(result).argmax()
            print("result:",self.CATEGORY[result])
            return self.CATEGORY[result]
            
    def save(self,path="model.pkl"):
            joblib.dump(self.models,path)
    
    def load(self,path="model.pkl"):
            self.models=joblib.load(path)
            

x=Model(['1','2','3','4'])
#x.train(wavdict,labeldict)
#x.save()
x.load()
x.test("test2.wav")




    
