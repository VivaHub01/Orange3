import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette(['#1f77b4', '#ff7f0e', '#2ca02c'])

df = pd.read_csv('StudentPerformanceFactors.csv')

print("Датасет загружен!")
print(f"Размерность: {df.shape}")
print(f"Колонки: {df.columns.tolist()}")
print("\nПервые 5 строк:")
print(df.head())

features_for_clustering = ['Hours_Studied', 'Attendance', 'Sleep_Hours']

for feat in features_for_clustering:
    if feat not in df.columns:
        print(f"Предупреждение: признак {feat} не найден в датасете")

X = df[features_for_clustering].copy()

print(f"\nПропущенные значения до обработки:\n{X.isnull().sum()}")
X = X.dropna()
print(f"После удаления пропусков: {X.shape}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nСтатистика после масштабирования:")
print(f"Среднее: {X_scaled.mean(axis=0).round(2)}")
print(f"Стд: {X_scaled.std(axis=0).round(2)}")

n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)

df_clustered = X.copy()
df_clustered['Cluster'] = cluster_labels

df_clustered['Cluster_Name'] = df_clustered['Cluster'].map({0: 'C1', 1: 'C2', 2: 'C3'})

print("\nКластеризация завершена!")
print("Распределение по кластерам:")
print(df_clustered['Cluster_Name'].value_counts().sort_index())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
cluster_names = ['C1', 'C2', 'C3']

for cluster in range(n_clusters):
    cluster_data = df_clustered[df_clustered['Cluster'] == cluster]
    plt.scatter(cluster_data['Hours_Studied'], 
                cluster_data['Attendance'],
                c=colors[cluster],
                label=f'C{cluster+1}',
                alpha=0.6,
                s=50,
                edgecolors='white',
                linewidth=0.5)

plt.xlabel('Hours_Studied', fontsize=12)
plt.ylabel('Attendance', fontsize=12)
plt.title('Кластеры: Hours_Studied vs Attendance', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

centroids = scaler.inverse_transform(kmeans.cluster_centers_)
for i, centroid in enumerate(centroids):
    plt.scatter(centroid[0], centroid[1], 
                c='red', marker='X', s=200, 
                edgecolors='black', linewidth=2,
                label=f'Центроид C{i+1}' if i == 0 else "")

plt.subplot(1, 2, 2)

for cluster in range(n_clusters):
    cluster_data = df_clustered[df_clustered['Cluster'] == cluster]
    plt.scatter(cluster_data['Sleep_Hours'], 
                cluster_data['Attendance'],
                c=colors[cluster],
                label=f'C{cluster+1}',
                alpha=0.6,
                s=50,
                edgecolors='white',
                linewidth=0.5)

plt.xlabel('Sleep_Hours', fontsize=12)
plt.ylabel('Attendance', fontsize=12)
plt.title('Кластеры: Sleep_Hours vs Attendance', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ПРОФИЛИ КЛАСТЕРОВ (СРЕДНИЕ ЗНАЧЕНИЯ)")
print("="*60)

centroid_df = pd.DataFrame(centroids, columns=features_for_clustering)
centroid_df['Cluster'] = [f'C{i+1}' for i in range(n_clusters)]
centroid_df = centroid_df.set_index('Cluster')

print("\nСредние значения признаков по кластерам:")
print(centroid_df.round(1))

plt.figure(figsize=(10, 6))
centroid_df.T.plot(kind='bar', color=colors)
plt.title('Профили кластеров (средние значения)', fontsize=14)
plt.xlabel('Признаки', fontsize=12)
plt.ylabel('Среднее значение', fontsize=12)
plt.legend(title='Кластер')
plt.xticks(rotation=0)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("СТАТИСТИКА ПО КЛАСТЕРАМ")
print("="*60)

for cluster in range(n_clusters):
    print(f"\nКластер C{cluster+1} ({len(df_clustered[df_clustered['Cluster']==cluster])} студентов):")
    for feat in features_for_clustering:
        mean_val = df_clustered[df_clustered['Cluster']==cluster][feat].mean()
        std_val = df_clustered[df_clustered['Cluster']==cluster][feat].std()
        print(f"  {feat}: {mean_val:.1f} ± {std_val:.1f}")

print("\n" + "="*60)
print("ИНТЕРПРЕТАЦИЯ КЛАСТЕРОВ")
print("="*60)

interpretations = {
    0: {
        'name': 'C1 — "Академические звёзды"',
        'desc': 'Высокая посещаемость, много часов учебы, нормальный сон',
        'role': 'Лидеры проекта, эксперты'
    },
    1: {
        'name': 'C2 — "Группа риска"',
        'desc': 'Низкая посещаемость, мало часов учебы',
        'role': 'Требуют внимания, могут быть креативными'
    },
    2: {
        'name': 'C3 — "Середняки"',
        'desc': 'Средние показатели по всем признакам',
        'role': 'Стабильные исполнители, основа команды'
    }
}

for cluster in range(n_clusters):
    print(f"\n{interpretations[cluster]['name']}")
    print(f"  Характеристика: {interpretations[cluster]['desc']}")
    print(f"  Роль в проекте: {interpretations[cluster]['role']}")

print("\n" + "="*60)
print("ФОРМИРОВАНИЕ СБАЛАНСИРОВАННЫХ ПРОЕКТНЫХ КОМАНД")
print("="*60)

def create_balanced_teams(df, n_teams=5):
    clusters = df['Cluster'].unique()
    cluster_students = {}
    
    for cluster in clusters:
        cluster_students[cluster] = df[df['Cluster'] == cluster].index.tolist()
    
    for cluster in clusters:
        np.random.shuffle(cluster_students[cluster])
    
    teams = {}
    team_id = 1
    
    max_teams = min(len(cluster_students[cluster]) for cluster in clusters)
    max_teams = min(max_teams, n_teams)
    
    for i in range(max_teams):
        team_members = []
        for cluster in sorted(clusters):
            if i < len(cluster_students[cluster]):
                team_members.append(cluster_students[cluster][i])
        
        if len(team_members) == len(clusters):
            teams[f"Team_{team_id:02d}"] = team_members
            team_id += 1
    
    return teams

teams = create_balanced_teams(df_clustered, n_teams=6)

print(f"\nСформировано {len(teams)} сбалансированных команд:")
print("-" * 70)

for team_name, members in teams.items():
    print(f"\n{team_name}:")
    for idx, student_idx in enumerate(members):
        student_data = df_clustered.loc[student_idx]
        cluster_name = f"C{student_data['Cluster']+1}"
        print(f"  Студент {idx+1} (индекс {student_idx}) — Кластер {cluster_name}: "
              f"Hours={student_data['Hours_Studied']:.0f}, "
              f"Att={student_data['Attendance']:.0f}%, "
              f"Sleep={student_data['Sleep_Hours']:.1f}h")

output_file = 'student_clusters_python.csv'
df_clustered.to_csv(output_file)
print(f"\nРезультаты сохранены в файл: {output_file}")

centroid_file = 'cluster_profiles.csv'
centroid_df.to_csv(centroid_file)
print(f"Профили кластеров сохранены в файл: {centroid_file}")

print("\n" + "="*60)
print("ГОТОВО! Кластеризация успешно выполнена.")
print("="*60)