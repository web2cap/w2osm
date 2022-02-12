"""LayerMapping
Чтобы импортировать данные, используйте LayerMapping в сценарии Python.
Каждый ключ в словаре world_mapping соответствует полю в модели WorldBorder. Значение - это имя поля шейп-файла, из которого будут загружены данные.
Ключом mpoly для поля геометрии является MULTIPOLYGON, тип геометрии, в качестве которого GeoDjango будет импортировать поле. Даже простые полигоны в шейпфайле будут автоматически преобразованы в коллекции перед вставкой в базу данных.
Путь к шейп-файлу не является абсолютным - другими словами, если вы переместите приложение world (с подкаталогом data) в другое место, сценарий все равно будет работать.
Ключевое слово transform установлено в False, потому что данные в шейпфайле не нужно преобразовывать - они уже находятся в WGS84 (SRID=4326).
После этого вызовите оболочку Django из директории проекта geodjango:

$ python manage.py shell
Далее импортируем модуль load, вызываем процедуру run и смотрим, как LayerMapping выполняет работу:

 from world import load
 load.run()
"""
from pathlib import Path

from django.contrib.gis.utils import LayerMapping

from .models import WorldBorder

world_mapping = {
    "fips": "FIPS",
    "iso2": "ISO2",
    "iso3": "ISO3",
    "un": "UN",
    "name": "NAME",
    "area": "AREA",
    "pop2005": "POP2005",
    "region": "REGION",
    "subregion": "SUBREGION",
    "lon": "LON",
    "lat": "LAT",
    "mpoly": "MULTIPOLYGON",
}

world_shp = (
    Path(__file__).resolve().parent / "data" / "TM_WORLD_BORDERS-0.3.shp"
)


def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
