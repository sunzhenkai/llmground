#!/bin/python3

from langchain.agents import tool


@tool
def get_weather_info(location: str) -> str:
    """获取指定位置的天气信息"""
    return f"{location}今天天气晴, 最高气温 28 摄氏度，最低气温 20 摄氏度"
