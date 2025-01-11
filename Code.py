class Input:
    def get_input_data(self):
        # Simulate retrieving input data (e.g., user input or from a file)
        return "Hello, World!"

class DataProcesso:
    def process_data(self, data):
        # Process the data (e.g., convert to uppercase)
        return data.upper()

class Output:
    def display_output(self, result):
        # Display the processed result
        print(result)

# Main program flow
if __name__ == "__main__":
    # Instantiate the classes
    input_obj = Input()
    processor_obj = DataProcesso()
    output_obj = Output()

    # Get input data
    data = input_obj.get_input_data()

    # Process the data
    processed_data = processor_obj.process_data(data)

    # Display the output
    output_obj.display_output(processed_data)
