# 📝 Todo App

**🚀 Live Demo:** [https://todo-app-chi-seven-62.vercel.app/](https://todo-app-chi-seven-62.vercel.app/)

---

## 📌 About

A simple yet powerful **To-Do List Management System** built with a functional programming approach. This application allows users to create, update, and delete tasks with a clean and intuitive web interface.

The backend is written in a **functional style** where each operation (insert, delete, update, display) is a pure function that takes the current task list as input and returns a NEW task list, ensuring immutability and predictable behavior.

---

## ✨ Features

- ✅ **Add Tasks** - Create new to-do items with a title
- ✏️ **Update Tasks** - Edit existing task titles
- 🗑️ **Delete Tasks** - Remove completed or unwanted tasks
- 📋 **View All Tasks** - Display all tasks in a sorted list
- 💾 **Flash Messages** - Get instant feedback on actions
- 🎨 **Responsive UI** - Clean and user-friendly interface

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Vercel (Serverless)
- **Architecture:** Functional Programming

---

## 📁 Project Structure

```
todo_app/
├── api/
│   └── index.py              # Flask app with functional core logic
├── public/
│   └── style.css             # Styling
├── templates/
│   └── index.html            # Main HTML template
├── static/                   # Additional static files (if any)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Git
- pip (Python package manager)

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubhbansal17/todo_app.git
   cd todo_app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python api/index.py
   ```

5. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

---

## 📤 Deploying to Vercel

### Step 1: Push to GitHub
Make sure your project is pushed to GitHub with the correct folder structure.

### Step 2: Deploy to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click **"New Project"**
3. Select your `todo_app` repository
4. Vercel will auto-detect Python/Flask
5. Click **"Deploy"** and wait for completion ✨

### Step 3: Get Your Live URL
Once deployed, you'll receive a live URL like:
```
https://your-app-name.vercel.app/
```

---

## 📖 How to Use

### Add a Task
1. Enter your task title in the input field
2. Click **"Add Task"**
3. Your task appears in the list below

### Update a Task
1. Enter the **Task ID** you want to update
2. Enter the **New Title**
3. Click **"Update Task"**

### Delete a Task
1. Enter the **Task ID** you want to delete
2. Click **"Delete Task"**

---

## 🔧 API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display all tasks |
| `/insert` | POST | Add a new task |
| `/update` | POST | Update an existing task |
| `/delete` | POST | Delete a task |

---

## 💡 Functional Programming Approach

This project follows a **functional programming paradigm**:

- **Pure Functions:** Each operation (`insert_task`, `delete_task`, `update_task`) is a pure function
- **Immutability:** Functions return a NEW list instead of mutating the existing one
- **No Classes:** Logic is separated into functions rather than object-oriented classes
- **Predictable Behavior:** Same input always produces the same output

Example:
```python
def insert_task(task_list, title, next_id):
    """Return a NEW list with a new task appended."""
    new_task = {"id": next_id, "title": title.strip()}
    return task_list + [new_task], next_id + 1
```

---

## 📝 Notes

- Tasks are stored in **in-memory storage** (data resets on server restart)
- For production use with persistent data, consider integrating a database like PostgreSQL or MongoDB
- The `secret_key` in the app should be changed for production deployment

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements!

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Shubh Bansal**  
GitHub: [@shubhbansal17](https://github.com/shubhbansal17)

---

## 🔗 Links

- 🌐 **Live Demo:** [https://todo-app-chi-seven-62.vercel.app/](https://todo-app-chi-seven-62.vercel.app/)
- 📦 **Repository:** [https://github.com/shubhbansal17/todo_app](https://github.com/shubhbansal17/todo_app)

---

**Happy task managing! ✨**
