#!/bin/bash 
mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py
touch bioinformatics_project/results/cutsite_summary.txt
touch bioinformatics_project/data/random_sequence.fasta
echo "Bioinformatics Project Structure:" > bioinformatics_project/README.md
echo "The main directory is the Bioinformatics Project." >> bioinformatics_project/README.md
echo "Inside the main directory, it contains 3 subdirectories: data, scripts, and results." >> bioinformatics_project/README.md
echo "In the data subdirectory, it contains an empty file named random_sequence.fasta." >> bioinformatics_project/README.md
echo "In the results subdirectory, it contains an empty file named cutsite_summary.txt." >> bioinformatics_project/README.md
echo "Lastly, in the scripts subdirectory, it contains three empty Python files named generate_fasta.py, dna_operations.py, and find_cutsites.py." >> bioinformatics_project/README.md
echo "Project directory structure created successfully:"
echo "bioinformatics_project/"
echo "├── data/"
echo "├── results/"
echo "└── scripts/"
echo "    ├── generate_fasta.py"
echo "    ├── dna_operations.py"
echo "    └── find_cutsites.py"
echo "└── README.md"

