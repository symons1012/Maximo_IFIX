change_directory('employee_folder')
 copy_file('./install_required_packages.py', '../auto_gpt_workspace/maximo_ifixes/install_required_packages.py')
 execute_python_file('auto_gpt_workspace/maximo_ifixes/install_required_packages.py')
 update_aws_configuration()