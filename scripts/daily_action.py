#!/usr/bin/env python3
"""
毛选行动力 - 每日计划生成器
Usage: python3 daily_action.py [--plan|--review]
"""
import sys
import os
from datetime import datetime

TEMPLATE_PLAN = """# 毛选行动力 - 每日作战计划
日期：{date}    阶段判定：

## 主要矛盾
（哪件事不做会让你内心惶恐？写出唯一答案）
-> 

## 局部战场（从小到大排列）
战场1（5min）：-> 
战场2（15min）：-> 
战场3（30min）：-> 

## 启动协议
1. 停下来，拿出白纸
2. 识别主要矛盾 -> 上面那件事
3. 拆解到极小 -> 战场1
4. 立刻动手，不做任何准备
5. 初战必胜！
"""

TEMPLATE_REVIEW = """# 毛选行动力 - 每日复盘
日期：{date}

## 事实记录（不带情绪）
- 今日主要矛盾完成情况：
- 拖延发生时间：
- 当时任务：
- 实际做了什么：

## 冰冷分析
触发原因：
□ 任务未拆解 -> 用「集中优势兵力」拆解
□ 追求完美 -> 用「实践论」先做烂版
□ 硬磕卡壳 -> 用「运动战」转移战线
□ 外部干扰 -> 消除干扰源
□ 精力不足 -> 调整任务量，保存有生力量

病灶诊断（具体到时间+场景）：

## 明日战壕
针对性措施：
明日主要矛盾：
第一个局部战场（<5min）：
"""

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--review":
        content = TEMPLATE_REVIEW.format(date=today)
        filename = f"review_{today}.md"
    else:
        content = TEMPLATE_PLAN.format(date=today)
        filename = f"plan_{today}.md"
    
    # Write to current directory
    with open(filename, "w") as f:
        f.write(content)
    
    print(f"已生成: {filename}")
    print("记住：丢掉幻想，准备斗争！只争朝夕！")

if __name__ == "__main__":
    main()
