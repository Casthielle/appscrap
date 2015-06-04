# APPSCRAP
Python App para extraer saldo de la cuenta y las transacciones de los bancos. Es un fork de la jema Rubí bank_scrap hecha por diacode.

## Bancos compatibles


| Operaciones     |  BBVA  |  Mercantil  |
|-----------------|:------:|:-----------:|
| Saldo de Cuenta |    ✓   |      ✓      |
| Transacciones   |    ✓   |      ✓      |

Interesado en cualquier otro banco? Abre un nuevo problema y vamos a tratar de ayudar.


## Antecedentes y motivación
La mayoría de los bancos no ofrecen APIs públicas y la única manera de acceder a sus datos (saldo y transacciones) es a través de sus sitios web ... y la mayoría de los sitios web de los bancos son una pesadilla.

Somos desarrolladores y no queremos perder el tiempo haciendo cosas que son capaces de automatizar. Tener que hacer 20 clics en un sitio horrible, sólo para comprobar la cantidad de dinero que tenemos no es algo que nos gusta.


## Instalación

### de Git

Puedes comprobar la última versión en git de la siguiente manera:

    git clone https://github.com/Casthielle/appscrap.git


## Requisitos
Para realizar operaciones en el banco BBVA, es necesario agregar los detalles de su tarjeta de claves en el archivo '/src/appscrap.py' en la variable codecard. Por ejemplo:

Para conseguir su balance:

```python
codecard = {
			"A1":"106", "A2":"745", "A3":"078", "A4":"584", "A5":"396", "A6":"818", "A7":"537", "A8":"577", "A9":"184", "A10":"380",
			"B1":"555", "B2":"103", "B3":"740", "B4":"924", "B5":"131", "B6":"482", "B7":"028", "B8":"116", "B9":"040", "B10":"282",
			"C1":"434", "C2":"608", "C3":"027", "C4":"452", "C5":"194", "C6":"085", "C7":"633", "C8":"058", "C9":"427", "C10":"897",
			"D1":"126", "D2":"477", "D3":"292", "D4":"583", "D5":"052", "D6":"275", "D7":"951", "D8":"162", "D9":"162", "D10":"709",
			"E1":"917", "E2":"549", "E3":"889", "E4":"154", "E5":"316", "E6":"903", "E7":"874", "E8":"892", "E9":"136", "E10":"587",
			"F1":"997", "F2":"146", "F3":"524", "F4":"056", "F5":"402", "F6":"290", "F7":"848", "F8":"690", "F9":"133", "F10":"522",
			"G1":"149", "G2":"089", "G3":"109", "G4":"390", "G5":"546", "G6":"016", "G7":"669", "G8":"509", "G9":"812", "G10":"419",
			"H1":"974", "H2":"639", "H3":"670", "H4":"119", "H5":"646", "H6":"272", "H7":"565", "H8":"489", "H9":"207", "H10":"049"
		}
```

## Uso

### en el terminal
#### Saldo de la cuenta bancaria

###### BBVA | Mercantil

    $ python appscrap.py YOUR_BANK balance --user YOUR_BANK_USER --password YOUR_BANK_PASSWORD

or

	$ python appscrap.py YOUR_BANK balance -u YOUR_BANK_USER -p YOUR_BANK_PASSWORD

#### Últimas Transacciones
###### BBVA | Mercantil

    $ python appscrap.py YOUR_BANK transactions --user YOUR_BANK_USER --password YOUR_BANK_PASSWORD

or

	$ python appscrap.py YOUR_BANK transactions -u YOUR_BANK_USER -p YOUR_BANK_PASSWORD


Si usted no desea pasar su usuario y contraseña cada vez, puede definirlo en tu .bash_profile, añadiendo:

    export SUSER= TU_USUARIO_EN_EL_BANCO
    export SPASSWORD=TU_CLAVE_EN_EL_BANCO


## Para hacer tu contribución

1. Fork  ( https://github.com/Casthielle/appscrap/fork )
2. Cree su rama de la característica (`git checkout -b my-new-feature`)
3. Comenta y Compromete tus cambios (`git commit -am 'Add some feature'`)
4. Sube la rama (`git push origin my-new-feature`)
5. Crea un new Pull Request

## Gracias

Gracias a Javier Cuevas (javiercr) y Diacode para su joya bank_scrap.
Y gracias también a madrid.rb y codersvenezuela.com
