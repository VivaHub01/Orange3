# Python
## Графики:
![one](/images/cluster-python1.png)
![two](/images/cluster-python2.png)
![three](/images/cluster-python3.png)
## Вывод:
Датасет загружен!
Размерность: (4999, 20)
Колонки: ['Hours_Studied', 'Attendance', 'Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities', 'Sleep_Hours', 'Previous_Scores', 'Motivation_Level', 'Internet_Access', 'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality', 'School_Type', 'Peer_Influence', 'Physical_Activity', 'Learning_Disabilities', 'Parental_Education_Level', 'Distance_from_Home', 'Gender', 'Exam_Score']

Первые 5 строк:
   Hours_Studied  Attendance Parental_Involvement Access_to_Resources  ... Parental_Education_Level  Distance_from_Home  Gender Exam_Score
0             23          84                  Low                High  ...              High School                Near    Male         67
1             19          64                  Low              Medium  ...                  College            Moderate  Female         61
2             24          98               Medium              Medium  ...             Postgraduate                Near    Male         74
3             29          89                  Low              Medium  ...              High School            Moderate    Male         71
4             19          92               Medium              Medium  ...                  College                Near  Female         70

[5 rows x 20 columns]

Пропущенные значения до обработки:
Hours_Studied    0
Attendance       0
Sleep_Hours      0
dtype: int64
После удаления пропусков: (4999, 3)

Статистика после масштабирования:
Среднее: [ 0.  0. -0.]
Стд: [1. 1. 1.]

Кластеризация завершена!
Распределение по кластерам:
Cluster_Name
C1    1689
C2    1391
C3    1919
Name: count, dtype: int64

============================================================
ПРОФИЛИ КЛАСТЕРОВ (СРЕДНИЕ ЗНАЧЕНИЯ)
============================================================

Средние значения признаков по кластерам:
         Hours_Studied  Attendance  Sleep_Hours
Cluster
C1                19.8        89.3          8.0
C2                19.7        83.9          5.3
C3                20.5        68.8          7.4

============================================================
СТАТИСТИКА ПО КЛАСТЕРАМ
============================================================

Кластер C1 (1689 студентов):
  Hours_Studied: 19.8 ± 6.1
  Attendance: 89.3 ± 6.4
  Sleep_Hours: 8.0 ± 1.0

Кластер C2 (1391 студентов):
  Hours_Studied: 19.7 ± 5.8
  Attendance: 84.0 ± 9.6
  Sleep_Hours: 5.3 ± 0.7

Кластер C3 (1919 студентов):
  Hours_Studied: 20.5 ± 6.0
  Attendance: 68.8 ± 5.4
  Sleep_Hours: 7.4 ± 1.1

============================================================
ИНТЕРПРЕТАЦИЯ КЛАСТЕРОВ
============================================================

C1 — "Академические звёзды"
  Характеристика: Высокая посещаемость, много часов учебы, нормальный сон
  Роль в проекте: Лидеры проекта, эксперты

C2 — "Группа риска"
  Характеристика: Низкая посещаемость, мало часов учебы
  Роль в проекте: Требуют внимания, могут быть креативными

C3 — "Середняки"
  Характеристика: Средние показатели по всем признакам
  Роль в проекте: Стабильные исполнители, основа команды

============================================================
ФОРМИРОВАНИЕ СБАЛАНСИРОВАННЫХ ПРОЕКТНЫХ КОМАНД
============================================================

Сформировано 6 сбалансированных команд:
----------------------------------------------------------------------

Team_01:
  Студент 1 (индекс 957) — Кластер C1: Hours=23, Att=95%, Sleep=7.0h
  Студент 2 (индекс 310) — Кластер C2: Hours=19, Att=97%, Sleep=6.0h
  Студент 3 (индекс 4015) — Кластер C3: Hours=17, Att=63%, Sleep=6.0h

Team_02:
  Студент 1 (индекс 2902) — Кластер C1: Hours=17, Att=82%, Sleep=7.0h
  Студент 2 (индекс 2303) — Кластер C2: Hours=22, Att=68%, Sleep=4.0h
  Студент 3 (индекс 2989) — Кластер C3: Hours=34, Att=68%, Sleep=7.0h

Team_03:
  Студент 1 (индекс 2021) — Кластер C1: Hours=22, Att=91%, Sleep=8.0h
  Студент 2 (индекс 3034) — Кластер C2: Hours=20, Att=93%, Sleep=6.0h
  Студент 3 (индекс 4997) — Кластер C3: Hours=39, Att=67%, Sleep=5.0h

Team_04:
  Студент 1 (индекс 2001) — Кластер C1: Hours=19, Att=82%, Sleep=7.0h
  Студент 2 (индекс 835) — Кластер C2: Hours=21, Att=97%, Sleep=6.0h
  Студент 3 (индекс 3897) — Кластер C3: Hours=24, Att=72%, Sleep=10.0h

Team_05:
  Студент 1 (индекс 3014) — Кластер C1: Hours=16, Att=94%, Sleep=8.0h
  Студент 2 (индекс 1385) — Кластер C2: Hours=22, Att=79%, Sleep=6.0h
  Студент 3 (индекс 2844) — Кластер C3: Hours=21, Att=67%, Sleep=7.0h

Team_06:
  Студент 1 (индекс 3266) — Кластер C1: Hours=15, Att=98%, Sleep=8.0h
  Студент 2 (индекс 1694) — Кластер C2: Hours=21, Att=61%, Sleep=4.0h
  Студент 3 (индекс 4608) — Кластер C3: Hours=24, Att=75%, Sleep=8.0h

Результаты сохранены в файл: student_clusters_python.csv
Профили кластеров сохранены в файл: cluster_profiles.csv

============================================================
ГОТОВО! Кластеризация успешно выполнена.
============================================================