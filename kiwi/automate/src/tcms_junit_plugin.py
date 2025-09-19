from tcms_junit_plugin import main
import ssl
import sys

ssl._create_default_https_context = ssl._create_unverified_context

main(sys.argv)  # type: ignore
