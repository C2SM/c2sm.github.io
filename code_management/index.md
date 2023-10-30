---
title: Coding Best Practices
layout: default
nav_order: 5
has_children: false
---

# Coding Best Practices
If you're new to coding or already working on it, remember two important things: always **use version control** and **add automatic tests**.
These steps will help you and anyone you work with to make things easier.

## Version Control with Git
**Git** is a popular tool for managing source code. C2SM repositories are hosted on GitHub, which uses Git as its version control system.

If you're new to Git or want to improve your Git skills, we recommend attending our annual **Git for Beginners** and/or **Git for Advanced** courses.
Additionally, all course materials are publicly available and can be used throughout the year.
For more details, please visit [Technical Events - Git Courses](https://c2sm.github.io/events/git_courses.html).

### Key Concepts of Git

#### 1. Repository (Repo)

A Git repository is a container for a software project. It stores the complete history of the project, including all files, directories, and changes made over time. Repositories can be hosted locally or remotely on platforms like GitHub, GitLab, or Bitbucket.

#### 2. Commit

A commit is a fundamental concept in Git, representing a snapshot of the codebase at a specific point in time. Each commit is identified by a unique SHA-1 hash, contains a descriptive message explaining the changes, and references the previous commit, forming a version history.

#### 3. Branch

Branches allow developers to work on separate lines of development. The primary branch is usually named "master" or "main," while feature branches enable the development of new features or bug-fix branches for addressing issues without affecting the main codebase.

#### 4. Merge

Merging is the process of combining changes from one branch into another. Git provides tools to automatically or manually resolve conflicts that may arise when merging different branches.

#### 5. Pull Request (PR)

In a collaborative development environment, developers use pull requests to propose changes from their branches to the main branch. Changes are reviewed, discussed, and, if approved, merged into the main codebase.

### GitHub Workflow


## Automatic Testing
Code testing is a critical step in software development. It's about finding and fixing problems to make sure the software works well, is of high quality and reliable.
Testing involves checking different parts of the code to make sure the software is strong and free of bugs.

### Tests
The specific tests you need will depend on your project and its requirements. Here is a list of tests that are usually very useful.
#### 1. Unit Tests
Link to spack-c2sm
#### 2. Integrations Tests
Link to spack-c2sm
#### 3. System Tests
Link to spack-c2sm
#### 3. Functional Tests
#### 4. Regression Tests
#### 5. Performance Tests
#### 6. Security Tests
#### 7. GitHooks & GitHub actions
Link to Git course. Example for GitHub actions (Micha)
#### 8. Tolerance test

