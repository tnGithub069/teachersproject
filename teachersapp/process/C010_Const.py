"""
共通クラス
C010_Const
共通的な定数を格納する

"""
from django.contrib.messages import constants


#Djangoメッセージレベル
DEBUG = constants.DEBUG
INFO = constants.INFO
SUCCESS = constants.SUCCESS
WARNING = constants.WARNING
ERROR = constants.ERROR

#シーケンステーブルID
S100 = {"tableID":"S100_SHITSMN_ID","header":"Q"}
S120 = {"tableID":"S130_KAIG_ID","header":"K"}
