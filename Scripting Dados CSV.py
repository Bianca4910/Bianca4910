import csv

def main():
    """
    Main function to handle writing data to a CSV file.
    """
    file_name = 'pessoas.csv'
    
    # Define the header for the CSV file
    header = ['Nome', 'Idade', 'Cidade']
    
    # Data to be written to the CSV file
    # You can add more data here or get it from user input
    data = [
        ['Maria Silva', 30, 'São Paulo'],
        ['João Santos', 24, 'Rio de Janeiro'],
        ['Ana Pereira', 35, 'Belo Horizonte'],
        ['Pedro Costa', 29, 'Curitiba']
    ]

    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)
            
            # Write the header row
            csv_writer.writerow(header)
            
            # Write the data rows
            csv_writer.writerows(data)
        
        print(f"Dados gravados com sucesso no arquivo '{file_name}'")
    except IOError as e:
        print(f"Erro ao escrever no arquivo '{file_name}': {e}")

if __name__ == "__main__":
    main()