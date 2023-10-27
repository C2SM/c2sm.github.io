---
title: Code Management
layout: default
nav_order: 3
has_children: false
---

# Code Management
If you're new to coding or already working on it, remember two important things: always **use version control** and **add automatic tests**.
These steps will help you and anyone you work with to make things easier.

## Version Control with Git
**Git** is a popular tool for managing source code. C2SM repositories are hosted on GitHub, which uses Git as its version control system.

If you're new to Git or want to improve your Git skills, we recommend attending our annual **Git for Beginners** and/or **Git for Advanced** courses.
Additionally, all course materials are publicly available and can be used throughout the year.
For more details, please visit [Technical Events - Git Courses](https://c2sm.github.io/events/git_courses.html).

### Key Concepts

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


## Code Testing

Code or software testing, is a critical phase in the software development process aimed at identifying and eliminating defects and ensuring the functionality, 
quality, and reliability of a software application. It involves systematic evaluation and validation of various components 
and aspects of the code. Code testing is essential to deliver robust and error-free software.

### Purpose of Code Testing

The primary objectives of code testing are:

1. **Defect Detection:** Identifying and addressing defects, bugs, and issues in the software code to prevent them from reaching end-users.

2. **Quality Assurance:** Ensuring that the software meets specified requirements and performs as expected, meeting user needs and expectations.

3. **Performance Evaluation:** Assessing the software's speed, scalability, and resource utilization under various conditions.

4. **Usability Testing:** Evaluating the user-friendliness and user experience of the software.

5. **Regression Testing:** Ensuring that code changes do not introduce new issues and that existing functionality remains intact.


### Importance of Code Testing

Code testing is vital in software development because it:

- Enhances software quality and reliability.
- Reduces the cost of bug fixing in later development stages.
- Identifies issues early in the development process, allowing for quicker resolutions.
- Ensures that the software meets user requirements and expectations.
- Supports continuous improvement and software maintenance.
