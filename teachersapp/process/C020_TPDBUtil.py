"""
C020_TPDBUtilクラス
DB関連の共通メソッドを格納する

"""
# MySQLdbのインポート
import MySQLdb

def connectDB():
    # データベースへの接続とカーソルの生成
    #settingsから以ってきたい
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='ルートのパスワード',
        db='python_db')
    cursor = connection.cursor()
    return cursor

 
 def closeDB(errflg)
    if errflg == "0":
        # コミット
        connection.commit()
    else:
        # ロールバック
        connection.rollback()
    # 接続を閉じる
    connection.close()
