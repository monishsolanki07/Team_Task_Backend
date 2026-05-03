<div align="center">

# 🗂️ TeamTask
### Real-Time Project Management Platform

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django_REST-092E20?style=for-the-badge&logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

*A full-stack collaborative project management app with JWT auth, role-based access, and real-time task updates.*

[Live Demo](https://team-task-frontend-alpha.vercel.app/login) · [Backend Repo](#) · [Frontend Repo](https://github.com/monishsolanki07/Team_Task_Frontend)

</div>

---

## 🚀 Key Features

- **Project Dashboards** — Visualize task statistics and project overviews at a glance.
- **Dynamic Task Management** — Create and assign tasks with specific due dates and descriptions.
- **Open Status Updates** — Any team member can update task status (`Todo`, `In Progress`, `Done`) for a truly collaborative workflow.
- **Role-Based Access** — Specialized admin controls for project creation and member assignment.
- **Secure Authentication** — JWT-based user authentication ensures secure, stateless access to all project data.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React (Vite), Tailwind CSS, Axios, React Router |
| **Backend** | Python, Django REST Framework (DRF) |
| **Database** | PostgreSQL (Production) |
| **Auth** | JSON Web Tokens (JWT) |
| **Deployment** | Backend → Render · Frontend → Vercel |
| **Dev Environment** | EndeavourOS (Linux) |

---

## 📂 Project Structure

### Frontend — `team-task-frontend/`

```
team-task-frontend/
├── src/
│   ├── api/
│   │   └── axios.js          # Centralized API client with JWT interceptors
│   ├── pages/
│   │   ├── Login.jsx         # User authentication page
│   │   ├── Projects.jsx      # Dashboard for project listing & creation
│   │   ├── ProjectDetail.jsx # Detailed view of tasks & team members
│   │   └── Dashboard.jsx     # Cross-project task stats and updates
│   ├── App.jsx               # Main routing configuration
│   └── main.jsx              # Application entry point
├── tailwind.config.js        # Tailwind styling configuration
└── package.json              # Dependencies & scripts
```

### Backend — `team-task-backend/`

```
team-task-backend/
├── config/
│   ├── settings.py           # CORS & database configuration
│   └── urls.py               # Root URL routing
├── api/
│   ├── models.py             # Project, Task, and Profile schemas
│   ├── serializers.py        # Data transformation for API endpoints
│   ├── views.py              # Business logic for projects and task updates
│   └── urls.py               # API-specific endpoint routing
└── manage.py                 # Django management script
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL

### Backend Setup

1. **Clone the repository and install dependencies:**
   ```bash
   git clone <your-repo-url>
   cd team-task-backend
   pip install -r requirements.txt
   ```

2. **Configure environment variables** — create a `.env` file:
   ```env
   SECRET_KEY=your_django_secret_key
   DATABASE_URL=your_postgresql_url
   DEBUG=True
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd team-task-frontend
   ```

2. **Install packages:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

---

## 🌐 API Configuration

To connect the frontend to your hosted backend, update the `baseURL` in `src/api/axios.js`:

```javascript
const api = axios.create({
  baseURL: "https://team-task-backend-hjpt.onrender.com",
});
```

For local development, use:

```javascript
const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});
```

---

## 📡 API Endpoints

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `POST` | `/api/token/` | Obtain JWT token pair | Public |
| `POST` | `/api/token/refresh/` | Refresh access token | Public |
| `GET` | `/api/projects/` | List all projects | Authenticated |
| `POST` | `/api/projects/` | Create a new project | Admin |
| `GET` | `/api/projects/:id/` | Retrieve project details | Authenticated |
| `GET` | `/api/tasks/` | List all tasks | Authenticated |
| `POST` | `/api/tasks/` | Create a new task | Authenticated |
| `PATCH` | `/api/tasks/:id/` | Update task status | Authenticated |

---

## 🏆 About the Developer

**Monish Solanki** — Software Developer focused on Backend Engineering and Data Structures.

- 🎓 B.Tech student at **Chandigarh University** *(Expected 2026)*
- 🥈 **1st Runner-Up** — Electrothon 7.0 @ NIT Hamirpur
- 🏁 **Finalist** — HackWithIndia 2024

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](#)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=todoist&logoColor=white)](#)

</div>

---

<div align="center">
  <sub>Built with ❤️ on EndeavourOS · Deployed on Render & Vercel</sub>
</div>
