'''Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly'''


from admin import Admin

admin_1 = Admin('kaye', 'lee', 'calgary', '26')

admin_1.privileges.add_privileges(['call boss', 'print documents', 'design projects'])

admin_1.privileges.show_privileges()