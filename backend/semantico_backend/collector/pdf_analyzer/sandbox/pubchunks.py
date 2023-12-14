import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr, data

utils = importr('utils')
base = importr('base')
pubchunks = importr('pubchunks')

utils.chooseCRANmirror(ind=39)

utils.install_packages('stats')
utils.install_packages('lme4')
pubchunks.install_packages('pubchunks')

stats = importr('stats')
lme4 = importr('lme4')
