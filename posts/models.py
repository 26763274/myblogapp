from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
# 「Djangoに対して、データベース内に記事データを保存するためのテーブル（設計図）を新しく作成する」 という宣言文
    title = models.CharField(max_length=100)
    # 記事のタイトル（見出し）を保存する列
    # CharField: 短い文字列用。max_length=100 で最大文字数を100文字に制限しています。
    
    published = models.DateTimeField()
    # 投稿日時（日付と時刻） を保存する列
    
    image = models.ImageField(upload_to='media/')
    # 記事の画像 を保存する列 
    # upload_to='media/': 画像がアップロードされたとき、保存先を media/ フォルダ内に指定
    
    body = models.TextField()
    # 記事の本文を保存する列
    # TextField: 長文のテキストを制限なく保存できる。

    likes= models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        #文字列をページに返すことができる
        return self.title
        #titleで設定したデータが一覧に返るようになる
    
    def summary(self):
        return self.body[:30]
