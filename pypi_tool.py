import pkg_resources
import csv


def list_package_dependencies(package_name, output_file):
    """
    List all dependencies of a Python package and write them into a file.

    Args:
    package_name (str): The name of the package to list dependencies for.
    output_file (str): The path to the file where dependencies will be written.
    """
    # Get the distribution for the specified package
    distribution = pkg_resources.get_distribution(package_name)

    # Get a list of dependencies for the package
    dependencies = distribution.requires()

    # Open the output file and write the dependencies to it
    with open(output_file, 'w') as f:
        for dependency in dependencies:
            f.write(str(dependency) + '\n')

    print(f"Dependencies for {package_name} have been written to {output_file}")

def check_packages_and_write_to_csv(input_file, output_csv):
    """
    Check if packages from the input file are installed in the system and write to a CSV file.

    Args:
    input_file (str): The path to the input file containing package dependencies.
    output_csv (str): The path to the output CSV file.
    """
    packages = []

    # Read the input file
    with open(input_file, 'r') as f:
        for line in f:
            package_name, needed_version = line.strip().split('==')
            packages.append((package_name, needed_version))

    # Prepare the data for CSV
    csv_data = []
    for package_name, needed_version in packages:
        try:
            # Check if the package is installed and get the current version
            current_version = pkg_resources.get_distribution(package_name).version
        except pkg_resources.DistributionNotFound:
            current_version = "Not Installed"

        csv_data.append([package_name, needed_version, current_version])

    # Write data to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Package', 'Needed Version', 'Current Version'])  # Header
        writer.writerows(csv_data)

    print(f"Output written to {output_csv}")

# Example usage
input_file = 'dependencies.txt'  # The input file from the previous step
output_csv = 'package_versions.csv'  # The output CSV file
check_packages_and_write_to_csv(input_file, output_csv)
