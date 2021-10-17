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
from . import (C010_Const,C030_MessageUtil,
                S020_ShitsmnInfoTork,
                S030_ShitsmnInfoKoshin,
                S040_ShitsmnInfoSakj,
                S050_ShitsmnInfoShutk,
                S060_ShitsmnListShutk_Shinchk,
                S070_ShitsmnListShutk_Jokn,
                S090_KaigiJiknListShutk,
                S900_HanyoMstShutk,
                S905_SaibnMstShtk
)

def main(request):
    #--View共通----------------------------------------------
    #戻り値用の変数宣言
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    #-------------------------------------------------------
    try:
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
            flg_S999 = json_S999["json_CommonInfo"]["errflg"]
            list_msgInfo_S999 = json_S999["json_CommonInfo"]["list_msgInfo"]
            tuple_shitsmnIchirn_S999 = json_S999["tuple_shitsmnIchirn"]
            #メッセージがある場合はセットする
            C030_MessageUtil.setMessageList(request,list_msgInfo_S999)
            #--S020-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnTitle = "菊花賞の勝ち馬を教えてください"
            shitsmnNaiyo = "3000mの3歳馬なので分かりません。"
            shitsmnUserID = "tsunesanbk"
            list_hashTag = ["菊花賞","福永祐一"]
            list_kaigikibujikn = [{"KAISHNCHJ":"2021-10-23 13:00:00","SHURYNCHJ":"2021-10-23 13:30:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-23 18:00:00","SHURYNCHJ":"2021-10-23 18:00:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-24 13:00:00","SHURYNCHJ":"2021-10-24 13:30:00","KAIGIJIKN":30}
                                ]
            json_S020 = S020_ShitsmnInfoTork.main(shitsmnTitle,shitsmnNaiyo,shitsmnUserID,list_hashTag,list_kaigikibujikn)
            #個々の値を取得
            flg_S020 = json_S020["json_CommonInfo"]["errflg"]
            list_msgInfo_S020 = json_S020["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S020 = json_S020["str_shitsmnID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S020)
            #検証用
            json_shitsmnInfo_S050_S020Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S020)["json_shitsmnInfo"]
            #-------------------------------------------------------------------------------
            #--S030-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnID = "Q20211017000000036"
            shitsmnTitle = "マカヒキは強いですか？"
            shitsmnNaiyo = "ニエル賞の勝ち馬が弱いわけありません。"
            shitsmnUserID = ""
            kaigiID = ""
            updUserID = "tsunesanbk"
            list_hashTag = ["凱旋門賞","ニエル賞","クリストフ"]
            list_kaigikibujikn = [{"KAISHNCHJ":"2021-10-23 13:00:00","SHURYNCHJ":"2021-10-23 13:30:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-23 18:00:00","SHURYNCHJ":"2021-10-23 18:00:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-24 13:00:00","SHURYNCHJ":"2021-10-24 13:30:00","KAIGIJIKN":30}
                                ]
            json_S030 = S030_ShitsmnInfoKoshin.main(shitsmnID,shitsmnTitle,shitsmnNaiyo,shitsmnUserID,kaigiID,list_hashTag,list_kaigikibujikn,updUserID,"0")
            #個々の値を取得
            flg_S030 = json_S030["json_CommonInfo"]["errflg"]
            list_msgInfo_S030 = json_S030["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S030 = json_S030["str_shitsmnID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S030)
            #検証用
            json_shitsmnInfo_S050_S030Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S030)["json_shitsmnInfo"]
            #-------------------------------------------------------------------------------
            #--S040-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnID = "Q20211017000000034"
            updUserID = "tsunesanbk"
            json_S040 = S040_ShitsmnInfoSakj.main(shitsmnID,updUserID)
            #個々の値を取得
            flg_S040 = json_S040["json_CommonInfo"]["errflg"]
            list_msgInfo_S040 = json_S040["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S040 = json_S040["str_shitsmnID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S040)
            #検証用
            json_shitsmnInfo_S050_S040Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S040)["json_shitsmnInfo"]
            #-------------------------------------------------------------------------------
            #--S050-------------------------------------------------------------------------
            #サービス呼び出し
            json_S050 = S050_ShitsmnInfoShutk.main("Q20210920000000001")
            #個々の値を取得
            flg_S050 = json_S050["json_CommonInfo"]["errflg"]
            list_msgInfo_S050 = json_S050["json_CommonInfo"]["list_msgInfo"]
            json_shitsmnInfo_S050 = json_S050["json_shitsmnInfo"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S050)
            #-------------------------------------------------------------------------------
            #--S060-------------------------------------------------------------------------
            #サービス呼び出し
            json_S060 = S060_ShitsmnListShutk_Shinchk.main()
            #個々の値を取得
            flg_S060 = json_S060["json_CommonInfo"]["errflg"]
            list_msgInfo_S060 = json_S060["json_CommonInfo"]["list_msgInfo"]
            tuple_T100_shitsmnList_shinchk_S060 = json_S060["tuple_T100_shitsmnList_shinchk"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S060)
            #-------------------------------------------------------------------------------
            #--S070-------------------------------------------------------------------------
            #サービス呼び出し
            keyWord = "マカヒキ"
            list_hashTag = ["競馬","マカヒキ"]
            date_From = "2021-10-15 21:00:00"
            date_To = "2021-10-17 21:00:00"
            selfQ_userID = ""
            selfRQ_userID = "tsunesanBK"
            json_S070 = S070_ShitsmnListShutk_Jokn.main(keyWord,list_hashTag,date_From,date_To,selfQ_userID, selfRQ_userID)
            #個々の値を取得
            flg_S070 = json_S070["json_CommonInfo"]["errflg"]
            list_msgInfo_S070 = json_S070["json_CommonInfo"]["list_msgInfo"]
            tuple_T100_shitsmnList_jokn_S070 = json_S070["tuple_T100_shitsmnList_jokn"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S070)
            #-------------------------------------------------------------------------------
            #--S090-------------------------------------------------------------------------
            #サービス呼び出し
            json_S090 = S090_KaigiJiknListShutk.main()
            #個々の値を取得
            flg_S090 = json_S090["json_CommonInfo"]["errflg"]
            list_msgInfo_S090 = json_S090["json_CommonInfo"]["list_msgInfo"]
            tuple_M110_kaigiJiknList_S090 = json_S090["tuple_M110_kaigiJiknList"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S090)
            #-------------------------------------------------------------------------------
            #--S900-------------------------------------------------------------------------
            json_S900 = S900_HanyoMstShutk.main("SEC0001","01")
            flg_S900 = json_S900["json_CommonInfo"]["errflg"]
            list_msgInfo_S900 = json_S900["json_CommonInfo"]["list_msgInfo"]
            tuple_M101_hanyoMst_S900 = json_S900["tuple_M101_hanyoMst"]
            C030_MessageUtil.setMessageList(request,list_msgInfo_S900)
            #-------------------------------------------------------------------------------
            #--S905-------------------------------------------------------------------------
            tableID = C010_Const.S100["tableID"]
            header = C010_Const.S100["header"]
            json_S905 = S905_SaibnMstShtk.main(tableID,header)
            flg_S905 = json_S905["json_CommonInfo"]["errflg"]
            list_msgInfo_S905 = json_S905["json_CommonInfo"]["list_msgInfo"]
            str_newID_S905 = json_S905["newID"]
            C030_MessageUtil.setMessageList(request,list_msgInfo_S905)
            #-------------------------------------------------------------------------------

            #戻り値にセット
            flg_return = str(int(flg_S999) \
                            + int(flg_S900) \
                            + int(flg_S060) \
                            )
            template = 'teachersapp/T999_Sample.html'
            context = {**context,**{"list_shitsmnIchirn":tuple_shitsmnIchirn_S999,
                                    "json_shitsmnInfo_S050_S020Kensho": json_shitsmnInfo_S050_S020Kensho,
                                    "json_shitsmnInfo_S050_S030Kensho": json_shitsmnInfo_S050_S030Kensho,
                                    "json_shitsmnInfo_S050_S040Kensho": json_shitsmnInfo_S050_S040Kensho,
                                    "json_shitsmnInfo":json_shitsmnInfo_S050,
                                    "tuple_shitsmnList_shinchk":tuple_T100_shitsmnList_shinchk_S060,
                                    "tuple_T100_shitsmnList_jokn":tuple_T100_shitsmnList_jokn_S070,
                                    "tuple_M110_kaigiJiknList_S090":tuple_M110_kaigiJiknList_S090,
                                    "tuple_hanyoMst":tuple_M101_hanyoMst_S900,
                                    "str_newID":str_newID_S905,
                                    }
                    }
        
        #戻り値用のjsonを作成
        json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
        print("===デバッグ用=============================================================================")
        print("■json_view(V999)")
        print(" flg_return:",json_view['flg_return'])
        print(" template:",json_view['template'])
        print(" path_name:",json_view['path_name'])
        print("=========================================================================================")
        return json_view
    #==例外処理==========================================================================================
    except Exception as e :
        raise
    #====================================================================================================

