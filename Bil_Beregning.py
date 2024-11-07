# Laurent Zogaj

# Et program som beregner de årlige kostnadene ved å eie en bil

# Konstant for antall km/år (har ikke bil)
KM_PER_ÅR = 10000

# Konstanter nødvendig for programmets funksjon 
FORSIKRING = {'El-Bil': 5000, 'Bensinbil': 7500}
TRAFIKKFORSIKRINGSAVGIFT = (8.38 * 365)
DRIVSTOFF = {'El-Bil': 0.2 * 2.00, 'Bensinbil': 1.0} 
BOMAVGIFT = {'El-Bil': 0.1, 'Bensinbil': 0.3}

# Beregnign av årlig kostnader for elbil
drivstoffkostnad_elbil = DRIVSTOFF['El-Bil'] * KM_PER_ÅR
bomkostnad_elbil = BOMAVGIFT['El-Bil'] * KM_PER_ÅR
totalkostnad_elbil = FORSIKRING['El-Bil'] + TRAFIKKFORSIKRINGSAVGIFT + drivstoffkostnad_elbil + bomkostnad_elbil

# Beregning av årlige kostnader for bensinbil
drivstoffkostnad_bensinbil = DRIVSTOFF['Bensinbil'] * KM_PER_ÅR
bomkostnad_bensinbil = BOMAVGIFT['Bensinbil'] * KM_PER_ÅR
totalkostnad_bensinbil = FORSIKRING['Bensinbil'] + TRAFIKKFORSIKRINGSAVGIFT + drivstoffkostnad_bensinbil + bomkostnad_bensinbil

# Utskrift av resultatene
print("\nTotale årlige kostnader:")
print(f"El-Bil: {totalkostnad_elbil:.2f} kr")
print(f"Bensinbil: {totalkostnad_bensinbil:.2f} kr")
print(f"Kostnadsdifferanse: {totalkostnad_bensinbil - totalkostnad_elbil:.2f} kr")

