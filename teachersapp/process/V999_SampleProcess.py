"""
A999_SampleActionクラス
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)

flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

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
        """
        POST時の処理を書く。
        パターンに応じてflg_returnの値を設定する。
        bottunパターンによって処理を分けたりもするかも。
        例は、redirect
        """
        flg_return = "1"
        path_name = 'sample_url2'
    else:
        #POST以外の場合
        """
        POST時の処理を書く。
        パターンに応じてflg_returnの値を設定する。
        bottunパターンによって処理を分けたりもするかも。
        例は、render
        """
        flg_return = "0"
        template = 'teachersapp/D999_Sample.html'
        context = S999_SampleService.main()["json_TaskList"]
    #戻り値用のjsonを作成
    json_view = {'flg_return':flg_return, template':template, 'context':context, 'path_name':path_name}
    return json_view
