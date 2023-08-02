import pkg_resources

def is_package_installed(package_name):
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

# Replace 'textSummarizer' with the name of the package you want to check
package_name = 'textSummarizer'
is_installed = is_package_installed(package_name)

if is_installed:
    print(f"The package '{package_name}' is installed in the virtual environment.")
else:
    print(f"The package '{package_name}' is not installed in the virtual environment.")
