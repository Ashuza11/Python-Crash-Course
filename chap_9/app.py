from admin_privileges import Admin

# Question 9-12. Multiple Modules
admin = Admin("Dan", "Ash", "M", 35)
admin.describe_user()
print("This is the admin privileges: ")
admin.privilege.show_privileges()