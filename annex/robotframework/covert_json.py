"""
hello.robotをjsonに変換する例
"""
from robot.running import TestSuite


# Create suite based on data on the file system.
suite = TestSuite.from_file_system('tests/hello.robot')

# Get JSON data as a string.
data = suite.to_json(indent=2)
print(data)
# Save JSON data to a file with custom indentation.
# suite.to_json('data.rbt', indent=2)