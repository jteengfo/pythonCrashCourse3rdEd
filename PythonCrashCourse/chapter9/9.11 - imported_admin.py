'''Start with your work from Exercise 9-8 (page 173). Store
the classes User, Privileges, and Admin in one module. Create a separate file,
make an Admin instance, and call show_privileges() to show that everything is
working correctly.'''

from personnel import User, Privileges, Admin

admin_1 = Admin('kaye', 'lee', 'calgary', '26')

admin_1.privileges.add_privileges(['call boss', 'print documents', 'design projects'])

admin_1.privileges.show_privileges()