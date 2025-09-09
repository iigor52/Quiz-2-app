import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Immunoglobulin Quiz Hub",
    page_icon="🧬",
    layout="wide"
)

# Main title
st.title("🧬 Immunoglobulin Quiz - Hub")

# Welcome message
st.markdown("""
## Dobrodošli na Immunoglobulin Quiz!

### 📋 Instrukcije:
- Otvorite sidebar (Pages) ili skenirajte QR kod za direktan pristup stanici
- Svaka stanica sadrži pitanja o imunoglobulinima
- Možete pristupiti stanicama bilo kojim redosledom

### 🎯 Dostupne stanice:
- Station 1
- Station 2  
- Station 3
- Station 4
- Station 5
- Station 6
- Station 7

---
### 💡 Kako pristupiti stanicama:

1. **Preko sidebar-a**: Otvorite sidebar (Pages) i kliknite na željenu stanicu
2. **Direktni linkovi**: Svaka stanica ima svoj direktni link
3. **QR kodovi**: Skenirajte QR kod za brz pristup

---
*Srećno sa kvizom!* 🎓
""")
