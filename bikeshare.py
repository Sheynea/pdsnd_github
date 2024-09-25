import pandas as pd

# 加载数据集(包含芝加哥，纽约，华盛顿）
def load_data(city, month=None, day=None):
    FILE_PATHS = {
        'chicago': 'chicago.csv',
        'new_york_city': 'new_york_city.csv',
        'washington': 'washington.csv'
    }
    df = pd.read_csv(FILE_PATHS[city])

    # 将 Start Time 转换为 datetime 类型
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # 过滤数据
    if month:
        df = df[df['Start Time'].dt.month == month]
    if day:
        df = df[df['Start Time'].dt.dayofweek == day]

    return df

# 显示统计结果(包含时间，站点，行程持续时间，用户类型计数，性别和年龄信息)
def display_statistics(df):
    # 计算常用时间
    popular_month = df['Start Time'].dt.month.mode()[0]
    popular_day = df['Start Time'].dt.day_name().mode()[0]
    popular_hour = df['Start Time'].dt.hour.mode()[0]

    # 计算常用站点
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    popular_trip = (df['Start Station'] + ' -> ' + df['End Station']).mode()[0]

    # 计算行程持续时间
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()

    # 用户类型计数
    user_types = df['User Type'].value_counts()

    # 性别和年龄信息（如果可用）
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
    else:
        gender_counts = "Not Available"

    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
    else:
        earliest_birth_year = most_recent_birth_year = most_common_birth_year = "Not Available"

    # 打印统计结果
    print(f"Popular Month: {popular_month}")
    print(f"Popular Day: {popular_day}")
    print(f"Popular Hour: {popular_hour}")
    print(f"Popular Start Station: {popular_start_station}")
    print(f"Popular End Station: {popular_end_station}")
    print(f"Popular Trip: {popular_trip}")
    print(f"Total Travel Time: {total_travel_time} seconds")
    print(f"Average Travel Time: {mean_travel_time} seconds")
    print(f"Counts of Each User Type:\n{user_types}")
    print(f"Counts of Each Gender:\n{gender_counts}")
    print(f"Earliest Birth Year: {earliest_birth_year}")
    print(f"Most Recent Birth Year: {most_recent_birth_year}")
    print(f"Most Common Birth Year: {most_common_birth_year}")

# 主函数
def main():
    while True:
        # 获取用户输入的城市
        city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
        while city not in ['chicago', 'new_york', 'washington']:
            city = input("Invalid entry. Please enter 'Chicago', 'New York', or 'Washington': ").lower()

        # 获取用户是否要过滤数据
        filter_option = input("Would you like to filter the data by month, day, or not at all? ").lower()
        while filter_option not in ['month', 'day', 'not at all']:
            filter_option = input("Invalid entry. Please enter 'month', 'day', or 'not at all': ").lower()

        month, day = None, None
        if filter_option == 'month':
            month = input("Which month - January, February, March, April, May, or June? ").title()
            while month not in ['January', 'February', 'March', 'April', 'May', 'June']:
                month = input("Invalid entry. Please enter one of the listed months: ").title()
            month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6}
            month = month_map[month]

        elif filter_option == 'day':
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").title()
            while day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                day = input("Invalid entry. Please enter one of the listed days: ").title()
            day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
            day = day_map[day]

        # 加载数据并显示统计结果
        df = load_data(city, month, day)
        display_statistics(df)

        # 是否显示原始数据
        show_raw_data = input("Would you like to see the raw data? Enter yes or no.\n").lower()
        start_loc = 0
        while show_raw_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            show_raw_data = input("Do you wish to continue?: ").lower()

        # 是否重新开始
        restart = input("\nWould you like to restart? Enter yes or no.\n").lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()