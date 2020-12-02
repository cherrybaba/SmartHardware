from python_speech_features import mfcc
from scipy.io import wavfile
# 特征提取，feat = compute_mfcc(wadict[wavid])
def compute_mfcc(file):
    fs, audio = wavfile.read(file)
    mfcc_feat = mfcc(audio)
    return mfcc_feat

def save(self,path="model.pkl"):
    joblib.dump(self.models,path)
    
def load(self,path="model.pkl"):
    self.models=joblib.load(path)

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
            
for x in wavdict:
    # 提取声学特征
    mfcc_feat = compute_mfcc(wavdict[x])
    # hmm-gmm 模型训练
    model.fit(mfcc_feat)
result=[]
for k in range(self.category):
    model=self.models[k]
    mfcc_feat=compute_mfcc(filepath)
    # 生成每个数据在当前模型下的得分情况
    re = model.score(mfcc_feat)
    result.append(re)
#选取得分最高的种类
result=np.array(result).argmax()



    
