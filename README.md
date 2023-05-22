# Fyysikkokilta Guild official parser
Parses line format copy-pasted from the Guild of Physics appendix
nominating the guild officials. This produces the `jaokset.json`, `toimarit.json` and `kuvat.json` files which are used by the [Wordpress theme](https://github.com/fyysikkokilta/fktheme2019).

## Usage
1. Copy the text from the appendix. Example can be found from 2/2023 meeting [appendixes](https://drive.google.com/drive/folders/1XXKefiVIU9XgC-XYjUtKwivlnfj2tLEl) of the Guild board with the name "Liite 2: Nimitettävät toimihenkilöt vuodelle 2023"  
The text looks something as follows
    ```
    TAPAHTUMAJAOS
    DJ
    Sun Mutsis

    N-VASTAAVA
    Sun Isäs
    Joku Muu

    IHMEJUTTUJAOS
    KILLANISUKKI
    Diktaattori Diktaattorinen

    OPINTOJAOS
    ÄNNÄ
    Ännä Ännäinen

    TUTORITYYPPI
    Tutori Tutorinen
    ```
    Save this as `volunteers.txt` next to the `toimarit.py` file.

1. Run the script with `python3 toimarit.py`
2. Copy created `jaokset.json`, `toimarit.json` and `kuvat.json` files to the Wordpress installation under `wp-content/uploads/toimarit/[YEAR]` folder.
3. Create `kuvat` folder in the `toimarit/[YEAR]` folder and copy the images of the officials there (the images should be named as the official's name in the `kuvat.json` file with spaces replaced by dashes `-`)

