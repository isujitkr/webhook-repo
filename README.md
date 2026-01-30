# GitHub Webhook Listener

This project implements a GitHub webhook listener that captures repository activity events, stores them in MongoDB, and displays the latest updates in a React-based user interface.

The application demonstrates end-to-end webhook handling, backend data persistence, and frontend polling.

---

## Overview

The system consists of the following components:

- **action-repo**  
  A GitHub repository used to generate events such as Push, Pull Request, and Merge.

- **webhook-repo (this repository)**  
  A backend service that receives GitHub webhook events, stores them in MongoDB, and exposes APIs for a frontend UI.

- **React Frontend**  
  Periodically polls the backend every 15 seconds and displays the latest repository activity.

---

## Tech Stack

### Backend
- Python
- Flask
- MongoDB
- PyMongo

### Frontend
- React
- JavaScript

---

## Supported GitHub Events

- PUSH  
- PULL_REQUEST  
- MERGE  

> Note: When a pull request is merged, GitHub emits both a MERGE event and a PUSH event (for the merge commit). This behavior is expected and reflects real GitHub event flow.

---

## Application Flow

1. A user performs an action (push, pull request, merge) in `action-repo`
2. GitHub sends a webhook payload to this application
3. Flask processes the webhook and stores the event in MongoDB
4. React frontend polls the backend every 15 seconds
5. The latest events are displayed in the UI

---

## MongoDB Schema

```json
{
  "_id": "ObjectId",
  "request_id": "string",
  "author": "string",
  "action": "PUSH | PULL_REQUEST | MERGE",
  "from_branch": "string | null",
  "to_branch": "string",
  "timestamp": "UTC datetime"
}

```

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/isujitkr/webhook-repo.git

2. Navigate to the project directory
   ```bash
   cd webhook-repo
   
3. Set up environment variables in the .env file for MongoDB connection string.
   ```bash
   # In backend directory
   PORT=5000
   MONGODB_URI=
   DB_NAME=

   # In frontend directory
   VITE_DOMAIN=http://localhost:5000

4. Create and Activate Virtual Environment
   ```bash
   cd backend
   python -m venv venv
   for Windows
     venv\Scripts\activate
   for macOS / Linux
    source venv/bin/activate


5. Install dependencies for frontend and backend:
   ```bash
   cd frontend
   npm install
   cd ../backend
   pip install -r requirements.txt

6. Run both the client and server:
   ```bash
   # From the backend directory
   python app.py

   # From the frontend directory
   npm run dev
