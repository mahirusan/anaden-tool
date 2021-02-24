from .models import MainTask,SubTask
import csv


#######################
# python manage.py shellから実行
#######################

# csvファイルを開きヘッダーを抜いたデータだけのリストを作る
def open_csv_to_list(file_path):
    l = []

    with open(file_path) as f:
        # print(f.read())
        reader = csv.reader(f)
        header_in_list = [row for row in reader]
        l = sorted(header_in_list[1:])

    return l



# 1-26章までが1部、27-45章が1.5部、46-55章が2部前編、56-66章が2部中編、67-74章が2部後編
def addStorys():
    add_datas = [] #作成クエリの配列の配列
    csv_datas = open_csv_to_list("./static/csv/anaden_storys.csv") #csvを二次元リストに変換
    print(csv_datas)

    #全てのSubTaskを削除(今回だけ)
    SubTask.objects.all().delete()

    for csv_data in csv_datas:
        # 第1部の場合
        if int(csv_data[0]) >= 1 and int(csv_data[0]) <= 26:
            main = MainTask.objects.get(types=1,task_seq=1)
            sub = SubTask(main_task=main,title=csv_data[1] + " 「" + csv_data[2] + "」",content="無し",condition=1,task_seq=int(csv_data[0]))
            add_datas.append(sub)

        # 第1.5部の場合
        elif int(csv_data[0]) >= 27 and int(csv_data[0]) <= 45:
            main = MainTask.objects.get(types=1,task_seq=2)
            sub = SubTask(main_task=main,title=csv_data[1] + " 「" + csv_data[2] + "」",content="無し",condition=1,task_seq=int(csv_data[0])-26)
            add_datas.append(sub)

        # 第2部前編の場合
        elif int(csv_data[0]) >= 46 and int(csv_data[0]) <= 55:
            main = MainTask.objects.get(types=1,task_seq=3)
            sub = SubTask(main_task=main,title=csv_data[1] + " 「" + csv_data[2] + "」",content="無し",condition=1,task_seq=int(csv_data[0])-45)
            add_datas.append(sub)

        # 第2部中編の場合
        elif int(csv_data[0]) >= 56 and int(csv_data[0]) <= 66:
            main = MainTask.objects.get(types=1,task_seq=4)
            sub = SubTask(main_task=main,title=csv_data[1] + " 「" + csv_data[2] + "」",content="無し",condition=1,task_seq=int(csv_data[0])-56)
            add_datas.append(sub)

        # 第2部後編の場合
        elif int(csv_data[0]) >= 67 and int(csv_data[0]) <= 74:
            main = MainTask.objects.get(types=1,task_seq=5)
            sub = SubTask(main_task=main,title=csv_data[1] + " 「" + csv_data[2] + "」",content="無し",condition=1,task_seq=int(csv_data[0])-67)
            add_datas.append(sub)

    SubTask.objects.bulk_create(add_datas) #最後に一気に追加




# 外典クエスト情報の追加
def add_gaiten():
    add_datas = [] #作成クエリの配列の配列
    csv_datas = open_csv_to_list("./static/csv/anaden_gaiten.csv") #csvを二次元リストに変換
    print(csv_datas)

    for csv_data in csv_datas:
        #剣の唄と失楽の翼の場合(種類が増えたらストーリーと同じく分岐させる)
        main = MainTask.objects.get(types=2,task_seq=1)
        sub = SubTask(main_task=main,title=csv_data[1] + " 「" + csv_data[2] + "」",content="無し",condition=1,task_seq=int(csv_data[0]))
        add_datas.append(sub) 

    SubTask.objects.bulk_create(add_datas) #最後に一気に追加



# 外伝クエスト情報の追加(メイン)
def add_gaiden_main():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_main_gaiden')

    for csv_data in csv_datas:
        # 外伝情報の作成
        main = MainTask(title=csv_data[1],types=3,task_seq=int(csv_data[1]))
        add_datas.append(main)

    MainTask.objects.bulk_create(add_datas)


# 外伝クエスト情報の追加(サブ)
def add_gaiden_sub():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_sub_gaiden')

    for csv_data in csv_datas:
        main = MainTask.objects.get(types=3,task_seq=int(csv_data[0]))
        # 特殊処理(また変わるかも)
        title = csv_data[2].replace('：','').replace('"','').replace('「','').replace('」','').replace('攻略','')
        sub = SubTask(main_task=main,title=title[0:3] + ' 「' + title[3:]+ '」',task_seq=int(csv_data[1]))
        add_datas.append(sub)

    SubTask.objects.bulk_create(add_datas)



# 邂逅クエスト情報の追加(メイン)
def add_kaikou_main():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_main_kaikou')

    for csv_data in csv_datas:
        main = MainTask(title=csv_data[1],types=4,task_seq=int(csv_data[0]))
        add_datas.append(main)

    MainTask.objects.bulk_create(add_datas)


# 邂逅クエスト情報の追加(サブ)
def add_kaikou_sub():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_sub_kaikou')

    for csv_data in csv_datas:
        main = MainTask.objects.get(types=4,task_seq=int(csv_data[0]))
        title = csv_data[2]
        sub = SubTask(main_task=main,title=title,task_seq=int(csv_data[1]))
        add_datas.append(sub)

    SubTask.object.bulk_create(add_datas)


# 断章クエスト情報の追加(メイン)
def add_dansyo_main():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_main_dansyo')

    for csv_data in csv_datas:
        main = MainTask(title=csv_data[1],types=5,task_seq=int(csv_data[0]))
        add_datas.append(main)

    MainTask.objects.bulk_create(add_datas)


# 断章クエスト情報の追加(サブ)
def add_dansyo_sub():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_sub_dansyo')

    for csv_data in csv_datas:
        main = MainTask.objects.get(types=5,task_seq=int(csv_data[0]))
        title = csv_data[2].replace("：","")
        sub = SubTask(main_task=main,title=title[0:3] + " 「" + title[3:] + "」",task_seq=int(csv_data[1]))
        add_datas.append(sub)

    SubTask.pbjects.bulk_create(add_datas)


# 協奏クエスト情報の追加(メイン)
def add_kyouso_main():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_main_kyouso')


# 協奏クエスト情報の追加(サブ)
def add_kyouso_sub():
    add_datas = []
    csv_datas = open_csv_to_list('./static/csv/anaden_sub_kyouso')