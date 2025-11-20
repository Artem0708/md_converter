import os
from markitdown import MarkItDown

# Инициализация
md = MarkItDown()

input_dir = "input"
output_dir = "output"

# Создаем папку output, если её нет
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Проходим по всем файлам в папке input
for filename in os.listdir(input_dir):
    # Игнорируем скрытые файлы (например .gitkeep)
    if filename.startswith("."):
        continue
        
    input_path = os.path.join(input_dir, filename)
    
    # Проверяем, что это файл, а не папка
    if os.path.isfile(input_path):
        try:
            print(f"Конвертирую: {filename}...")
            
            # Магия конвертации
            result = md.convert(input_path)
            
            if result and result.text_content:
                # Формируем имя нового файла (меняем расширение на .md)
                base_name = os.path.splitext(filename)[0]
                output_filename = f"{base_name}.md"
                output_path = os.path.join(output_dir, output_filename)
                
                # Сохраняем результат
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result.text_content)
                print(f"Успешно сохранено: {output_filename}")
            else:
                print(f"Пустой результат для {filename}")
                
        except Exception as e:
            print(f"Ошибка при конвертации {filename}: {e}")