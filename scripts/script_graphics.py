import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

output_dir = "../graphics/"


def plot_clustered_bar_chart(player_data, TEAM_1, TEAM_2, POSITIONS):
    """ Функция генерации кластеризованной столбчатой диаграммы для двух команд,
    сравнивающая суммарное количество голов игроков по позициям среди этих команд.
    Автор: Данилов Игорь

    Parameters
    ----------
    player_data : pd.DataFrame - исходная таблица с данными об игроках
    TEAM_1 : str - название команды 1
    TEAM_2 : str - название команды 2
    POSITIONS : list - позиции, по которым идёт сравнение
    Returns
    -------
    None
    """
    goals_1, goals_2 = [0 for _ in range(len(POSITIONS))], [0 for _ in range(len(POSITIONS))]

    for i in range(len(player_data)):
        player = player_data[i]
        if player[3] == TEAM_1:
            for j in range(len(POSITIONS)):
                if POSITIONS[j] in player[2]:
                    goals_1[j] += int(player[7])
        if player[3] == TEAM_2:
            for j in range(len(POSITIONS)):
                if POSITIONS[j] in player[2]:
                    goals_2[j] += int(player[7])

    bar_width = 0.32
    x = range(len(POSITIONS))

    plt.bar(x, goals_1, width=bar_width, label=TEAM_1)
    plt.bar([i + bar_width for i in x], goals_2, width=bar_width, label=TEAM_2)

    plt.xlabel('Позиции игроков')
    plt.ylabel('Суммарное количество голов')
    plt.title('Кластеризованная столбчатая диаграмма')
    plt.xticks([i + bar_width / 2 for i in x], POSITIONS)
    plt.legend()

    plt.savefig(os.path.join(output_dir, "1.png"))
    plt.show()


def plot_histogram(teams_data, teams):
    """ Функция генерации категоризированной гистограммы, показывающей средний
    возраст игроков выбранных команд с добавлением значений на график.
    Автор: Хомин Максим

    Parameters
    ----------
    teams_data : pd.DataFrame - исходная таблица с данными о командах
    teams : list - список выбранных команд
    Returns
    -------
    None
    """
    average_ages = []
    for team in teams_data:
        if team[0] in teams:
            average_ages.append(team[1])

    plt.bar(teams, average_ages, color='skyblue')

    plt.title('Категоризированная гистограмма')
    plt.xlabel('Команды')
    plt.ylabel('Средний возраст')

    for i in range(len(teams)):
        plt.text(i, average_ages[i], str(average_ages[i]), ha='center', va='bottom')

    plt.savefig(os.path.join(output_dir, "2.png"))
    plt.show()


def plot_boxplot(player_data, teams):
    """ Функция генерации категоризированной диаграммы (box-and-whiskers)
    для параметра "гол+пас" игроков из выбранных команд
    Автор: Петросян Гурген

    Parameters
    ----------
    player_data : pd.DataFrame - исходная таблица с данными об игроках
    teams : list - список выбранных команд
    Returns
    -------
    None
    """
    team_indices = {team: idx for idx, team in enumerate(teams)}
    poss_by_mass = [[] for _ in range(len(teams))]

    for player in player_data:
        for team in teams:
            if player[3] == team:
                team_idx = team_indices[team]
                poss_by_mass[team_idx].append(player[8])
                break

    data = {team: ages for team, ages in zip(teams[:5], poss_by_mass[:5])}

    box_data = [ages for team, ages in data.items()]

    plt.boxplot(box_data)
    plt.xticks(range(1, len(data) + 1), data.keys())
    plt.xlabel("Команды")
    plt.ylabel("Гол+пас")
    plt.title("Категоризированная диаграмма")

    plt.savefig(os.path.join(output_dir, "3.png"))
    plt.show()


def plot_scatter(player_data, TEAM, TEAM_2):
    """ Функция генерации категоризированной диаграммы рассеивания для
    двух выбранных команд, показывающей количество помощей игроков
    Автор: Данилов Игорь

    Parameters
    ----------
    player_data : pd.DataFrame - исходная таблица с данными об игроках
    TEAM : str - название команды 1
    TEAM_2 : str - название команды 2
    Returns
    -------
    None
    """
    goals, assist, current_player = [], [], []
    goals_2, assist_2, current_player_2 = [], [], []

    for i in range(len(player_data)):
        if player_data[i, 3] == TEAM:
            current_player.append(player_data[i, 0])
            goals.append(player_data[i, 7])
            assist.append(player_data[i, 8])
        if player_data[i, 3] == TEAM_2:
            current_player_2.append(player_data[i, 0])
            goals_2.append(player_data[i, 7])
            assist_2.append(player_data[i, 8])

    plt.scatter(goals, assist, label=TEAM)
    plt.scatter(goals_2, assist_2, label=TEAM_2)

    plt.xlabel("Количество голов")
    plt.ylabel("Количество ассистов")
    plt.title('Категоризированная диаграмма рассеивания')

    plt.legend()
    plt.savefig(os.path.join(output_dir, "4.png"))
    plt.show()

# data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#         'salary': [50000, 60000, 80000, 130000, 40000]}
# df = pd.DataFrame(data)
#
# Q1 = df['salary'].quantile(0.25)
# Q3 = df['salary'].quantile(0.75)
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5* IQR
# upper_bound = Q3 + 1.5*IQR
# outliers = df[(df['salary'] < lower_bound) | (df['salary'] > upper_bound)]
# print(outliers)
