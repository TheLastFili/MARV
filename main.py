# Project MARV  - Maschinendialog für Abschluss-Relevante Voraussetzungen

ziel = 0
zahl_e = 0
zahl_g = 0
def_dorm = 0
def_dandm = 0
def_in_FG1 = 0
def_in_FG2 = 0
def_in_GK = 0
def_in_zwe_fs = 0
dkurs = 0
mkurs = 0
ekurs = 0
chkurs = 0
e_g_switch = ["", "E", "G"]
e_kurse = []
g_kurse = []
ausgleich = 0
ausgleich2 = 0

def kursart_bestimmen():
    global dkurs, mkurs, ekurs, chkurs
    print("Hast du in Deutsch einen E-Kurs oder einen G-Kurs?")
    kurs = int(input("1. E-Kurs\n2. G-Kurs\n"))
    dkurs = kurs
    print("Hast du in Mathematik einen E-Kurs oder einen G-Kurs?")
    kurs = int(input("1. E-Kurs\n2. G-Kurs\n"))
    mkurs = kurs
    print("Hast du in Englisch einen E-Kurs oder einen G-Kurs?")
    kurs = int(input("1. E-Kurs\n2. G-Kurs\n"))
    ekurs = kurs
    print("Hast du in Chemie einen E-Kurs oder einen G-Kurs?")
    kurs = int(input("1. E-Kurs\n2. G-Kurs\n"))
    chkurs = kurs
    if dkurs == 1:
        e_kurse.append("D")
    else:
        g_kurse.append("D")
    if mkurs == 1:
        e_kurse.append("M")
    else:
        g_kurse.append("M")
    if ekurs == 1:
        e_kurse.append("E")
    else:
        g_kurse.append("E")
    if chkurs == 1:
        e_kurse.append("Ch")
    else:
        g_kurse.append("Ch")



def zweite_fremdsprache_entfernen():
    global def_in_zwe_fs, def_in_FG2
    if def_in_FG2 > 1:
            def_in_zwe_fs = int(input("Ist eine dieser Fünfen in Französisch oder Latein?\n"
                                          "1. Ja\n"
                                          "2. Nein\n"))
            if def_in_zwe_fs == 1:
                def_in_FG2 -= 1

ziel_liste = [" ", "Hauptschulabschluss 9", "Hauptschulabschluss 10", "Realschulabschluss (FOR)",
              "Zulassung zur Oberstufe (FOR-Q)"]
ziel = int(input("Welchen Abschluss strebst du an? Bitte Zahl eingeben.\n"
                 "1. Hauptschulabschluss 9 (nur möglich, wenn du mindestens eine Klasse wiederholt hast)\n"
                 "2. Hauptschulabschluss 10\n"
                 "3. Realschulabschluss (FOR) \n"
                 "4. Zulassung zur Oberstufe (FOR-Q)\n"))
if ziel not in range(1, 5):
    print("Fehlerhafte Eingabe. Bitte erneut versuchen.")
    exit()

print(f"Du hast dich für {ziel_liste[ziel]} entschieden.")

if ziel > 2:
    kursart_bestimmen()
    print(
    f"\nKurse: Deutsch: {e_g_switch[dkurs]}, Mathematik: {e_g_switch[mkurs]}, Englisch: {e_g_switch[ekurs]}, Chemie: {e_g_switch[chkurs]}\n")

# HA9
if ziel == 1:
    def_dorm = int(input("Stehst du in Deutsch oder Mathe 5 oder schlechter?\n"
                         "1. Ja\n"
                         "2. Nein\n"))
    if def_dorm == 1:
        def_dandm = int(input("Stehst du in Deutsch und Mathe 5 oder schlechter?\n"
                              "1. Ja\n"
                              "2. Nein\n"))
        # if def_dandm == 1: PENDING HUEN
        #    if dkurs == 1 or mkurs == 1:
        #            print("Eine 5 in deinen E-Kursen kann umgerechnet werden, damit sie als 4 im G-Kurs zählt.")
        #            def_dandm = 2
        if def_dandm == 1 and dkurs == 2 and mkurs == 2:
            print("Für einen Hauptschulabschluss 9 müsstest du eine dieser Noten auf 4 verbessern oder in einem der"
                  "beiden Fächer im E-Kurs sein. Eventuell könnte eine Nachprüfung nötig sein.")
            exit()
    if def_dandm == 2 or 0:
        def_in_FG2 = int(input("Stehst du in einem oder mehr anderen Fächern 5 oder schlechter?\n"
                               "0. Nein\n"
                               "1. Ja, in einem.\n"
                               "2. Ja, in zwei.\n"
                               "3. Ja, in mehr.\n"))
        # if def_in_FG2 > 1:
        #     def_in_zwe_fs = int(input("Ist eine dieser Fünfen in Französisch oder Latein?\n"
        #                                   "1. Ja\n"
        #                                   "2. Nein\n"))
        #     if def_in_zwe_fs == 1:
        #         def_in_FG2 -= 1
        if def_in_FG2 > 1:
            def_in_zwe_fs = int(input("Ist eine dieser Fünfen in Französisch oder Latein?\n"
                                          "1. Ja\n"
                                          "2. Nein\n"))
            if def_in_zwe_fs == 1:
                def_in_FG2 -= 1
        if def_in_FG2 > 1 and def_in_zwe_fs == 2:
            print("Derzeit würdest du keinen Hauptschulabschluss 9 erreichen, weil du zu viele Fünfen hast.")
        if def_dandm == 2 or 0:
            if def_dorm == 1 and def_in_FG2 <= 1:
                print("Derzeit erfüllst du die Voraussetzungen für einen Hauptschulabschluss 9.")
            if def_dorm == 0 or 2:
                if def_in_FG2 <= 2:
                    print("Derzeit erfüllst du die Voraussetzungen für einen Hauptschulabschluss 9.")

#HA 10
if ziel == 2:
    def_in_FG1 = int(input("Stehst du in Deutsch, Mathe, AL oder NW 5 oder schlechter?\n"
                           "0. Nein\n"
                           "1. Ja, in einem dieser Fächer.\n"
                           "2. Ja, in zwei dieser Fächer.\n"
                           "3. Ja, in mehr als zwei dieser Fächer.\n"))
    if def_in_FG1 > 1:
        print ("Derzeit erfüllst du die Voraussetzungen für einen Hauptschulabschluss 10 nicht, weil du zu viele Fünfen hast. "
               "Für einen Hauptschulabschluss 10 darfst du nur in einem dieser Fächer 5 stehen. Eventuell könnte eine Nachprüfung nötig sein.")
        exit()
    def_in_FG2 = int(input("Stehst du in anderen Fächern 5 oder schlechter?\n"
                           "0. Nein\n"
                           "1. Ja, in einem dieser Fächer.\n"
                           "2. Ja, in zwei dieser Fächer.\n"
                           "3. Ja, in mehr als zwei dieser Fächer.\n"))
    if def_in_FG2 > 0:
        def_in_zwe_fs = int(input("Ist eine dieser Fünfen in Französisch oder Latein?\n"
                                          "1. Ja\n"
                                          "2. Nein\n"))
        if def_in_zwe_fs == 1:
            def_in_FG2 -= 1

    if def_in_FG1 + def_in_FG2 >= 2:
        print("Derzeit erfüllst du die Voraussetzungen für einen Hauptschulabschluss nicht, weil du zu viele Fünfen hast. "
               "Für einen Hauptschulabschluss müsstest darfst du maximal in zwei Fächern 5 stehen. Dies dürfen nicht gleichzeitig Deutsch,"
              "Mathe, AL oder NW sein. Eventuell könnte eine Nachprüfung nötig sein")
        exit()
    if def_in_FG1 + def_in_FG2 < 2:
        print ("Derzeit erfüllst du die Voraussetzungen für einen Hauptschulabschluss 10.")

#FOR
if ziel == 3:
    if len(e_kurse) < 2:
        print ("Derzeit erfüllst du die Voraussetzungen für einen FOR nicht, weil du zu wenige E-Kurse hast.")
    else:
        def_in_FG1 = int(input("Stehst du in einem deiner E-Kurse oder in WP schlechter als 4?\n"
                               "0. Nein\n"
                               "1. Ja, in einem Fach.\n"
                               "2. Ja, in zwei oder mehr Fächern.\n"))
        if def_in_FG1 == 2:
            print ("Derzeit erfüllst du die Voraussetzungen für einen FOR nicht, weil die Noten in deinen E-Kursen und/oder WP zu schlecht sind.")
        if def_in_FG1 == 1:
            ausgleich = int(input("Kannst du eine dieser Noten mit einem anderen E-Kurs (nicht Chemie) oder WP ausgleichen, so dass die beiden Noten"
                                  "im Schnitt 4 ergeben?\n"
                                  "0. Nein\n"
                                  "1. Ja\n"))
            def_in_FG1 -= ausgleich
            if ausgleich == 0:
                    print ("Derzeit erfüllst du die Voraussetzungen für einen FOR nicht, weil die Noten in deinen E-Kursen und/oder WP zu schlecht sind.")
        if def_in_FG1 == 0:
            def_in_GK = int(input("Stehst du in einem deiner G-Kurse schlechter als 3?\n"
                               "0. Nein\n"
                               "1. Ja, in einem Fach.\n"
                               "2. Ja, in zwei oder mehr Fächern.\n"))
            if def_in_GK > 0 and ausgleich == 1:
                print ("Derzeit erfüllst du die Voraussetzungen für einen FOR nicht, weil du nicht alle Noten ausgleichen kannst.")
            if def_in_GK >= 1 and ausgleich != 1:
                ausgleich = int(input("Kannst du eine dieser Noten mit einem anderen G-Kurs ausgleichen, so dass die beiden Noten"
                                  "im Schnitt 3 ergeben?\n"
                                  "0. Nein\n"
                                  "1. Ja\n"))
                def_in_GK -= ausgleich
            if def_in_GK == 0 and def_in_FG1 == 0:
                def_in_FG2 =  int(input("Stehst du mindestens in zwei anderen Fächern 3 und 4 oder besser in allen anderen?\n"
                               "0. Ja\n"
                               "1. Nein.\n"))
                if def_in_FG2 > 0:
                    ausgleich2 = int(input("Kannst du eine dieser Noten ausgleichen?\n"
                                  "0. Nein\n"
                                  "1. Ja\n"))
                    if ausgleich2 == 0:
                        print ("Derzeit erfüllst du die Voraussetzungen für einen FOR nicht, weil du nicht alle Noten ausgleichen kannst.")
                    if ausgleich2 == 1:
                        print ("Derzeit erfüllst du die Vorraussetzungen für einen FOR.")
                if def_in_FG2 == 0:
                        print ("Derzeit erfüllst du die Vorraussetzungen für einen FOR.")

#FORQ
if ziel == 4:
    if len(e_kurse) < 3:
        print ("Derzeit erfüllst du die Voraussetzungen für einen FOR nicht, weil du zu wenige E-Kurse hast.")
    else:
        def_in_FG1 = int(input("Stehst du in einem deiner E-Kurse oder in WP schlechter als 3?\n"
                               "0. Nein\n"
                               "1. Ja, in einem Fach.\n"
                               "2. Ja, in zwei oder mehr Fächern.\n"))
        if def_in_FG1 == 2:
            print ("Derzeit erfüllst du die Voraussetzungen für einen FOR-Q nicht, weil die Noten in deinen E-Kursen und/oder WP zu schlecht sind.")
        if def_in_FG1 == 1:
            ausgleich = int(input("Kannst du eine dieser Noten mit einem anderen E-Kurs (nicht Chemie) oder WP ausgleichen, so dass die beiden Noten"
                                  "im Schnitt 3 ergeben?\n"
                                  "0. Nein\n"
                                  "1. Ja\n"))
            def_in_FG1 -= ausgleich
            if ausgleich == 0:
                    print ("Derzeit erfüllst du die Voraussetzungen für einen FOR-Q nicht, weil die Noten in deinen E-Kursen und/oder WP zu schlecht sind.")
        if def_in_FG1 == 0:
            def_in_GK = int(input("Stehst du in einem deiner G-Kurse schlechter als 2?\n"
                               "0. Nein\n"
                               "1. Ja, in einem Fach.\n"
                               "2. Ja, in zwei oder mehr Fächern.\n"))
            if def_in_GK > 0 and ausgleich == 1:
                print ("Derzeit erfüllst du die Voraussetzungen für einen FOR-Q nicht, weil du nicht alle Noten ausgleichen kannst.")
            if def_in_GK >= 1 and ausgleich != 1:
                ausgleich = int(input("Kannst du eine dieser Noten mit einem anderen G-Kurs ausgleichen, so dass die beiden Noten"
                                  "im Schnitt 2 ergeben?\n"
                                  "0. Nein\n"
                                  "1. Ja\n"))
                def_in_GK -= ausgleich
            if def_in_GK == 0 and def_in_FG1 == 0:
                def_in_FG2 =  int(input("Stehst du 3 oder besser in allen anderen Fächern?\n"
                               "0. Ja\n"
                               "1. Nein.\n"))
                if def_in_FG2 > 0:
                    ausgleich2 = int(input("Kannst du zwei dieser Noten mit einer 2 ausgleichen?\n"
                                  "0. Nein\n"
                                  "1. Ja\n"))
                    if ausgleich2 == 0:
                        print ("Derzeit erfüllst du die Voraussetzungen für einen FOR-Q nicht, weil du nicht alle Noten ausgleichen kannst.")
                    if ausgleich2 == 1:
                        print ("Derzeit erfüllst du die Vorraussetzungen für einen FOR-Q.")
                if def_in_FG2 == 0:
                        print ("Derzeit erfüllst du die Vorraussetzungen für einen FOR-Q.")

print("Diese Aussagen sind nicht verbindlich. Die Nutzung dieses Programms ersetzt kein Beratungsgespräch mit den Klassenlehrern.")
