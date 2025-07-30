# 🚴‍♂️ Fun Habit Tracker with Pixela API in Python
A simple yet powerful habit tracker built in Python that lets you log daily activities (like cycling kilometers) visually via the Pixela API. This project showcases API integration, environment variable usage for security, and basic HTTP requests — perfect for automating your habit tracking with a clean graphical representation.

> **Note:** You can customize this tracker to log *any* habit you want — whether it's reading, meditation, water intake, or coding hours. Just change the graph's name, unit, and input prompts to fit your lifestyle!


<img width="1536" height="1024" alt="a6e573fd-3717-45a4-a267-d7b878523fd4" src="https://github.com/user-attachments/assets/75be0f81-d24f-4da9-bee2-6e09ea7e70d0" />


---

## 🚀 Features
- Create and manage a habit tracking graph on Pixela  
- Log daily quantities (e.g., kilometers cycled) via simple user input  
- Securely store and use API tokens with environment variables  
- Supports pixel creation, updating, and deletion on your graph  
- Lightweight and easy to extend for other habits or metrics 

---

## 🧠 Built With
- Python 3.7+  
- `requests` for making HTTP API calls  
- `datetime` for date formatting  
- `os` for managing environment variables  
- Pixela API for visual habit tracking (https://pixe.la)   

---

## 💻 How It Works
1. The program optionally creates a user account on Pixela (run only once).  
2. It can create a graph to track a specific habit (run only once).  
3. On each run, it asks how much of the habit you completed today and posts this as a pixel on the graph.  
4. Optionally, you can update or delete pixels if needed by uncommenting the respective sections.  

---

## Preview

![sdnas d](https://github.com/user-attachments/assets/6f44c54a-2796-46a7-b0d2-151d11a3c303)

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fun-habit-tracker.git
cd fun-habit-tracker
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Set Environment Variables

#### On Linux/macOS:
```bash
export PIXELA_USERNAME="your_pixela_username"
export PIXELA_TOKEN="your_secret_token"
```

#### On Windows (CMD):
```cmd
set PIXELA_USERNAME=your_pixela_username
set PIXELA_TOKEN=your_secret_token
```

🛡️ Keep your token secret and never commit it to public repositories.

---

## ▶️ Running the Script
After setting the environment variables, run the script:

```bash
python main.py
```

The script will prompt you to enter the quantity (e.g., km cycled today) and update your Pixela graph.

---

## 🌐 APIs Used

| API                | Purpose                                                                          |
|--------------------|----------------------------------------------------------------------------------|
|Pixela	             | 	Create user, graphs, and post pixels for habit tracking visualization           |

---

## 🧠 What You’ll Learn
- How to interact with RESTful APIs in Python
- How to manage API authentication securely with environment variables
- How to automate personal tracking and data visualization
- Handling user input and HTTP requests gracefully
- Practical use of date formatting and JSON payloads

---

## 🙌 Credits
- 👨‍💻 **Built by: Mussa Tariq
- LinkedIn: https://www.linkedin.com/in/mussa-tariq-0652712a0/
- 🔗 Pixela API – https://pixe.la

---

## 📬 Final Note
Automate your habits and visualize your progress effortlessly. Keep pushing forward—one pixel at a time! 🚀
