import sys
import time

def animated_loading(message: str = "Scanning"):
    """
    Показывает анимацию загрузки с точками.
    """
    # Цикл по количеству точек
    for i in range(4):
        # Строка, которую мы будем выводить: "Scanning." -> "Scanning.." -> "Scanning..."
        output = f"\r{message}{'.' * i}"
        
        # Вывод строки в консоль
        sys.stdout.write(output)
        
        # flush=True гарантирует, что текст немедленно отобразится, а не будет ждать буфера
        sys.stdout.flush()
        
        # Небольшая задержка
        time.sleep(0.5)

# --- Использование ---
print("Please wait!!")

# Цикл выполнения анимации
for _ in range(5): # Повторим анимацию 5 раз
    animated_loading()
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

# В конце очищаем строку, чтобы курсор остался на следующей чистой строке
# \r возвращает курсор в начало, а пробелы затирают старый текст
sys.stdout.write('\r' + ' ' * 20 + '\r')
sys.stdout.flush()

print("Scan finished!")
