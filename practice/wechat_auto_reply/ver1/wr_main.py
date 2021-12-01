import pyautogui  # 搜索相应匹配的图片,然后就会点击
import pyperclip  # 文本复制粘贴

# task list
tasklist = [{
    "type": "click pict",
    "content": "red1.png"
}, {
    "type": "input",
    "content": "auto reply"
}, {
    "type": "click pict",
    "content": "send1.png"
}]


def mouse_click(image):
    """find the region of the image, then click it"""
    location = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    if location is not None:
        pyautogui.click(location.x,
                        location.y,
                        clicks=1,
                        interval=0.2,
                        duration=0.2,
                        button="left")
        return True
    else:
        return False


def execute_task(task):
    if task["type"] == "click pict":
        image = task["content"]
        return mouse_click(image)
    elif task["type"] == "input":
        text = task["content"]
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        return True


if __name__ == "__main__":
    while True:
        i = 0
        while i < len(tasklist):
            if execute_task(tasklist[i]):
                i += 1
            else:
                print("listening ...")
