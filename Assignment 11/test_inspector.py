import os

from package_inspector import SourceAuditor

auditor = SourceAuditor("package_inspector.py")


# Test 1: AST function spacing
source = """def first_function():
    return 1


def second_function():
    return 2
"""

result = auditor.audit_module_structure(source)

print("TEST 1 - Function spacing")
print(result)
print()


# Test 2: Colon spacing
source = """def test(value:str):
    return value
"""

result = auditor.audit_module_structure(source)

print("TEST 2 - Colon spacing")
print(result)
print()


# Test 3: Line length
source = """def test():
    this_is_a_very_long_variable_name_that_should_make_this_line_longer_than_seventy_nine_characters = True
"""

result = auditor.audit_module_structure(source)

print("TEST 3 - Line length")
print(result)
print()


# Test 4: Trailing whitespace
source = """def test():
    return 1   
"""

result = auditor.audit_module_structure(source)

print("TEST 4 - Trailing whitespace")
print(result)
print()


# Test 5: Decorated function
source = """def first_function():
    return 1


@staticmethod
def second_function():
    return 2
"""

result = auditor.audit_module_structure(source)

print("TEST 5 - Decorated function")
print(result)
print()
print("TEST 6 - sdist layout")

print(
    "Valid package:",
    auditor.verify_sdist_layout("my_package")
)

print()
