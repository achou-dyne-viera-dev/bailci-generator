from datetime import date

def check_conformite(date_contrat, mention):
    if date_contrat >= date(2026, 10, 1) and "2 mois" in mention.lower():
        return "❌ NON-CONFORME: doit etre 6 semaines (42 jours)"
    return "✅ CONFORME decret 2026-596"

# Test jury INPHB
print(check_conformite(date(2026, 11, 1), "2 mois"))
print(check_conformite(date(2026, 11, 1), "6 semaines"))
