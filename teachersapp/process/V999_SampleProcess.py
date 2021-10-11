"""
A999_SampleActionクラス
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)

"""

from django.urls import reverse
from . import D000_Sample_SetDisp
from . import S999_SampleService
from . import C010_Const

def main(request):
    #--戻り値用の変数を宣言-----
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    if request.method == 'POST':
        #POSTの場合
        flg_return = "0"
        path_name = ''
    else:
        #POST以外の場合
        flg_return = "1"
        template = 'teachersapp/D000_Sample.html'
        context = {}
    #戻り値用のjsonを作成
    json_view = {'flg_return':flg_return, template':template, 'context':context, 'path_name':path_name}
    return json_view


#以下無視でOK
"""
#main()メソッドは定型文。正常時、異常時のtemplateをそれぞれ指定する。
def main(request):
    #--初期値宣言----------------------------------------------
    errflg_main = "0"
    template = ""
    context = {}
    #--メソッド実行----------------------------------------------
    errflg_pre = pre(request)
    errflg_chk = check(request)
    if errflg_chk == "0":
        #チェックメソッドクリアの場合のみ、flowクラスを実行する
        errflg_flw = flow(request)
        #正常終了した場合のテンプレートを指定し、コンテキストを取得する
        template = "teachersapp/D000_Sample.html"
        context = D000_Sample_SetDisp.main()
    if errflg_chk == "1":
        #業務エラーが発生した場合のテンプレートを指定し、コンテキストを取得する
        template = "teachersapp/D000_Sample.html"
        context = D000_Sample_SetDisp.main()
    errflg_cls = close()
    #--戻り値の設定----------------------------------------------
    json_main = {'context':context, 'template':template}
    return json_main

#pre()は後続処理を行うための準備メソッド。DB接続などを行う。
def pre(request):
    errflg = "0"
    #pre処理（DB接続など）
    return errflg

#check()は入力チェック用メソッド。check結果：NGの場合は業務エラーを返す。
def check(request):
    errflg = "0"
    #check処理（単項目チェック、相関チェック）
    #業務エラーの場合
    errflg = "1"
    return errflg

#flow()は業務処理用メソッド。入力チェックが正常に終了した場合、処理を実施する。サービスを呼び出したりする。
def flow(request):
    errflg = "0"
    #flow処理
    #業務エラーの場合
    errflg = "1"
    return errflg

#close()はアクション終了メソッド。DB接続解除などを行う。
def close():
    errflg = "0"
    #close処理（DB接続解除など）
    return errflg
"""