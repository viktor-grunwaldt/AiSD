# AiSD 

Pliki przydatne w nauce do egzaminu.\
Fork z ![https://github.com/JumiDeluxe/AiSD](https://github.com/JumiDeluxe/AiSD).

## co to jest?

To jest zestaw pytań do egzaminu z przedmiotu Algorytmy i Struktury Danych na kierunku Informayka (pierwszego stopnia) Uniwersystetu Wrocławskiego.

## jak korzystać

VS Code ma wbudowany renderer do markdown'a, sam którego używałem. Niektóre rozwiązania posiadają bloki równań, które markdown z VS Code obsługuje a (w tej samej formie) Github już nie, stąd polecam pobrać repo i korzystać lokalnie.

A i jeśli VS Code ci nie pasuje, to (chyba) jedyne czego github nie renderuje to te bloki formuł. Z tego co wiem, pod spodem je parsuje i renderuje KaTeX, więc można ten kod wrzucić na jakąś stronę co wygeneruje obrazek z matmą.

## mój wkład

Usunąłem notatki by zaoszczędzić miejsce/czas pobierania. Jeśli podchodzisz do egzaminu to je już masz, a jak nie to co tu robisz wgl?

(Prawie?) Każde zadanie otrzymało tag, mówiący do jakiej grupy zagadnień on należy, istnieje szansa że zadania nie zrozumiałem i wylądował w złej grupie lub jest na tyle dziwne że nie pasuje do żadnej z istniejących grup. Naklepałem też skrypcik który czyta tagi i generuje strukturę katalogów z odnośnikami do zadań z tym samym tagiem.

Dodałem własne rozwiązania, nie są one w żaden sposób zweryfikowane, więc proszę nie spodziewać się że będą poprawne :)

Niektóre (w szczególności te stare) pytania posiadały już odpowiedzi. Jak uznałem że było błędne, to starałem się dać poprawne rozwiązanie. Jednak większość rozwiązań wyglądała git. 

Sporo się napociłem konwertując stare rozwiązania na mój format - tj sporo z nich miało wstawione obrazki z imgura/codecogs np zawierające formuły LaTeX'owe lub screenshoty poleceń. Te mozolnie przepisywałem na tekst/kod w TeX'u embedowany w markdown który się renderuje w VS Code bez konieczności posiadania połączenia z internetem. Dzięki temu część rozwiązań nie jest uzależniona od tego, czy Imgur te zdjęcia będzie hostować czy może jednak nie. 

Jeśli nie ma rozwiązania, isnieje szansa, że nie chciało mi się go pisać po raz drugi, dlatego polecam użyć skryptu grupującego na podstawie tagów i sprawdzić czy już się zadanie nie powtórzyło.

Ze wgzędu na wprowadzone zmiany, uznałem że nie będę próbować robić MRki do Jumi.

## chcę pomóc

Po pierwsze, dziękuję. Chcę aby to repozytorium służył jako materiał do nauki dla przyszłych roczników, tak jak repozytorium z którego zforkowałem służyło mi.

Po drugie, ja już go nie potrzebuję. Nie mam żadnej zachęty aby wkładać dalej wysiłek w rozwój tego repo. Ale jeśli jesteś dobrą duszą, której coś z tego się przydało i zauważyłeś/aś coś co chesz poprawić albo dodać to z chęcią zmerge'uję pull request od Ciebie. Tak naprawdę to nawet to nie jest wymagane, możesz też oczywiście stworzyć forka i opublikować własną wersję.

Po trzecie, rzeczy, które potrzebują więcej pracy, szybko rzucają się w oczy: każdego roku fajnie by było dodać pytania, część pytań nie ma odpowiedzi, część pytań ma - nie mam pojęcia czy są dobre czy nie. Należałoby to zweryfikować, a błędnie odpowiedzi (może?) wytłumaczyć czemu są błęde (aby się uczyć na cudzych błędach) i ewentualnie dodać poprawne odpowiedzi.

ale hej, piszę to o 6-ej nad ranem pół roku później i nie wiem czy kiedykolwiek jakiś człowiek to przeczyta.
