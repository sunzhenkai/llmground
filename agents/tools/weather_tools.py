#!/bin/python3
import json

from langchain.agents import tool
import os
import requests

# 心知天气 API 密钥
SENIVERSE_API_SECRET_KEY = os.getenv('SENIVERSE_API_SECRET_KEY')


@tool
def get_weather_info(location: str) -> str:
    """获取指定位置的天气信息"""
    url = f"https://api.seniverse.com/v3/weather/now.json?key={SENIVERSE_API_SECRET_KEY}&location={location}"
    try:
        r = requests.get(url=url)
        j = r.json()['results'][0]
        # print(json.dumps(j, indent=4, ensure_ascii=False))
        return f"地点: {j['location']['name']}, 现在天气: {j['now']['text']}, 气温: {j['now']['temperature']} 摄氏度"
    except  Exception as e:
        print(e)
    return '获取天气信息失败'
