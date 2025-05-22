# ArithmeticOperation

Веб-приложение на Python (Flask) с HTML/JS фронтендом для решения арифметических задач.

---

## Установка и запуск

### 1. Скачайте проект

Клонируйте репозиторий или скачайте .zip и распакуйте:

```bash
git clone https://github.com/kk7k3r/ArithmeticOperation.git
cd ArithmeticOperation
```

---

### 2. Создайте виртуальное окружение
В папке проекта выполните следующую команду:
```bash
python -m venv venv
```

---

### 3. Активируйте окружение

#### Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

> Если видите ошибку типа *"ExecutionPolicy"*, выполните:
>
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

---

### 4. Установите зависимости

```bash
pip install -r requirements.txt
```

---

### 5. Запустите приложение

```bash
python -m web.app
```

Если всё прошло успешно, приложение будет доступно по адресу:

[http://localhost:5000](http://localhost:5000)

---


## ⚠️ Важно
**Не размещайте проект в папке с кириллицей или пробелами** (например, `C:\Users\Иван\Мой проект\`) — это может вызвать ошибки запуска.

---
