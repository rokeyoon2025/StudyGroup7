import os

""" PART1. 데이터셋 준비 """

print("현재 디렉토리")
print(os.getcwd())  # 현재 디렉토리를 사용하여 경로 설정

import pandas as pd

# 데이터셋 가져오기(type: csv -> df)
info = pd.read_csv(os.path.join(os.getcwd(), 'heroes_information.csv'))
abilities = pd.read_csv(os.path.join(os.getcwd(), 'heroes_abilities.csv'))

# # 데이터셋 확인하기
# print('heroes_information.cev 확인하기 \n', info.head(3))
# print('heroes_abilities.csv 확인하기 \n', abilities.head(3))

# print(info.info())          # 캐릭터 기본 정보
# print(abilities.info())     # 캐릭터 보유 능력

""" PART2. 데이터셋 병합 """

merged_data = pd.merge(info, abilities)
# print(merged_data.head())     # 병합된 데이터프레임 확인하기
# print(merged_data.info())     # 캐릭터 기본 정보 & 보유 능력

import numpy as np

# 결측치 처리하기(-99 -> NaN)
merged_data.replace(-99, np.nan, inplace=True)
# print(merged_data.isnull().sum())

# 결측치 제거하기(NaN을 제거)
final_data = merged_data.dropna(axis=0, how='any')
# print(final_data.head())    # 최종 데이터셋 확인하기
# print(final_data.info())

# # [ 추가 ] 최종 데이터셋 CSV 파일로 받기
# final_data.to_csv(os.path.join(, 'final_data.csv'), index=False)
