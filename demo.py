Set 2:
1. Create and configure a Scrum project in Jira.
2. Write JQL to find issues where status changed from “To Do” to “In
Progress” in the last 7 days.
3. Find overdue issues assigned to yourself using JQL.
4. Show unresolved tasks from the current sprint using JQL.
5. Git commands to stage, commit with message, and push to remote.
6. Create a GitHub repo, add a README.md, and share with a
teammate.Create a new Git branch for a feature and merge it after
completion.

Here are the answers to **Set 2** in a clear, practical format:

---

### **1. Create and configure a Scrum project in Jira**
**Steps:**
1. Login to Jira.
2. Click **“Projects” → “Create project”**.
3. Choose **“Scrum”** under **Agile templates**.
4. Click **“Use template”** → Choose a name for the project.
5. Set project key (optional) → Choose **Team-managed** or **Company-managed**.
6. Click **“Create project”**.
7. Configure the board by adding sprints, epics, and tasks.

---

### **2. Write JQL to find issues where status changed from “To Do” to “In Progress” in the last 7 days**
```JQL
status CHANGED FROM "To Do" TO "In Progress" DURING (-7d, now())
```

---

### **3. Find overdue issues assigned to yourself using JQL**
```JQL
assignee = currentUser() AND due <= now() AND resolution = Unresolved
```

---

### **4. Show unresolved tasks from the current sprint using JQL**
```JQL
project = "YourProjectName" AND sprint in openSprints() AND resolution = Unresolved AND issuetype = Task
```

> Replace `"YourProjectName"` with your actual project name or key.

---

### **5. Git commands to stage, commit with message, and push to remote**
```bash
git add .
git commit -m "Your commit message"
git push origin main  # or your branch name
```

---

### **6. Create a GitHub repo, add a README.md, and share with a teammate. Create a new Git branch for a feature and merge it after completion.**

**Steps:**
1. Go to [GitHub](https://github.com) → Click **“New repository”**.
2. Name your repo → Select options → Click **“Create repository”**.
3. Clone it to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
4. Add a README.md:
   ```bash
   echo "# Project Title" > README.md
   git add README.md
   git commit -m "Add README"
   git push origin main
   ```
5. Share: Go to the repo → Click **“Settings” → “Collaborators”** → Add teammate by username or email.

**Create and merge a feature branch:**
```bash
git checkout -b feature/my-feature
# work on code
git add .
git commit -m "Add my feature"
git push origin feature/my-feature

# Create a pull request on GitHub and merge it
```

---

Let me know if you want a markdown/pdf version of this or a visual guide!
