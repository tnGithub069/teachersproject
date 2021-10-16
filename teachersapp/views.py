from django.shortcuts import render,redirect

# Create your views here.

from .process import (
    V999_SampleProcess
)
from .process import C010_Const,C030_MessageUtil

#記載例
def v999_sampleMethod(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V999_SampleProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        path_name = "systemError"
        return redirect(path_name)
        

def v999_sampleMethod2(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V999_SampleProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #エラーフラグを「2：システムエラー」にする
        errflg = "2"
        #コンソールにエラーを出力
        C030_MessageUtil.systemErrorCommonMethod()
        raise(e)


def v999_systemError(request):
    template = 'teachersapp/D999_ERR500.html'
    context = {}
    try:
        return render(request, template, context)
    except Exception as e :
        #コンソールにエラーを出力
        C030_MessageUtil.systemErrorCommonMethod()
        return render(request, template, context)
