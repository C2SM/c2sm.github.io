---
title: Coding Best Practices
layout: default
nav_order: 5
has_children: false
---

# Coding Best Practices
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
  - TOC
  {:toc}
</details>

If you're new to coding or already working on it, remember two important things: always **use version control** and **add automatic tests**.
These steps will help you and anyone you work with to make things easier. Also, try out tools that can make coding easier for you.

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
The specific tests you need will depend on your project and its requirements. Here is a list of tests that are usually very useful.
### 1. Unit Tests
These tests are for testing individual components or functions of your code to ensure they work correctly in isolation.
Find an [example for unit tests](https://github.com/C2SM/spack-c2sm/blob/main/test/unit_test.py) in our spack-c2sm repository. It can be executed by running `python3 test/unit_test.py` (after creating and activating the respective environment).
### 2. Integrations Tests
These tests are to check how different parts of your code work together and communicate.
Find an [example for integration tests](https://github.com/C2SM/spack-c2sm/blob/main/test/integration_test.py) in our spack-c2sm repository. It can be executed by running `python3 test/integration_test.py` (after creating and activating the respective environment).
### 3. System Tests
These tests are performed to ensure that all the components and modules of a software system work together as intended and that the system meets its specified requirements and functions correctly in its operational environment.
Find an [example for system tests](https://github.com/C2SM/spack-c2sm/blob/main/test/system_test.py) (wrong!) in our spack-c2sm repository. It can be executed by running `python3 test/system_test.py` (after creating and activating the respective environment).
### 4. Tolerance tests
These tests are used for the development of ICON, specifically when code is ported from CPU to GPU. The results when running on CPU and GPU are not bit identical, therefore a tolerance range is accepted when comparing a test case to the CPU reference. The accepted tolerance range is created by running an ensemble of the same test case with different perturbations. MeteoSwiss has development [probtest](https://github.com/MeteoSwiss/probtest) for handling everything related to tolerance tests with ICON. If you have a DKRZ account and are working with ICON-NWP, you can also check out the manual for [Generating tolerances for non-standard tests](https://gitlab.dkrz.de/icon/wiki/-/wikis/GPU-development/Validating-with-probtest-without-buildbot-references-(Generating-tolerances-for-non-standard-tests)).
### 5. Git Hooks & GitHub Actions
Git Hooks are local scripts in Git that make sure things get done right when you work on your code. GitHub Actions, on the other hand, are integrated with GitHub and allow you to automate code management workflows. They can be run automatically on GitHub whenever something is committed.

Check out our Git course for examples of [Custom Git Hooks](https://github.com/C2SM/git-course/blob/main/advanced/Exercise_7_git-hooks.md) hooks, and read GitHub's [documentation on GitHub Actions](https://docs.github.com/en/actions).


## Useful tools for coding
Two popular tools for coding are [Visual Studio (VS) Code](https://code.visualstudio.com) and [PyCharm](https://www.jetbrains.com/pycharm/). Here are instructions for setting up and using Visual Studio Code with SSH on a CSCS machine.
### VS Code
1. [Download](https://code.visualstudio.com/download) and install VS Code on your computer.
2. Install extensions:
    - Open VS Code.
    - Look for the "Extensions" icon in the sidebar (it looks like four small squares).
    - Install the extensions you need for your coding work. We recommend:
        - Python: for Python development support
        - GitLens: to improve Git functionality
        - vim: if you prefer Vim keybindings
        - Remote-SSH: to connect to remote machines
3. Use VS Code with SSH on CSCS:
    - Install the "Remote-SSH" extension.
    - [Ensure VS Code remains active when working on CSCS](https://confluence.cscs.ch/display/KB/VScode+gets+killed)
