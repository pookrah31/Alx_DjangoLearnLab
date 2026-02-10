# Django Blog Project

## Setup
1. Install dependencies: `pip install django`
2. Navigate to project root: `cd django_blog`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Run server: `python manage.py runserver`

## Notes
- Database: SQLite (default)
- Admin: /admin
- Static files: blog/static/blog/
- Templates: blog/templates/blog/


Step 6: Test Blog Post Features
Testing Guidelines:
Test each view for functionality and security. Ensure that all forms submit data correctly and that unauthorized users cannot edit or delete posts they do not own.
Check the navigation between views and ensure all links are correctly set up and functional.
Step 7: Documentation
Feature Documentation:
Document the blog post features in a README file or directly in the code as comments. Include details on how to use each feature and any special notes about permissions and data handling.