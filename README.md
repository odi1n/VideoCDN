# VideoCND - API

Реализация Api для сервиса VideoCDN.tv

Установка:```pip install videocdn-tv```

## Методы

Взаимодействие:

```python
from .videocdn import VideoCDN, ParamsContent, ParamsEpisode, ParamsSeason
videocdn = VideoCDN(api_token="KEY")
```

### translations

```python
data = videocdn.get_translations()
```

### movies

```python
data = videocdn.get_movies(ParamsContent(query="Аквамене"))
```

### animes

```python
data = videocdn.get_animes(ParamsContent(query="Ван-Пис: Золото"))
```

### tv-series

```python
data = videocdn.get_tv_series(ParamsContent(query="Игра Пристолов"))
```

### tv-series/seasons

```python
data = videocdn.get_tv_series_seasons(ParamsSeason(tv_series_id=1))
```

### tv-series/episodes

```python
data = videocdn.get_tv_series_episodes(ParamsEpisode(tv_series_id=1))
```

### anime-tv-series

```python
data = videocdn.get_anime_tv_series(ParamsContent(query="Доктор Стоун"))
```

### anime-tv-series/seasons

```python
data = videocdn.get_anime_tv_series_seasons(ParamsSeason(tv_series_id=1))
```

### anime-tv-series/episodes

```python
data = videocdn.get_anime_tv_series_episodes(ParamsEpisode(tv_series_id=1))
```

### show-tv-series

```python
data = videocdn.get_show_tv_series(ParamsContent(query="Зовите шефа"))
```

### show-tv-series/seasons

```python
data = videocdn.get_show_tv_series_season(ParamsSeason(tv_series_id=1))
```

### show-tv-series/episodes

```python
data = videocdn.get_show_tv_series_episodes(ParamsEpisode(tv_series_id=1))
```