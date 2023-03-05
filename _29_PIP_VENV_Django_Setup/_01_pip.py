"""
# PIP is a package manager for Python packages, or modules if you like.

>> What is a Package and Module?

A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

# Check if PIP is Installed

pip --version

# Using a Package

pip install camelcase

# Remove a Package

pip uninstall camelcase

# List Packages

pip list
"""
# 
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))