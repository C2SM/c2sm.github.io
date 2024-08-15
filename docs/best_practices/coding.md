# Coding

Whether you're new to coding or already working on it, there are two important things to remember: always **use version control** and **add automatic testing**. These steps will make things easier for you and everyone you work with. Also, try out tools that can make coding easier for you.

## Version Control with Git

**Git** is a popular tool for managing source code. C2SM repositories are hosted on GitHub, which uses Git as its version control system.

If you're new to Git or want to improve your Git skills, we recommend attending our annual **Git for Beginners** and/or **Git for Advanced** courses.
Additionally, all course materials are publicly available and can be used throughout the year.
For more details, please visit [Technical Events - Git Courses](../events/git_courses.md).

### Key Concepts of Git

- **Repository (Repo)**: A Git repository is a container for a software project. It stores the complete history of the project, including all files, directories, and changes made over time. Repositories can be hosted locally or remotely on platforms like GitHub, GitLab, or Bitbucket.
- **Commit**: A commit is a fundamental concept in Git, representing a snapshot of the codebase at a particular point in time. Each commit is identified by a unique SHA-1 hash, contains a descriptive message explaining the changes, and references the previous commit, forming a version history.
- **Branches**: Branches allow developers to work on separate lines of development. The primary branch is usually called 'master' or 'main', while feature branches enable the development of new features or bug-fix branches for addressing issues without affecting the main codebase.
- **Merge**: Merging is the process of combining changes from one branch into another. Git provides tools to automatically or manually resolve conflicts that may arise when merging different branches.

### GitHub Workflow

When working together with Git, follow these simple steps for a smooth collaborative process:

1. **Clone**: Get a copy of the remote repository you want to work on.
2. **Branch Out**: Create a branch with a name that describes your development.
3. **Development Zone**: Work on your feature within that branch.
4. **Pull Request (PR)**: When you are finished, open a pull request from your feature branch to the main one. Request a review.
5. **Refinement**: Make any necessary changes until it's approved.
6. **Merge Time**: Once the revisions are done and the tests are green, merge your feature branch into the main branch.

## Automatic Testing

Code testing is a critical step in software development. It's about finding and fixing problems to make sure the software works well, is of high quality and reliable.
Testing involves checking different parts of the code to make sure the software is strong and free of bugs.
The specific tests you need will depend on your project and its requirements. Here is a list of tests that are usually very useful.

### Unit Tests

These tests are for testing individual components or functions of your code to ensure they work correctly in isolation.
Find an [example for unit tests](https://github.com/C2SM/spack-c2sm/blob/main/test/unit_test.py){:target="_blank"} in our spack-c2sm repository.

### Integrations Tests

These tests are to check how different parts of your code work together and communicate with each other.
Find an [example for integration tests :material-open-in-new:](https://github.com/C2SM/spack-c2sm/blob/main/test/integration_test.py) in our spack-c2sm repository.

### System Tests

These tests are performed to ensure that all the components and modules of a software system work together as intended and that the system meets its specified requirements and functions correctly in its operational environment.
Find an [example for system tests :material-open-in-new:](https://github.com/C2SM/spack-c2sm/blob/main/test/system_test.py){:target="_blank"} in our spack-c2sm repository.

### Tolerance tests

These tests are used in the development of ICON, specifically when code is ported from CPU to GPU. The results when running on CPU and GPU are not bit identical, therefore a tolerance range is accepted when comparing a test case to the CPU reference. The accepted tolerance range is created by running an ensemble of the same test case with different perturbations. MeteoSwiss has developed [probtest :material-open-in-new:](https://github.com/MeteoSwiss/probtest){:target="_blank"} for handling everything related to tolerance tests with ICON. If you have a DKRZ account and are working with ICON-NWP, you can also check out the manual for [Generating tolerances for non-standard tests :material-open-in-new:](https://gitlab.dkrz.de/icon/wiki/-/wikis/GPU-development/Validating-with-probtest-without-buildbot-references-(Generating-tolerances-for-non-standard-tests){:target="_blank"}).

### Git Hooks & GitHub Actions

Git Hooks are local scripts in Git that make sure things get done right when you work on your code. GitHub Actions, on the other hand, are integrated with GitHub and allow you to automate code management workflows. They can be run automatically on GitHub whenever something is committed.

Check out our Git course for examples of [Custom Git Hooks :material-open-in-new:](https://github.com/C2SM/git-course/blob/main/advanced/Exercise_7_git-hooks.md){:target="_blank"} hooks, and read GitHub's [documentation on GitHub Actions :material-open-in-new:](https://docs.github.com/en/actions){:target="_blank"}.

## Useful tools for coding

Two popular tools for coding are [Visual Studio (VS) Code :material-open-in-new:](https://code.visualstudio.com){:target="_blank"} and [PyCharm :material-open-in-new:](https://www.jetbrains.com/pycharm/){:target="_blank"}. Here are instructions for setting up and using Visual Studio Code with SSH on a CSCS machine.

### VS Code

1. [Download :material-open-in-new:](https://code.visualstudio.com/download){:target="_blank"} and install VS Code on your computer.
2. Install extensions:
    - Open VS Code.
    - Look for the 'Extensions' icon in the sidebar (it looks like four small squares).
    - Install the extensions you need for your coding work. We recommend:
        - Python: for Python development support
        - GitLens: to improve Git functionality
        - vim: if you prefer Vim keybindings
        - Remote-SSH: to connect to remote machines
3. Use VS Code with SSH on CSCS:
    - Install the "Remote-SSH" extension.
    - Ensure VS Code remains active when working on CSCS:
        - Activate the "Remote.SSH: Remote Server Listen On Socket" option in "Remote-SSH: Settings".