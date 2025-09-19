from tcms_junit_plugin import main
import ssl
import sys

# 検証目的のためだけに使用
ssl._create_default_https_context = ssl._create_unverified_context

main(sys.argv)  # type: ignore
