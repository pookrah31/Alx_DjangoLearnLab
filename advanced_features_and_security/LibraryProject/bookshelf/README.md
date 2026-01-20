# Bookshelf Permissions & Groups

## Groups
- Admins: can_view, can_create, can_edit, can_delete
- Editors: can_view, can_create, can_edit
- Viewers: can_view

## How It Works
- Permissions are defined in Book model
- Groups are auto-created using Django signals after migrations
- Views are protected using @permission_required decorators

## Assigning Users
Admin → Users → Select User → Groups → Save
