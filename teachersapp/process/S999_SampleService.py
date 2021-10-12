
def main():
    errflg = "0"
    #タスク一覧取得
    all_task_list = []
    #json形式に変換
    json_TaskList = {'all_task_list': all_task_list}
    json_service = {"errflg":errflg,"json_TaskList":json_TaskList}
    return json_service