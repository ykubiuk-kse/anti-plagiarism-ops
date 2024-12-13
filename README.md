# GitHub Actions Plagiarism Detection

Automated plagiarism detection system for student assignments using MOSS (Measure Of Software Similarity).

## Prerequisites

1. MOSS account and user ID from [Stanford MOSS](https://theory.stanford.edu/~aiken/moss/)
2. GitHub organization with student repositories
3. Admin access to the organization

## Setup

1. Create a new repository for the plagiarism checker
2. Copy the workflow file to `.github/workflows/moss.yml`
3. Add the MOSS script to `scripts/moss`
4. Configure GitHub Secrets:

   Settings > Secrets and variables > Actions > New repository secret:
   
   1. Add MOSS user ID: 
    ```
    Name: MOSS_USER_ID
    Value: your_moss_id
    ```
   2. Add GitHub personal token

   ```
   Name: TOKEN
   Value: your_gh_token
   ```
    _Note: make sure GH token has right permissions_:
    * _workflow_
    * _read:org_

## Usage

1. Go to the "Actions" tab in your repository
2. Select "Plagiarism Check with MOSS" workflow
3. Click "Run workflow"
4. Enter parameters:
   - `assignment_org`: name of GH organization where student assignments are located
   - `repo_pattern`: Regex pattern matching student repositories (e.g., `assignment-*`)
   - `language`: Programming language to check
   - `exclude_filter`: Patterns to exclude from file search (e.g., `SFML,CMakeFiles`)
5. Click "Run workflow"

URL with scan results will be printed at the end of `Run MOSS chacker` step

## Repository Structure
```
.
├── .github
│   └── workflows
│       └── moss.yml
├── scripts
│   └── moss.py
└── README.md
```