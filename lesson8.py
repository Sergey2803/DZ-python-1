import os
import json
import csv
import pickle

def get_dir_info(dir_path):
    result = []
    
    for root, dirs, files in os.walk(dir_path):
        parent = os.path.basename(root) if root != dir_path else dir_path
        
        # Счетчик размера для директорий
        total_size = 0
        
        # Обработка файлов
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            result.append({
                'name': file,
                'type': 'file',
                'parent': parent,
                'size': file_size
            })
            total_size += file_size

        # Обработка директорий
        for dir in dirs:
            dir_path_full = os.path.join(root, dir)
            result.append({
                'name': dir,
                'type': 'directory',
                'parent': parent,
                'size': total_size  # в данном случае, пока что устанавливаем 0
            })
        
    # После завершения обхода, обновляем размер для директорий
    return result

def save_to_json(data, path):
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, path):
    with open(path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, path):
    with open(path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

def save_directory_info(dir_path):
    dir_info = get_dir_info(dir_path)

    # Сохраняем информацию в разные форматы
    save_to_json(dir_info, 'directory_info.json')
    save_to_csv(dir_info, 'directory_info.csv')
    save_to_pickle(dir_info, 'directory_info.pkl')

if __name__ == "__main__":
    directory_path = 'your_directory_path_here'  # Укажите путь к вашей директории
    save_directory_info(directory_path)
    