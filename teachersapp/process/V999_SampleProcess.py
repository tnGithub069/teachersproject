"""
ビュークラス
A999_SampleAction
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)

flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

from django.urls import reverse
from . import S999_SampleService
from . import C010_Const,C030_MessageUtil

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
        POST以外時の処理を書く。
        パターンに応じてflg_returnの値を設定する。
        bottunパターンによって処理を分けたりもするかも。
        例は、render
        """
        #サービスを利用する場合は呼び出す
        json_S999 = S999_SampleService.main()
        #json型から各値を取得する
        json_shitsmnIchirn = json_S999["json_shitsmnIchirn"]
        list_msgInfo = json_S999["json_CommonInfo"]["list_msgInfo"]
        flg_S999 = json_S999["json_CommonInfo"]["errflg"]
        #メッセージがある場合はセットする
        C030_MessageUtil.setMessageList(request,list_msgInfo)
        #戻り値にセット
        flg_return = "0"
        template = 'teachersapp/D999_Sample.html'
        context = {**context,**json_shitsmnIchirn}
    #戻り値用のjsonを作成
    json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
    #--検証用----------------------------------------------------------------------------
    msgID = "I0001"
    tuple_msgPalams = ("アーモンドアイ","オルフェーブル")
    getMessageInfo_DB = C030_MessageUtil.getMessageInfo_DB(msgID)
    getMessageInfo = C030_MessageUtil.getMessageInfo(msgID,tuple_msgPalams)
    C030_MessageUtil.setMessage(request,msgID,tuple_msgPalams)
    print("getMessageInfo_DB：",getMessageInfo_DB)
    print("getMessageInfo_DB：",getMessageInfo)
    #------------------------------------------------------------------------------------
    return json_view
