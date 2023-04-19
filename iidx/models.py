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


class GeneralCodeCategory(BaseModel):
    """汎用コードカテゴリーモデル"""

    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'general_code_category'


class GeneralCode(BaseModel):
    """汎用コードモデル"""

    name = models.CharField(max_length=30)
    category = models.ForeignKey(GeneralCodeCategory, on_delete=models.PROTECT)
    code = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        db_table = 'general_code'


class Music(BaseModel):
    """楽曲モデル"""

    title = models.CharField(max_length=100, default="")
    genre = models.CharField(max_length=100, default="")
    artist = models.CharField(max_length=100, default="")
    version = models.ForeignKey(GeneralCode, on_delete=models.PROTECT, default="")

    class Meta:
        db_table = 'music'


class Memo(BaseModel):
    """メモモデル"""

    memo = models.TextField(null=True, max_length=1000)
    music = models.ForeignKey(Music, on_delete=models.PROTECT)

    class Meta:
        db_table = 'memo'


class MusicDifficulty(BaseModel):
    """楽曲・難易度モデル"""

    music = models.ForeignKey(Music, on_delete=models.PROTECT)
    difficulty = models.ForeignKey(GeneralCode, on_delete=models.PROTECT)
    level = models.IntegerField()

    class Meta:
        db_table = 'music_difficulty'
