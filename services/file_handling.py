import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    ch = ',.!:;?'
    ssize = size
    if len(text) <= size + start:
        ssize = len(text)-start
    else:
        for i in range(size+start-1, start, -1):
            if text[i] in ch and text[i+1] not in ch:
                break
            ssize -= 1
    return [text[start:i].rstrip(), ssize]


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(file=path, mode='r', encoding='utf-8') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0],
                os.path.normpath(BOOK_PATH)))
