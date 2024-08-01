def generate_report(results, output_file):
    try:
        with open(output_file, 'w') as f:
            for result in results:
                f.write(f"{result}\n")
        print(f"Report successfully generated at {output_file}.")
    except IOError as e:
        print(f"Error writing report file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    results = ["Result 1", "Result 2"]
    generate_report(results, "report.txt")