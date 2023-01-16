import uuid
from django.db import models


class BaseModel(models.Model):
    """Baseモデル"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.IntegerField()
    created_user = models.UUIDField(null=True)
    updated_user = models.UUIDField(null=True)

    class Meta:
        abstract = True


class Music(BaseModel):
    """楽曲モデル"""

    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'music'


class Memo(BaseModel):
    """メモモデル"""

    memo = models.TextField(null=True, max_length=1000)
    music = models.ForeignKey(Music, on_delete=models.PROTECT)

    class Meta:
        db_table = 'memo'


class Difficulty(BaseModel):
    """難易度モデル"""

    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'difficulty'


class MusicDifficulty(BaseModel):
    """楽曲・難易度モデル"""

    music = models.ForeignKey(Music, on_delete=models.PROTECT)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    level = models.IntegerField()

    class Meta:
        db_table = 'music_difficulty'
