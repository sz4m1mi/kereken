import math


def beolvas_txt(file_nev):
  """Beolvassa a megadott txt fájlt sorról sorra egy tömbbe.

  Args:
    file_nev: A beolvasandó txt fájl neve.

  Returns:
    Egy tömb, amiben a txt fájl sorai szerepelnek.
  """
  sorok = []
  with open(file_nev, "r") as f:
    for sor in f:
      sorok.append(sor.strip())
  return sorok

cont = []

def feldolgoz_sorokat(sorok):
  """Feldolgozza a beolvasott sorokat.

  Args:
    sorok: A beolvasott sorokat tartalmazó tömb.

  Returns:
    Egy tömb, amiben a sorok elemei space karakterek mentén szét vannak választva.
  """

  feldolgozott_sorok = []
  poly_print = ""
  for sor in sorok:
      for koord in sor.split(' '):
          koordX = koord.split(',')[0]
          koordX = str((float(koordX)/3351)*100)[0:5]
          
          koordY = koord.split(',')[1]
          koordY = str((float(koordY)/3351)*100)[0:5]
          
          cont.append(koord.split(','))
          poly_print += (koordX + '% ' + koordY + '%, ')
    
    #feldolgozott_sorok.append(sor.split())
  return poly_print

# Példa a használatra
file_nev = "sec7p.txt"
sorok = beolvas_txt(file_nev)
feldolgozott_sorok = feldolgoz_sorokat(sorok)

# A feldolgozott_sorok tömb most már tartalmazza a txt fájl tartalmát,
# feldolgozva a space karaktereket is.

print(feldolgozott_sorok)