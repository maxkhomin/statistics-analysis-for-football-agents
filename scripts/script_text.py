import pandas as pd
import tkinter as tk

df = pd.read_csv('../data/player_premier_league_stats.csv', delimiter=";")
df_teams = pd.read_csv('../data/squad_premier_league_stats.csv', delimiter=",")


def goals(df: pd.DataFrame, cndname: str, cndval: str, intname: str, intval: int) -> pd.DataFrame:
    """ Функция генерации отчетов о количестве голов для одного строкового
    и одного целочисленного (макс.) критериев с выводом на экран
    Автор: Хомин Максим

    Parameters
    ----------
    df : pd.DataFrame - исходная таблица с данными об игроках
    cndname : str - атрибут критерия
    cndval : str - значение критерия
    intname : str - атрибут критерия
    intval : int - максимальное значение критерия
    Returns
    -------
    filtered_df : pd.DataFrame - отчет.
    """
    filtered_df = df[(df[cndname] == cndval) & (df[intname] <= intval)][['Player', intname, 'Squad', 'Goals']]
    filtered_text = filtered_df.to_string(index=False)

    display_window = tk.Toplevel()
    display_window.title("Результаты")

    text_widget = tk.Text(display_window, wrap="none")
    text_widget.insert('1.0', filtered_text)
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar_y = tk.Scrollbar(display_window, command=text_widget.yview)
    scrollbar_y.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(display_window, orient="horizontal", command=text_widget.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    text_widget.config(xscrollcommand=scrollbar_x.set)

    filtered_df.to_csv('../output/report1.txt', sep=';', index=False)
    return filtered_df


def statistics() -> pd.DataFrame:
    """
    Функция для генерации отчетов статистики для основных количественных переменных
    Автор: Петросян Гурген

    Parameters
    ----------
    count : количество непустых (непропущенных) значений в столбце.
    mean : среднее арифметическое значение для всех значений в столбце.
    std : стандартное отклонение, которое измеряет разброс значений от среднего значения. Большое стандартное
    отклонение указывает на большой разброс, а маленькое - на то, что значения сгруппированы близко к среднему.
    min : минимальное значение в столбце.
    25% (первый квартиль) : значение, ниже которого попадает 25% значений столбца. Это также называется 25-м процентилем.
    50% (медиана) : значение, ниже которого попадает 50% значений столбца. Это также называется медианой.
    75% (третий квартиль) : значение, ниже которого попадает 75% значений столбца. Это также называется 75-м процентилем.
    max : максимальное значение в столбце.
    Returns
    -------
    statistics_df : pd.DataFrame - отчет с основными статистическими показателями
    """

    variables = ['Age', 'Goals', 'Match_Play', '90s_played', 'Assist', 'xG']

    statistics_df = df[variables].describe().T

    display_window = tk.Toplevel()
    display_window.title("Результаты")

    text_widget = tk.Text(display_window, wrap="none")
    text_widget.insert('1.0', statistics_df.to_string())
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar_y = tk.Scrollbar(display_window, command=text_widget.yview)
    scrollbar_y.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(display_window, orient="horizontal", command=text_widget.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    text_widget.config(xscrollcommand=scrollbar_x.set)

    statistics_df.to_csv('../output/report2.txt', sep=';', index=False)
    return statistics_df


def xAG(df: pd.DataFrame, cndname_1: str, cndval_1: str) -> pd.DataFrame:
    """ Функция генерации отчетов о сравнении реальных ассистов игрока с его xAG для
    одного строкового критерия
    Автор: Данилов Игорь

    Parameters
    ----------
    df : pd.DataFrame - исходная таблица с данными об игроках
    cndname_1 : str - атрибут критерия 1
    cndval_1 : str - значение критерия 1
    Returns
    -------
    filtered_df : pd.DataFrame - отчет.
    """
    filtered_df = df[df[cndname_1] == cndval_1][['Player', '90s_played', 'Assist', 'xAG']]
    filtered_df.to_csv('../output/report3.txt', sep=';', index=False)

    filtered_text = filtered_df.to_string(index=False)

    display_window = tk.Toplevel()
    display_window.title("Результаты")

    text_widget = tk.Text(display_window, wrap="none")
    text_widget.insert('1.0', filtered_text)
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar_y = tk.Scrollbar(display_window, command=text_widget.yview)
    scrollbar_y.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(display_window, orient="horizontal", command=text_widget.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    text_widget.config(xscrollcommand=scrollbar_x.set)
    return filtered_df

def create_pivot_table(df: pd.DataFrame, index_col1: str, index_col2: str, values_col: str,
                       agg_func: str) -> pd.DataFrame:
    """
    Функция для создания сводной таблицы на основе входных параметров
    Автор: Хомин Максим

    Parameters
    ----------
    df: pd.DataFrame - исходная таблица с данными
    index_col1: str - название первого качественного столбца для использования в качестве индекса
    index_col2: str - название второго качественного столбца для использования в качестве индекса
    values_col: str - название количественного столбца для агрегации
    agg_func: str - метод агрегации

    Returns
    -------
    pivot_table : pd.DataFrame - Сводная таблица на основе входных параметров
    """
    pivot_table = pd.pivot_table(df, values=values_col, index=index_col1, columns=index_col2, aggfunc=agg_func,
                                 fill_value=0)

    display_window = tk.Toplevel()
    display_window.title("Результаты")

    text_widget = tk.Text(display_window, wrap="none")
    text_widget.insert('1.0', pivot_table.to_string())
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar_y = tk.Scrollbar(display_window, command=text_widget.yview)
    scrollbar_y.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(display_window, orient="horizontal", command=text_widget.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    text_widget.config(xscrollcommand=scrollbar_x.set)

    pivot_table.to_csv('../output/report4.txt', sep=';', index=True)
    return pivot_table
