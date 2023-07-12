import cv2
import numpy as np
from PIL import ImageColor


def create_video(text, color_text, color_back, fps, time, width, height):
    image = np.zeros((width, height, 3), dtype=np.uint8)

    # Параметры текста
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    line_type = cv2.LINE_AA
    R, G, B = ImageColor.getcolor(color_text, "RGB")
    color_text = (B, G, R)
    R, G, B = ImageColor.getcolor(color_back, "RGB")
    color_back = (B, G, R)

    # Параметры видео
    total_frames = fps * time

    # Создаем объект записи видео
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter('main/media/result.mp4', fourcc, fps, (width, height))

    # Генерирация видео
    text_width, text_height = cv2.getTextSize(text, font, font_scale, 1)[0]
    i = round((width + text_width) / total_frames)  # Сдвиг текста
    if i<1:
        i=1
    x = width
    y = (height + text_height) // 2
    for frame_number in range(total_frames):
        image.fill(0)
        x -= i

        cv2.rectangle(image, (0, 0), (width, height), color_back, cv2.FILLED)
        cv2.putText(image, text, (x, y), font, font_scale, color_text, 1, line_type)
        video_writer.write(image)
    video_writer.release()
    return True
