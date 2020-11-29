from django.db import models



#メインタスク「メインストーリー前編」などのタイトルが表示される
class MainTask(models.Model):
    title = models.CharField('タイトル',max_length=64)
    TYPES = (
        (1,'メインストーリー'),
        (2,'外伝'),
        (3,'オリジナルタスク'),
        (4,'その他'),
    )
    types = models.IntegerField('タイプ',choices=TYPES)
    task_seq = models.IntegerField('順序',null=True,blank=True)

    def __str__(self):
        return self.title


#サブタスク「第64話」みたいなメインに対する細かいタスクが入る
class SubTask(models.Model):
    main_task = models.ForeignKey(MainTask,on_delete=models.CASCADE)
    title = models.CharField('タイトル',max_length=128)
    content = models.TextField('詳細')
    CONDITIONS = (
        (1,'新規'),
        (2,'挑戦中'),
        (3,'完了'),
    )
    condition = models.IntegerField('状態',choices=CONDITIONS,default=1)
    task_seq = models.IntegerField('順序',null=True,blank=True)
    created_at = models.DateTimeField('作成日',auto_now=True)
    updated_at = models.DateTimeField('更新日',auto_now=True)

    def __str__(self):
        return self.title

        
    

