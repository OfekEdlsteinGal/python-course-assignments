import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

def download_uniprot_data(taxon_id="562", limit=50):
    """
    Downloads protein data from UniProt KB via its REST API for a given Taxon ID.
    Default taxon_id '562' is Escherichia coli (E. coli).
    """
    print(f"[*] Fetching top {limit} protein entries for Taxon ID: {taxon_id}...")
    
    # UniProt REST API endpoint for searching UniProtKB entries
    url = "https://rest.uniprot.org/uniprotkb/search"
    
    # Query parameters to filter by organism and request required fields
    params = {
        "query": f"organism_id:{taxon_id} AND reviewed:true",
        "format": "json",
        "size": limit,
        "fields": "accession,protein_name,gene_primary,length,sequence"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from UniProt. HTTP Status: {response.status_code}")
        
    data = response.json()
    return data['results']

def process_protein_data(results):
    """
    Processes the raw JSON results from UniProt into a clean DataFrame 
    and calculates amino acid composition metrics.
    """
    print("[*] Processing data and analyzing amino acid compositions...")
    
    protein_list = []
    
    for entry in results:
        accession = entry.get('primaryAccession', 'N/A')
        
        # Extracting nested protein name
        protein_desc = entry.get('proteinDescription', {})
        recommended_name = protein_desc.get('recommendedName', {})
        protein_name = recommended_name.get('fullName', {}).get('value', 'Unknown Protein')
        
        # Extracting gene name
        genes = entry.get('genes', [])
        gene_name = genes[0].get('geneName', {}).get('value', 'N/A') if genes else 'N/A'
        
        # Sequence metrics
        sequence_info = entry.get('sequence', {})
        length = sequence_info.get('length', 0)
        sequence_str = sequence_info.get('value', '')
        
        # Basic sequence analysis: Calculate frequency of Hydrophobic residues (A, V, I, L, M, F, Y, W)
        hydrophobic_residues = set("AVILMFYW")
        hydrophobic_count = sum(1 for aa in sequence_str if aa in hydrophobic_residues)
        hydrophobic_ratio = (hydrophobic_count / length) if length > 0 else 0
        
        protein_list.append({
            "Accession": accession,
            "Protein Name": protein_name,
            "Gene": gene_name,
            "Length (AA)": length,
            "Hydrophobic Ratio": round(hydrophobic_ratio, 3)
        })
        
    df = pd.DataFrame(protein_list)
    return df

def generate_insights(df):
    """
    Prints descriptive statistics and saves an analytical distribution plot.
    """
    print("\n=== DATA ANALYSIS INSIGHTS ===")
    print(f"Total Proteins Analyzed: {len(df)}")
    print(f"Average Protein Length: {df['Length (AA)'].mean():.1f} amino acids")
    print(f"Max Protein Length: {df['Length (AA)'].max()} AA (Gene: {df.loc[df['Length (AA)'].idxmax(), 'Gene']})")
    print(f"Average Hydrophobic Content: {df['Hydrophobic Ratio'].mean() * 100:.1f}%")
    
    # Save a distribution plot to disk
    plt.figure(figsize=(10, 5))
    plt.hist(df['Length (AA)'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('Protein Length Distribution in E. coli Sample')
    plt.xlabel('Length (Number of Amino Acids)')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    output_plot = 'protein_length_distribution.png'
    plt.savefig(output_plot)
    print(f"\n[✓] Distribution plot successfully generated and saved as '{output_plot}'")

if __name__ == "__main__":
    try:
        # 1. Download
        raw_data = download_uniprot_data(taxon_id="562", limit=50)
        
        # 2. Process
        processed_df = process_protein_data(raw_data)
        
        # Display sample of the processed DataFrame
        print("\n[*] Sample of Processed Data Table:")
        print(processed_df.head(10).to_string(index=False))
        
        # 3. Analyze & Plot
        generate_insights(processed_df)
        
    except Exception as e:
        print(f"[!] An error occurred: {e}")
