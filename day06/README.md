# UniProt Protein Sequence Downloader & Analyzer

A Python-based pipeline that programmatically interacts with the **UniProt KB REST API** to download, clean, and analyze high-quality protein sequence data for biological research.

## About the Data Source (UniProt)
The **Universal Protein Resource (UniProt)** is one of the world's most comprehensive and heavily cross-referenced scientific databases for protein sequence and functional annotation. 
Unlike raw nucleotide databases (like NCBI Nucleotide), UniProt focuses explicitly on the proteome level. It offers detailed information including:
* **Protein Sequences:** Complete amino acid chains.
* **Functional Annotations:** Biological roles, enzymatic pathways, and active sites.
* **Taxonomic Lineage:** Precise organism identification (using Taxon IDs).
* **Curated Metadata:** Differentiating between manually verified records (Swiss-Prot/Reviewed) and automatically annotated ones (TrEMBL/Unreviewed).

This project focuses on downloading data from **UniProtKB** using specific organism query filters to ensure reproducible and isolated analysis pipeline execution.

## Features
1. **Dynamic REST Data Fetching:** Utilizes modern UniProt API JSON endpoints to pull custom fields (Accession, Gene Name, Sequence, Length).
2. **Bioinformatics Processing:** Parses the nested JSON structure into an analytical table (Pandas DataFrame).
3. **Sequence Calculations:** Computes individual protein metrics, such as the *Hydrophobic Ratio* (the proportion of amino acids that are water-repelling, critical for structural folding).
4. **Data Visualization:** Generates a clean matplotlib distribution histogram of protein lengths within the organism's sample.

## Prerequisites & Installation
Ensure you have Python 3.9+ installed. Clone this repository and install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
