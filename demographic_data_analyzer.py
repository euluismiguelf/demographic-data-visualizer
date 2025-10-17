import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer los datos del archivo CSV
    df = pd.read_csv("adult.data.csv")

    # 1. Número de personas de cada raza
    race_count = df['race'].value_counts()

    # 2. Edad media de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentaje de personas con una licenciatura
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Personas con educación avanzada
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 5. Porcentaje de personas con educación avanzada que ganan >50K
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Porcentaje de personas sin educación avanzada que ganan >50K
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 7. Número mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 8. Porcentaje de personas que trabajan el mínimo y ganan >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 9. País con el mayor porcentaje de personas que ganan >50K
    country_rich_ratio = (
        df[df['salary'] == '>50K']['native-country'].value_counts() /
        df['native-country'].value_counts() * 100
    ).dropna()

    highest_earning_country = country_rich_ratio.idxmax()
    highest_earning_country_percentage = round(country_rich_ratio.max(), 1)

    # 10. Ocupación más popular para quienes ganan >50K en India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Número de personas por raza:\n", race_count)
        print("Edad media de los hombres:", average_age_men)
        print("Porcentaje de personas con licenciatura:", percentage_bachelors)
        print("Porcentaje con educación avanzada y >50K:", higher_education_rich)
        print("Porcentaje sin educación avanzada y >50K:", lower_education_rich)
        print("Mínimo de horas trabajadas por semana:", min_work_hours)
        print("Porcentaje con salario >50K trabajando el mínimo:", rich_percentage)
        print("País con mayor porcentaje de >50K:", highest_earning_country, highest_earning_country_percentage)
        print("Ocupación más popular en India con >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
