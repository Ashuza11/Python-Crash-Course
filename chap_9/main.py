from admin_one import Admin

# Question 9-11. Imported Admin
admin = Admin("Dan", "Ash", "M", 35)
admin.describe_user()
print("This is the admin privileges: ")
admin.privilege.show_privileges()