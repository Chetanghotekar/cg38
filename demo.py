https://github.com/akashkolhe0512/cg38/blob/main/demo.py

Here’s a complete Set 2 with answers for your exam or interview prep:

---

**1. Create and configure a Scrum project in Jira:**

- Go to **Jira Dashboard > Projects > Create Project**.  
- Select **Scrum** under **Agile templates**.  
- Name your project, choose key and project type (team-managed or company-managed).  
- Click **Create**.  
- Configure by adding team members, creating boards, setting up sprints, and defining issue types (Story, Task, Bug, Epic).

---

**2. JQL to find issues where status changed from “To Do” to “In Progress” in the last 7 days:**

```jql
status CHANGED FROM "To Do" TO "In Progress" AFTER -7d
```

---

**3. Find overdue issues assigned to yourself using JQL:**

```jql
assignee = currentUser() AND due <= now() AND resolution = Unresolved
```

---

**4. Show unresolved tasks from the current sprint using JQL:**

```jql
project = "YourProjectName" AND sprint in openSprints() AND issuetype = Task AND resolution = Unresolved
```

*(Replace `YourProjectName` with your actual project key)*

---

**5. Git commands to stage, commit with message, and push to remote:**

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

---

**6. Create a GitHub repo, add a README.md, and share with a teammate. Create a new Git branch for a feature and merge it after completion:**

```bash
# Create GitHub repo on the site (or use CLI)
# Clone the repo
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Add README.md
echo "# My Project" > README.md
git add README.md
git commit -m "Add README"
git push origin main

# Share: Go to repo > Settings > Collaborators > Add teammate’s GitHub username

# Create and switch to feature branch
git checkout -b feature-branch

# After changes
git add .
git commit -m "Add new feature"
git push origin feature-branch

# Merge (on GitHub: create pull request and merge)
# Or using Git CLI:
git checkout main
git merge feature-branch
git push origin main
```

---

Let me know if you'd like a cheat sheet version or visuals for any part!
