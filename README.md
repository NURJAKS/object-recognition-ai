# 🧠 Object Recognition AI

Проект по распознаванию объектов с помощью искусственного интеллекта.  
ИИ обучен распознавать такие объекты, как **кружка**, **учебник**, **зубная паста** и другие, используя изображения, полученные с камеры в реальном времени.

## 🚀 Возможности

- Распознаёт объекты через веб-камеру.
- Выводит название распознанного объекта прямо на экране.
- Использует простую модель (KNN) для классификации.
- Быстрая настройка и запуск.

## 🗂️ Структура проекта

project/
├── data/
│ ├── cup/
│ ├── textbook/
│ ├── toothpaste/
│ └── background/
├── main.py
├── resize.py
├── requirements.txt
└── README.md

## ⚙️ Установка
в терминале
git clone https://github.com/ТВОЙ_ЛОГИН/object-recognition-ai.git
cd object-recognition-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🧪 Использование
Добавь изображения в папку data/ по категориям.

Измени размер с помощью:

в терминале:
python3 resize.py
Запусти модель:

в терминале:
python3 main.py
💡 Заметки
Все изображения должны быть размером 64x64 и в форматах .jpg или .jpeg.

Можно подключить внешнюю USB-камеру (указав cv2.VideoCapture(1)).

📦 Зависимости
OpenCV

NumPy

Scikit-learn

Joblib
---

Готово. Сохрани это в `README.md` и добавь:

в терминале:
git add README.md
git commit -m "Add README"
git push



🧑‍💻 Автор
Nurbek Abildaev – 2025
