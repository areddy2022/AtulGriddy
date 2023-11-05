import pandas as pd

# 2019 - 2022 Draft_Year

list_pngav = []

df_fy = 2022  # final year available in the data frame
df_ry = 2018  # if a player was drafted to the NFL after this date, they are considered a rookie that needs interpolated data
df_adp_av = pd.read_csv('adp_av_final.csv')
df_summed_data = pd.read_csv('summed_data_sloan.csv')


def find_rookie():
    for c_index, row in df_summed_data.iterrows():
        p_dy = row['Draft_Year']
        if int(p_dy) > df_ry:
            p_name = (row['Player'])
            p_pick = (row['Pick_Number'])
            p_cav = (row['Weighted Griddy AV'])  # current AV in summed_data
            df_dy_c = "drafted_" + str(p_dy)  # dataframe draft year column
            p_interpolated = df_adp_av.loc[p_pick - 1, df_dy_c]  # player's interpolated av
            p_ngav = p_cav + p_interpolated
        else:
            p_name = (row['Player'])
            p_ngav = (row['Weighted Griddy AV'])
        list_pngav.append([p_name, p_ngav])
    save()


def save():
    df = pd.DataFrame(list_pngav, columns=['Name', 'Griddy AV'])
    filename = 'output.csv'
    df.to_csv(filename, index=False)
    print(f'Data written to {filename}')


find_rookie()
