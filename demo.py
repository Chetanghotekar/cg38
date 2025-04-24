
### 📌 1️⃣ Navigate Jira to find the active sprint board and sprint backlog.

**Steps:**
1. Login to your **Jira** account.
2. From the sidebar, click on **"Boards"** or select your project.
3. Go to **Active Sprints** — you’ll see the current sprint board.
4. Below it or inside the board view, you'll find the **Sprint Backlog** (list of all tasks planned for the sprint).

---

### 📌 2️⃣ Create an Epic and link stories to it in Jira.

**Steps:**
1. Go to your **Jira Project**.
2. In the sidebar, click on **"Backlog"**.
3. On the left side, look for **Epics panel**.
4. Click **"+ Create Epic"**, give it a name, summary, and save.
5. To link stories:
   - Create a new issue (story) or open an existing one.
   - In the issue view, find the **Epic Link** field.
   - Select your created epic from the dropdown.
   - Save changes.

---

### 📌 3️⃣ Write a JQL to find all unresolved tasks assigned to Team-A.

**JQL Query:**

assignee = "Team-A" AND resolution = Unresolved


**Steps to run it:**
1. Go to **Filters** → **Advanced issue search**.
2. Switch to **JQL** mode.
3. Paste the above query.
4. Run it to see the results.

---

### 📌 4️⃣ Merge changes into the main branch after Pull Request approval.

**Steps (GitHub Example):**
1. Push your feature branch changes to GitHub.
2. Create a **Pull Request (PR)** from your branch to `main`.
3. Request reviewers and wait for **approval**.
4. Once approved:
   - Go to the PR page.
   - Click on **"Merge pull request"**.
   - Confirm by clicking **"Confirm merge"**.
5. Now your changes are merged into the `main` branch.

---

### 📌 5️⃣ JQL: Filter issues where assignee is EMPTY (unassigned).

**JQL Query:- assignee is EMPTY


**Steps to run it:**
1. Go to **Filters** → **Advanced issue search**.
2. Switch to **JQL** mode.
3. Paste this query.
4. Run to view all unassigned issues.

---

### 📌 6️⃣ Merge changes into the main branch after Pull Request approval (Same as point 4)

**Steps (Repeated):**
1. Push branch changes to the repo.
2. Open a Pull Request to merge into `main`.
3. Wait for review and approval.
4. Click **"Merge pull request"**.
5. Confirm merge.


