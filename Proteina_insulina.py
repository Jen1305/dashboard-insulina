# Archivo: dashboard_insulina.py
import streamlit as st
import py3Dmol
from Bio.SeqUtils import molecular_weight

# Prueba calcular el peso molecular
try:
    peso = molecular_weight("GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT", seq_type="protein")
    print(f"Peso molecular calculado: {peso} Da")
except Exception as e:
    print(f"Error: {e}")


# Título
st.title("Dashboard Interactivo: Proteína Insulina")

# Introducción
st.header("Introducción a la Insulina")
st.write("""
La insulina es una hormona proteica clave en la regulación de la glucosa en sangre, producida por las células beta del páncreas. 
Se compone de dos cadenas polipeptídicas (A y B) conectadas por puentes disulfuro.
""")

# Propiedades Bioquímicas
st.sidebar.header("Propiedades Bioquímicas")
peso = molecular_weight("GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT", seq_type="protein")
st.sidebar.write(f"*Peso Molecular Aproximado:* {peso:.2f} Da")
st.sidebar.write("*Punto isoeléctrico (pI):* ~5.4")
st.sidebar.write("*Cadenas A (21 aa) y B (30 aa)*")
# Secuencia de Aminoácidos
st.header("Secuencia de Aminoácidos")
secuencia = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
st.write(f"*Secuencia Completa:*\n{secuencia}")

# Estructura 3D Interactiva
st.header("Estructura 3D de la Insulina")
import streamlit.components.v1 as components
st.image("Insulina.png")

def render_molecule():
    pdb_data = """
    HEADER    INSULIN
    HETATM    1   N   ASN A   1      11.104  -8.618  -5.876  1.00  0.00           N
    HETATM    2   CA  ASN A   1      12.509  -8.763  -5.509  1.00  0.00           C
    ...
    """
    viewer = py3Dmol.view(width=800, height=400)
    viewer.addModel(pdb_data, "pdb")
    viewer.setStyle({"stick": {}})
    viewer.zoomTo()
    # Renderiza como HTML
    mol_html = viewer._make_html()
    components.html(mol_html, height=400, width=800)



# Rutas Metabólicas
st.header("Participación en Rutas Metabólicas")
st.write("La insulina regula procesos metabólicos clave como:")
st.markdown("""
- *Glucólisis*: Promueve la degradación de glucosa para generar energía.
- *Gluconeogénesis*: Inhibe la producción de glucosa en el hígado.
- *Síntesis de lípidos*: Estimula la formación de grasas a partir de glucosa.
""")

# Recursos Adicionales
st.header("Recursos Adicionales")
st.write("""
- [Entrada de Insulina en UniProt](https://www.uniprot.org/uniprot/P01308)
- [Estructura en el PDB](https://www.rcsb.org/structure/1ZNJ)
- [Simulaciones Metabólicas en KEGG](https://www.genome.jp/kegg/)
""")



