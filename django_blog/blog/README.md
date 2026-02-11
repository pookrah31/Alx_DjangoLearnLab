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

# Django Blog – Comment System

## Overview
The comment system allows users to leave comments on blog posts, edit their own comments, and delete them. It enhances interactivity and fosters discussion.

---

## Comment Features

### Viewing Comments
- All comments for a post are displayed on the post detail page.
- Visible to all users, including anonymous visitors.

### Creating Comments
- Only logged-in users can post comments.
- URL pattern: `/posts/<post_id>/comments/new/`
- CSRF protection is enforced on the form.
- Upon submission, the comment is linked to the logged-in user and the relevant post.

### Editing Comments
- Only the comment author can edit their comment.
- URL pattern: `/comment/<comment_id>/update/`
- Unauthorized users receive a 403 Forbidden response.

### Deleting Comments
- Only the comment author can delete their comment.
- URL pattern: `/comment/<comment_id>/delete/`
- Users must confirm deletion before removal.

---

## Permissions
- `LoginRequiredMixin` prevents anonymous users from posting comments.
- `UserPassesTestMixin` ensures that only comment authors can edit or delete their comments.

---

## Testing Instructions
1. Run the development server:
   ```bash
   python manage.py runserver
