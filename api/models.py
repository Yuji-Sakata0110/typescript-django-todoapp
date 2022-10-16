from django.db import models

# api経由でDBとのどんなやり取りをするか決定する。
class TodoTable (models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    # print out 時にプリントアウトすべき項目をここで決定する。
    def __str__(self):
        return self.text
