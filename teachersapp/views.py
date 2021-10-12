from django.shortcuts import render,redirect

# Create your views here.

from .process import (
    V999_SampleProcess
)
from .process import C010_Const

#記載例
def v999_sampleMethod(request):
    #ビュープロセスクラスを呼び出し
    json_view = V999_SampleProcess.main(request)
    #「render」か「redirect」かを判断
    flg_return = json_view["flg_return"]
    if flg_return == "0":
        #「render」の場合
        context = json_view["context"]
        template = json_view["template"]
        return render(request, template, context)
    if flg_return == "1":
        #「redirect」の場合
        path_name = json_view["path_name"]
        return redirect(path_name)

def v999_sampleMethod2(request):
    #ビュープロセスクラスを呼び出し
    json_view = V999_SampleProcess.main(request)
    #「render」か「redirect」かを判断
    flg_return = json_view["flg_return"]
    if flg_return == "0":
        #「render」の場合
        context = json_view["context"]
        template = json_view["template"]
        return render(request, template, context)
    if flg_return == "1":
        #「redirect」の場合
        path_name = json_view["path_name"]
        return redirect(path_name)