import os, time
import pyautogui as pg


class ANSI:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[m"


def print_red(text):
    """打印红色文本"""
    print(ANSI.RED + text + ANSI.RESET)


def print_green(text):
    """打印绿色文本"""
    print(ANSI.GREEN + text + ANSI.RESET)


def get_date():
    """获取当前日期和时间"""
    return pg.time.strftime("%Y年%m届%d日 %H:%M:%S - ", pg.time.localtime())


def sleep(seconds):
    """休眠的异常处理"""
    try:
        time.sleep(seconds)
    except:
        print_red("程序被强制退出")
        exit()


# 已弃用
# def open_game():
#     """打开元梦并解除省电模式，耗时3秒"""
#     print(get_date() + "寻找并打开游戏")
#     # 设置游戏图标的坐标并移到改坐标，然后点击
#     x, y = 1000, 1125
#     pg.moveTo(x, y, duration=1)
#     pg.click()
#     sleep(1)
#     # 点击屏幕中间解除省电模式
#     x, y = 900, 585
#     # print("解除省电模式")
#     pg.click(x, y)
#     sleep(1)

# 已弃用
# def open_browser():
#     '''打开浏览器，耗时2秒'''
#     # print("打开浏览器")
#     print(get_date() + "打开浏览器")
#     x, y = 600, 1125
#     pg.click(x, y)
#     sleep(1)
#     pg.moveTo(1770, 675, duration=1)
#     pg.click()


def open_ymzx():
    """打开元梦，耗时2秒"""
    os.system("open -a '元梦之星-云游戏-快捷方式'")
    print(get_date() + "打开元梦")
    sleep(1)


def open_browser():
    """打开抖音，耗时1秒"""
    os.system("open -a 'Google Chrome'")
    print(get_date() + "打开浏览器")
    sleep(1)
    pg.press("down")
    sleep(1)
    pg.press("up")


def farm():
    """收获农场，耗时1秒"""
    # print("收获农场")
    # x, y = 1360, 715
    # pg.click(x, y)
    print(get_date() + "收获农场中...")
    pg.press("Q")
    sleep(1)


def pasture():
    """收获牧场，耗时1秒"""
    # x, y = 1540, 640
    # pg.click(x, y)
    print(get_date() + "收获牧场中...")
    pg.press("E")
    sleep(1)


def find_drones():
    """寻找无人机，耗时2秒"""
    # 重置位置后，按下a键一秒钟
    print(get_date() + "寻找无人机...")
    pg.press("r")
    pg.keyDown("a")
    sleep(1)
    pg.keyUp("a")
    print(get_date() + "找到无人机")


def start():
    print_red(get_date() + "开始执行")
    num = 1
    while True:
        print_green(get_date() + "第{}次执行".format(num))

        # 收获农场
        open_ymzx()
        find_drones()
        farm()
        open_browser()
        print(get_date() + "休息2分钟...")
        # 休息2分钟
        sleep(120)

        # 收获牧场
        open_ymzx()
        find_drones()
        pasture()
        open_browser()

        # 判断是否执行了11次的倍数
        if num % 11 == 0:
            print_red(get_date() + "已收获{}波".format(num // 11))
        num += 1
        print(get_date() + "休息2分钟...")
        # 休息2分钟左右（时间根据实际情况调整，尽量控制浇水后时间减少的是一分钟）
        sleep(110)


if __name__ == "__main__":
    # 执行任务
    start()
