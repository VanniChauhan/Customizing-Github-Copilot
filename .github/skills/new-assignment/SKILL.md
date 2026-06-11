---
name: Create a New Assignment
description: Create a new assignment for the student portal with starter code and configuration updates.
example: "Create an assignment about Web Scraping with BeautifulSoup"
---

# Create a New Assignment

This skill helps you create new coding assignments for the student portal. It will:

1. Create a new assignment directory in `assignments/`
2. Generate a README.md following the assignment template
3. Create starter code for students
4. Update `config.json` with the new assignment details

## What You'll Need

- **Assignment Title**: A clear, descriptive name (e.g., "Web Scraping with BeautifulSoup")
- **Assignment Description**: A brief overview of what students will learn
- **Learning Objectives**: 1-2 sentences on learning goals
- **Number of Tasks**: 2-4 progressive tasks
- **Task Details**: For each task, provide a name, description, and requirements
- **Due Date**: When the assignment is due (YYYY-MM-DD format)

## Workflow

When you ask to create an assignment:

1. I'll draft the assignment structure following [assignment-template.md](../../../templates/assignment-template.md)
2. I'll create the assignment directory and files
3. I'll update `config.json` with assignment metadata
4. The new assignment will appear in the website's assignment list

## Example Request

> Create an assignment about Web Scraping with BeautifulSoup that teaches students how to extract data from websites, parse HTML, and handle errors.

This would result in:
- New directory: `assignments/web-scraping-beautifulsoup/`
- Updated `config.json` with the new assignment entry
- Full README.md with tasks and starter code
