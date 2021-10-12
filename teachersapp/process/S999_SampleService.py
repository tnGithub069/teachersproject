from . import C020_TPDBUtil
import MySQLdb

def main():
    errflg = "0"
    json_shitsmnIchirn = {}
    #DB接続開始、コネクションとカーソルを取得
    json_DBConnectInfo = C020_TPDBUtil.connectDB()
    con = json_DBConnectInfo['con']
    cur = json_DBConnectInfo['cur']
    #クエリを定義
    sql = "SELECT SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID FROM T100_SHITSMN"
    #クエリを実行
    cur.execute(sql)
    # 実行結果を取得する
    rows = cur.fetchall()
    print('テーブルから取得したオブジェクトの型：',type(rows))
    print('テーブルから取得したオブジェクトの型(1行)：',type(rows[0]))
    print('テーブルから取得したオブジェクトの型(カラム)：',type(rows[0]["SHITSMN_TITLE"]))
    print('テーブルから取得したオブジェクト(カラム)：',rows[0]["SHITSMN_TITLE"])
    #DB接続終了
    C020_TPDBUtil.closeDB(con,errflg)
    #json形式に変換
    json_shitsmnIchirn = {'list_shitsmnIchirn': rows}
    json_service = {"errflg":errflg,"json_shitsmnIchirn":json_shitsmnIchirn}
    return json_service