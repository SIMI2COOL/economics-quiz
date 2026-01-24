import json
import random

# Generate questions based on the NEW text file: Ekonomia międzynarodowa (1).txt
# This file has fewer sections than the main branch

questions = []

def create_question(id_num, category, question, options, correct_idx, explanation, rationales):
    return {
        "id": id_num,
        "category": category,
        "question": question,
        "options": options,
        "correctAnswerIndex": correct_idx,
        "explanation": explanation,
        "rationales": rationales
    }

question_id = 1

# ===== EKONOMIA MIĘDZYNARODOWA - PODSTAWY =====
questions.append(create_question(
    question_id, "Ekonomia międzynarodowa - podstawy",
    "Co najlepiej definiuje ekonomię międzynarodową według materiału źródłowego?",
    ["Część ekonomii zajmująca się transakcjami między państwami w dziedzinie towarów i usług, przepływami finansowymi i ruchem czynników produkcji", "Dyscyplina zajmująca się wyłącznie handlem wewnętrznym", "Nauka o zarządzaniu przedsiębiorstwami krajowymi", "Teoria dotycząca tylko polityki monetarnej"],
    0,
    "Ekonomia międzynarodowa - część ekonomii zajmująca się transakcjami między państwami w dziedzinie towarów i usług, przepływami finansowymi i ruchem czynników produkcji, zajmuje się współzależnościami gospodarczymi pomiędzy państwami.",
    ["To dokładna definicja z materiału źródłowego.", "Ekonomia międzynarodowa zajmuje się transakcjami międzynarodowymi, nie wewnętrznymi.", "Ekonomia międzynarodowa zajmuje się transakcjami międzynarodowymi, nie tylko zarządzaniem krajowym.", "Ekonomia międzynarodowa jest znacznie szersza niż tylko polityka monetarna."]
))
question_id += 1

questions.append(create_question(
    question_id, "Ekonomia międzynarodowa - podstawy",
    "Która z poniższych była podstawą wyodrębnienia ekonomii międzynarodowej jako subdyscypliny?",
    ["Stałe wzrastające znaczenie handlu międzynarodowego i innych form współpracy międzynarodowej oraz różnice między stosunkami ekonomicznymi w granicach jednego państwa i w skali międzynarodowej", "Spadek znaczenia handlu międzynarodowego", "Brak różnic między gospodarką krajową a międzynarodową", "Wyłącznie rozwój technologii komputerowych"],
    0,
    "Podstawy wyodrębnienia subdyscypliny z ekonomii: Stałe wzrastające znaczenie handlu międzynarodowego i innych form współpracy międzynarodowej oraz Różnice występujące między stosunkami ekonomicznymi nawiązywanymi w granicach jednego państwa i skali międzynarodowej.",
    ["To dokładne przyczyny wyodrębnienia subdyscypliny z materiału źródłowego.", "Wzrost, nie spadek znaczenia handlu był przyczyną wyodrębnienia.", "Właśnie różnice między gospodarką krajową a międzynarodową były jedną z przyczyn wyodrębnienia.", "Technologie komputerowe to tylko jeden z wielu czynników, nie główna przyczyna wyodrębnienia."]
))
question_id += 1

# ===== GOSPODARKA ŚWIATOWA =====
questions.append(create_question(
    question_id, "Gospodarka światowa",
    "Co najlepiej definiuje gospodarkę światową według materiału źródłowego?",
    ["System trwałych powiązań ekonomicznych między krajami, obejmujących swym zasięgiem cały świat", "Suma wszystkich gospodarek krajowych bez powiązań", "System działający tylko w krajach rozwiniętych", "Tylko handel towarami"],
    0,
    "GOSPODARKA ŚWIATOWA to system trwałych powiązań ekonomicznych między krajami, obejmujących swym zasięgiem cały świat - historycznie ukształtowany i zmieniający się w czasie system powiązań produkcyjnych, technologicznych, handlowych, finansowych i instytucjonalnych.",
    ["To dokładna definicja z materiału źródłowego.", "Gospodarka światowa to system powiązań, nie suma izolowanych gospodarek.", "Gospodarka światowa obejmuje wszystkie kraje, nie tylko rozwinięte.", "Gospodarka światowa obejmuje wszystkie formy powiązań, nie tylko handel towarami."]
))
question_id += 1

questions.append(create_question(
    question_id, "Gospodarka światowa",
    "Która z poniższych jest cechą gospodarki światowej według materiału?",
    ["Kategoria ekonomiczna o charakterze dynamicznym – pewien system znajdujący się w stałym ruchu i rozwoju", "System statyczny, niezmienny w czasie", "Obejmuje tylko kraje rozwinięte", "Działa tylko w okresie pokoju"],
    0,
    "Gospodarka światowa to kategoria ekonomiczna o charakterze dynamicznym – pewien system znajdujący się w stałym ruchu i rozwoju oraz kategoria historyczna - mogła powstać dopiero na określonym poziomie rozwoju historycznego.",
    ["To dokładna cecha gospodarki światowej z materiału źródłowego.", "Gospodarka światowa jest dynamiczna, nie statyczna.", "Gospodarka światowa obejmuje wszystkie kraje, nie tylko rozwinięte.", "Gospodarka światowa funkcjonuje w różnych warunkach, nie tylko w pokoju."]
))
question_id += 1

questions.append(create_question(
    question_id, "Gospodarka światowa",
    "Która z poniższych jest drugą cechą gospodarki światowej według materiału?",
    ["Kategoria historyczna - mogła powstać dopiero na określonym poziomie rozwoju historycznego", "System działający od zawsze", "Obejmuje tylko handel", "Działa tylko w krajach demokratycznych"],
    0,
    "Gospodarka światowa to kategoria historyczna - mogła powstać dopiero na określonym poziomie rozwoju historycznego, gdy powstały i wykształciły się jej podstawowe elementy składowe.",
    ["To dokładna cecha gospodarki światowej z materiału źródłowego.", "Gospodarka światowa powstała na określonym poziomie rozwoju, nie działała od zawsze.", "Gospodarka światowa obejmuje wszystkie formy powiązań, nie tylko handel.", "Gospodarka światowa działa w różnych systemach politycznych, nie tylko demokratycznych."]
))
question_id += 1

# ===== STYMULATORY VS BARIERY GLOBALIZACJI =====
questions.append(create_question(
    question_id, "Globalizacja - stymulatory i bariery",
    "Które z poniższych są stymulatorami globalizacji wymienionymi w materiale?",
    ["Wszelkie ułatwienia transportowe i integracja międzynarodowa", "Niestabilność przepisów prawa", "Ksenofobia i egocentryzm", "Odmienności kulturowe i religijne"],
    0,
    "Stymulatory globalizacji: wszelkie ułatwienia transportowe (stymulują) oraz integracja międzynarodowa (z jednej strony stymulują).",
    ["To dokładna informacja z materiału źródłowego o stymulatorach globalizacji.", "Niestabilność przepisów prawa ma negatywny wpływ i spowalnia globalizację.", "Ksenofobia i egocentryzm są czynnikami socjopsychologicznymi spowalniającymi globalizację.", "Odmienności kulturowe i religijne spowalniają globalizację."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - stymulatory i bariery",
    "Które z poniższych są barierami globalizacji wymienionymi w materiale?",
    ["Liberalizacja handlu", "Niestabilność przepisów prawa oraz kultury i religie (odmienności, ksenofobia, egocentryzm)", "Ułatwienia transportowe", "Integracja międzynarodowa"],
    1,
    "Bariery globalizacji: Niestabilność przepisów prawa (negatywny wpływ) oraz Czynniki socjopsychologiczne - Kultury i religie (odmienności, ksenofobia, egocentryzm) - spowalniają.",
    ["Liberalizacja handlu to stymulator, nie bariera globalizacji.", "To dokładna informacja z materiału źródłowego o barierach globalizacji.", "Ułatwienia transportowe to stymulator, nie bariera globalizacji.", "Integracja międzynarodowa to stymulator, nie bariera globalizacji."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - stymulatory i bariery",
    "Który z poniższych jest przykładem bariery ekonomicznej globalizacji wymienionym w materiale?",
    ["Liberalizacja handlu", "Blokady np. polityka handlowa USA teraz", "Ułatwienia transportowe", "Integracja międzynarodowa"],
    1,
    "Bariery ekonomiczne globalizacji: blokady np. polityka handlowa USA teraz.",
    ["Liberalizacja handlu to stymulator, nie bariera globalizacji.", "To dokładny przykład bariery ekonomicznej z materiału źródłowego.", "Ułatwienia transportowe to stymulator, nie bariera globalizacji.", "Integracja międzynarodowa to stymulator, nie bariera globalizacji."]
))
question_id += 1

# ===== NEGATYWNE SKUTKI GLOBALIZACJI =====
questions.append(create_question(
    question_id, "Globalizacja - skutki negatywne",
    "Który z poniższych negatywnych skutków globalizacji jest wymieniony w materiale jako 'drenaż mózgów'?",
    ["Wzrost bezrobocia na skutek automatyzacji", "Pranie brudnych pieniędzy", "Drenaż mózgów, czyli przenoszenie się najlepszych specjalistów do światowych ośrodków badawczych", "Konsumpcjonizm"],
    2,
    "Negatywny skutek globalizacji: 'drenaż mózgów', czyli przenoszenie się najlepszych specjalistów do światowych ośrodków badawczych.",
    ["Wzrost bezrobocia to inny negatywny skutek, nie drenaż mózgów.", "Pranie brudnych pieniędzy to inny negatywny skutek, nie drenaż mózgów.", "To dokładna definicja drenażu mózgów z materiału źródłowego.", "Konsumpcjonizm to inny negatywny skutek, nie drenaż mózgów."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - skutki negatywne",
    "Który z poniższych negatywnych skutków globalizacji dotyczy zależności gospodarczej?",
    ["Brak różnorodności", "Zależność gospodarcza (kryzysy w jednym kraju przenoszą się na inne)", "Wzrost bezrobocia", "Konsumpcjonizm"],
    1,
    "Negatywny skutek globalizacji: Zależność gospodarcza (kryzysy w jednym kraju przenoszą się na inne).",
    ["Brak różnorodności to inny negatywny skutek, nie zależność gospodarcza.", "To dokładna definicja zależności gospodarczej z materiału źródłowego.", "Wzrost bezrobocia to inny negatywny skutek, nie zależność gospodarcza.", "Konsumpcjonizm to inny negatywny skutek, nie zależność gospodarcza."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - skutki negatywne",
    "Który z poniższych negatywnych skutków globalizacji dotyczy środowiska?",
    ["Drenaż mózgów", "Środowisko (zwiększony transport, degradacja środowiska poprzez budowanie fabryk, zmiany klimatyczne, narkomania, choroby cywilizacyjne)", "Konsumpcjonizm", "Globalny terroryzm"],
    1,
    "Negatywny skutek globalizacji: Środowisko (zwiększony transport, degradacja środowiska poprzez budowanie fabryk, zmiany klimatyczne, narkomania, choroby cywilizacyjne).",
    ["Drenaż mózgów to inny negatywny skutek, nie dotyczący środowiska.", "To dokładna informacja o negatywnych skutkach globalizacji dla środowiska z materiału źródłowego.", "Konsumpcjonizm to inny negatywny skutek, nie dotyczący środowiska.", "Globalny terroryzm to inny negatywny skutek, nie dotyczący środowiska."]
))
question_id += 1

# ===== DOBRE SKUTKI GLOBALIZACJI =====
questions.append(create_question(
    question_id, "Globalizacja - skutki pozytywne",
    "Który z poniższych pozytywnych skutków globalizacji jest wymieniony w materiale?",
    ["Większa dostępność do technologii", "Spadek konkurencji", "Centralizacja zarządzania", "Brak różnorodności towarów"],
    0,
    "Pozytywny skutek globalizacji: Większa dostępność do technologii.",
    ["To dokładna informacja z materiału źródłowego.", "Globalizacja przynosi wyższy poziom konkurencji, nie spadek.", "Globalizacja przynosi przejście od centralizacji do decentralizacji, nie centralizację.", "Globalizacja przynosi różnorodność towarów, nie jej brak."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - skutki pozytywne",
    "Który z poniższych pozytywnych skutków globalizacji dotyczy konkurencji?",
    ["Spadek konkurencji", "Wyższy poziom konkurencji oraz mechanizm konkurencji przyspiesza zmiany strukturalne oraz postęp techniczny", "Brak konkurencji", "Tylko lokalna konkurencja"],
    1,
    "Pozytywne skutki globalizacji: Wyższy poziom konkurencji oraz mechanizm konkurencji przyspiesza zmiany strukturalne oraz postęp techniczny.",
    ["Globalizacja przynosi wzrost, nie spadek konkurencji.", "To dokładna informacja o pozytywnych skutkach globalizacji dla konkurencji z materiału źródłowego.", "Globalizacja zwiększa konkurencję, nie eliminuje ją.", "Globalizacja przynosi konkurencję międzynarodową, nie tylko lokalną."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - skutki pozytywne",
    "Który z poniższych pozytywnych skutków globalizacji dotyczy zarządzania?",
    ["Centralizacja zarządzania", "Przejście od centralizacji do decentralizacji zarządzania", "Brak zmian w zarządzaniu", "Tylko centralizacja"],
    1,
    "Pozytywny skutek globalizacji: Przejście od centralizacji do decentralizacji zarządzania.",
    ["Globalizacja przynosi decentralizację, nie centralizację.", "To dokładna informacja o pozytywnym skutku globalizacji dla zarządzania z materiału źródłowego.", "Globalizacja przynosi zmiany w zarządzaniu.", "Globalizacja przynosi decentralizację, nie tylko centralizację."]
))
question_id += 1

# ===== GLOBALIZACJA - TRENDY =====
questions.append(create_question(
    question_id, "Globalizacja - trendy",
    "Jak zmieniało się średnie tempo wzrostu handlu według materiału?",
    ["Wzrosło z 2,6% (2000) do 5,1% (2020)", "Spadło z 5,1% (2000) do 2,6% (2020)", "Pozostało stabilne na poziomie 4%", "Wzrosło z 4,6% (2000) do 5,1% (2020)"],
    1,
    "Średnie tempo wzrostu handlu spadło z 5,1% (2000) --> 4,6% (2010) --> 2,6% (2020).",
    ["To odwrotna tendencja niż w materiale.", "To dokładna informacja z materiału źródłowego pokazująca spadek tempa wzrostu handlu.", "To nieprawidłowa informacja - tempo spadło, nie pozostało stabilne.", "To nieprawidłowa informacja - tempo spadło, nie wzrosło."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - trendy",
    "Która informacja o trendach globalizacji jest wymieniona w materiale?",
    ["Spadek ceł w USA", "Rekordowo wysokie cła w USA (najwyższe od 100 lat)", "Brak zmian w polityce handlowej USA", "Zniesienie ceł w USA"],
    1,
    "Trend globalizacji: Rekordowo wysokie cła w USA (najwyższe od 100 lat).",
    ["Cła w USA wzrosły, nie spadły.", "To dokładna informacja o trendach globalizacji z materiału źródłowego.", "Nastąpiły zmiany w polityce handlowej USA - wzrost ceł.", "Cła w USA wzrosły, nie zostały zniesione."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - trendy",
    "Jaki trend jest wymieniony w materiale jako przeciwny do globalizacji?",
    ["Wzrost globalizacji", "Trend ku fragmentacji gospodarczej zamiast globalizacji", "Brak zmian", "Przyspieszenie globalizacji"],
    1,
    "Trend globalizacji: Trend ku fragmentacji gospodarczej zamiast globalizacji.",
    ["To odwrotny trend niż w materiale.", "To dokładna informacja o trendzie przeciwnym do globalizacji z materiału źródłowego.", "Nastąpiły zmiany - trend ku fragmentacji.", "To odwrotny trend niż w materiale - fragmentacja, nie przyspieszenie globalizacji."]
))
question_id += 1

# ===== SLOWBALISATION =====
questions.append(create_question(
    question_id, "Globalizacja - slowbalisation",
    "Co oznacza termin 'slowbalisation'?",
    ["Przyspieszenie globalizacji", "Całkowite zatrzymanie globalizacji", "Opóźnienie globalizacji", "Regionalizacja bez globalizacji"],
    2,
    "SLOWBALISATION to opóźnienie globalizacji (na egzamin definicja).",
    ["To odwrotne znaczenie niż slowbalisation.", "To nieprawidłowa definicja slowbalisation.", "To dokładna definicja slowbalisation z materiału źródłowego.", "To nieprawidłowa definicja slowbalisation."]
))
question_id += 1

# ===== SEMIGLOBALIZACJA VS DEGLOBALIZACJA =====
questions.append(create_question(
    question_id, "Globalizacja - semiglobalizacja",
    "Co oznacza semiglobalizacja według materiału?",
    ["Całkowita globalizacja", "Półglobalizacja - świat częściowo zintegrowany, częściowo podzielony", "Brak globalizacji", "Tylko regionalizacja"],
    1,
    "Semiglobalizacja - półglobalizacja. Świat częściowo zintegrowany, częściowo podzielony. Globalizacja istnieje, ale ograniczają ją bariery polityczne, kulturowe i regulacyjne.",
    ["Semiglobalizacja to częściowa globalizacja, nie całkowita.", "To dokładna definicja semiglobalizacji z materiału źródłowego.", "Semiglobalizacja to częściowa globalizacja, nie jej brak.", "Semiglobalizacja to więcej niż tylko regionalizacja."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - semiglobalizacja",
    "Kto stwierdził, że 'globalizacja nigdy nie była pełna'?",
    ["V. Posner", "P. Ghemawat", "P. Samuelson", "Grubiel i Lloyd"],
    1,
    "P. Ghemawat stwierdził, że globalizacja nigdy nie była pełna.",
    ["V. Posner stworzył teorię luki technologicznej, nie wypowiadał się o semiglobalizacji.", "To dokładna informacja z materiału źródłowego.", "P. Samuelson stworzył teoremat wyrównania się cen czynników produkcji, nie wypowiadał się o semiglobalizacji.", "Grubiel i Lloyd stworzyli teorię handlu wewnątrzgałęziowego, nie wypowiadał się o semiglobalizacji."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - deglobalizacja",
    "Co oznacza deglobalizacja według materiału?",
    ["Przyspieszenie globalizacji", "Odwrót od globalizacji - proces odwracania i integracji gospodarczej i politycznej", "Brak zmian", "Tylko regionalizacja"],
    1,
    "Deglobalizacja - odwrót od globalizacji. Proces odwracania i integracji gospodarczej i politycznej. Spadek znaczenia handlu i inwestycji międzynarodowych. Rosnąca rola protekcjonizmu, regionalizacji, autarkii.",
    ["To odwrotne znaczenie niż deglobalizacja.", "To dokładna definicja deglobalizacji z materiału źródłowego.", "Deglobalizacja to proces zmian, nie brak zmian.", "Deglobalizacja to więcej niż tylko regionalizacja - to odwrót od globalizacji."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalizacja - deglobalizacja",
    "Które z poniższych wydarzeń są wymienione w materiale jako przyspieszające deglobalizację?",
    ["Tylko kryzys 2008", "Kryzys 2008, covid-19, wojna w Ukrainie, napięcia USA-Chiny", "Tylko covid-19 i wojna w Ukrainie", "Tylko napięcia USA-Chiny"],
    1,
    "Wydarzenia przyspieszające deglobalizację: kryzys 2008, covid-19, wojna w Ukrainie, napięcia USA-Chiny.",
    ["To tylko jedno z wymienionych wydarzeń, nie wszystkie.", "To kompletna lista wydarzeń przyspieszających deglobalizację z materiału źródłowego.", "To niekompletna lista wydarzeń.", "To tylko jedno z wymienionych wydarzeń, nie wszystkie."]
))
question_id += 1

# ===== GLOBALNE RYZYKA I WYZWANIA =====
questions.append(create_question(
    question_id, "Globalne ryzyka i wyzwania",
    "Które z poniższych są globalnymi ryzykami i wyzwaniami wymienionymi w materiale?",
    ["Tylko rosnące napięcia handlowe", "Rosnące napięcia handlowe i protekcjonizm, niepewność polityczna i konflikty regionalne, zmiany klimatu i katastrofy naturalne, kryzys zadłużenia", "Tylko zmiany klimatu", "Tylko kryzys zadłużenia"],
    1,
    "Globalne ryzyka i wyzwania: Rosnące napięcia handlowe i protekcjonizm, Niepewność polityczna i konflikty regionalne, Zmiany klimatu i katastrofy naturalne --> coraz większe koszty, Kryzys zadłużenia - ponad połowa krajów o niskich dochodach w stanie zagrożenia.",
    ["To tylko jedno z wymienionych ryzyk, nie wszystkie.", "To kompletna lista globalnych ryzyk i wyzwań z materiału źródłowego.", "To tylko jedno z wymienionych ryzyk, nie wszystkie.", "To tylko jedno z wymienionych ryzyk, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Globalne ryzyka i wyzwania",
    "Jaka informacja o kryzysie zadłużenia jest wymieniona w materiale?",
    ["Tylko kilka krajów w stanie zagrożenia", "Ponad połowa krajów o niskich dochodach w stanie zagrożenia", "Brak kryzysu zadłużenia", "Tylko kraje rozwinięte w stanie zagrożenia"],
    1,
    "Kryzys zadłużenia - ponad połowa krajów o niskich dochodach w stanie zagrożenia.",
    ["To nieprawidłowa informacja - ponad połowa krajów o niskich dochodach jest zagrożona.", "To dokładna informacja o kryzysie zadłużenia z materiału źródłowego.", "Kryzys zadłużenia istnieje i dotyczy wielu krajów.", "Kryzys zadłużenia dotyczy krajów o niskich dochodach, nie tylko rozwiniętych."]
))
question_id += 1

# ===== PRZEDMIOTY GOSPODARKI ŚWIATOWEJ =====
questions.append(create_question(
    question_id, "Przedmioty gospodarki światowej",
    "Ile krajów musi obejmować działalność przedsiębiorstwa, aby było uznane za korporację transnarodową?",
    ["Przynajmniej 1 kraj", "Przynajmniej 2 kraje", "Przynajmniej 3 kraje", "Przynajmniej 5 krajów"],
    1,
    "Przedsiębiorstwo międzynarodowe (korporacje transnarodowe): Przedsiębiorstwo, które spełnia warunek prowadzenia działalności biznesowej opartej na własności aktywów i ich kontroli przynajmniej w 2 krajach.",
    ["To za mało - potrzeba przynajmniej 2 krajów.", "To dokładna informacja z materiału źródłowego.", "To więcej niż wymagane minimum.", "To więcej niż wymagane minimum."]
))
question_id += 1

questions.append(create_question(
    question_id, "Przedmioty gospodarki światowej",
    "Kiedy przedsiębiorstwa krajowe stają się podmiotami gospodarki światowej?",
    ["Zawsze, gdy działają w kraju", "Gdy w związku ze swoją działalnością gospodarczą nawiązują znaczące pod względem charakteru, znaczenia, zakresu międzynarodowe stosunki gospodarcze z innymi podmiotami", "Nigdy", "Tylko gdy eksportują"],
    1,
    "Przedsiębiorstwa krajowe stają się podmiotami gospodarki światowej, gdy w związku ze swoją działalnością gospodarczą nawiązują znaczące pod względem charakteru, znaczenia, zakresu międzynarodowe stosunki gospodarcze z innymi podmiotami.",
    ["Przedsiębiorstwa krajowe muszą nawiązać międzynarodowe stosunki, nie tylko działać w kraju.", "To dokładna informacja z materiału źródłowego.", "Przedsiębiorstwa krajowe mogą stać się podmiotami gospodarki światowej poprzez międzynarodowe stosunki.", "Przedsiębiorstwa mogą nawiązywać różne formy międzynarodowych stosunków, nie tylko eksport."]
))
question_id += 1

questions.append(create_question(
    question_id, "Przedmioty gospodarki światowej",
    "Które z poniższych są formami relacji/powiązań z zagranicą wymienionymi w materiale?",
    ["Tylko handlowe", "Handlowe, produkcyjne, technologiczne, finansowo-kredytowe i kapitałowe", "Tylko finansowe", "Tylko handlowe i produkcyjne"],
    1,
    "Konieczność relacji/powiązań z zagranicą: handlowe, produkcyjne, technologiczne, finansowo-kredytowe i kapitałowe.",
    ["To tylko jedna z form relacji, nie wszystkie.", "To kompletna lista form relacji/powiązań z zagranicą z materiału źródłowego.", "To tylko jedna z form relacji, nie wszystkie.", "To niekompletna lista form relacji."]
))
question_id += 1

questions.append(create_question(
    question_id, "Przedmioty gospodarki światowej",
    "Jak ugrupowania integracyjne są włączone do gospodarki światowej?",
    ["Bezpośrednio", "Pośrednio - np. poprzez działalność gospodarczą przedsiębiorstw oraz poprzez międzynarodowe stosunki ekonomiczne nawiązywane przez te podmioty", "Nie są włączone", "Tylko poprzez handel"],
    1,
    "Ugrupowania integracyjne są włączone do gospodarki światowej pośrednio - np. poprzez działalność gospodarczą przedsiębiorstw oraz poprzez międzynarodowe stosunki ekonomiczne nawiązywane przez te podmioty.",
    ["Ugrupowania integracyjne są włączone pośrednio, nie bezpośrednio.", "To dokładna informacja z materiału źródłowego.", "Ugrupowania integracyjne są włączone do gospodarki światowej pośrednio.", "Ugrupowania integracyjne są włączone poprzez różne formy, nie tylko handel."]
))
question_id += 1

# ===== FORMY UGRUPOWAŃ INTEGRACYJNYCH =====
questions.append(create_question(
    question_id, "Formy ugrupowań integracyjnych",
    "Która z poniższych jest pierwszą formą ekonomicznej integracji?",
    ["Unia celna", "Strefa wolnego handlu", "Wspólny rynek", "Unia gospodarcza"],
    1,
    "Formy ekonomicznej integracji w kolejności: Strefa wolnego handlu, Unia celna, Wspólny rynek, Unia gospodarcza, Unia polityczna.",
    ["Unia celna to druga forma, nie pierwsza.", "To dokładna informacja z materiału źródłowego - pierwsza forma to strefa wolnego handlu.", "Wspólny rynek to trzecia forma, nie pierwsza.", "Unia gospodarcza to czwarta forma, nie pierwsza."]
))
question_id += 1

questions.append(create_question(
    question_id, "Formy ugrupowań integracyjnych",
    "Która z poniższych jest ostatnią (najwyższą) formą ekonomicznej integracji?",
    ["Wspólny rynek", "Unia gospodarcza", "Unia polityczna", "Strefa wolnego handlu"],
    2,
    "Formy ekonomicznej integracji w kolejności: Strefa wolnego handlu, Unia celna, Wspólny rynek, Unia gospodarcza, Unia polityczna.",
    ["Wspólny rynek to trzecia forma, nie ostatnia.", "Unia gospodarcza to czwarta forma, nie ostatnia.", "To dokładna informacja z materiału źródłowego - ostatnia forma to unia polityczna.", "Strefa wolnego handlu to pierwsza forma, nie ostatnia."]
))
question_id += 1

questions.append(create_question(
    question_id, "Formy ugrupowań integracyjnych",
    "Ile krajów musi obejmować ugrupowanie integracyjne według materiału?",
    ["Tylko jeden kraj", "Dwa lub więcej krajów", "Tylko dwa kraje", "Przynajmniej pięć krajów"],
    1,
    "Międzynarodowe (regionalne) ugrupowania integracyjne to wyróżniający się na tle otoczenia względnie jednolity, nowy organizm gospodarczy, obejmujący dwa lub więcej krajów.",
    ["Ugrupowanie integracyjne musi obejmować co najmniej dwa kraje, nie jeden.", "To dokładna informacja z materiału źródłowego.", "Ugrupowanie może obejmować więcej niż dwa kraje.", "Ugrupowanie może obejmować mniej niż pięć krajów - minimum to dwa."]
))
question_id += 1

# ===== MIĘDZYNARODOWY FUNDUSZ WALUTOWY =====
questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (MFW)",
    "Jaka jest misja MFW według materiału?",
    ["Wspieranie rozwoju gospodarczego", "Zapewnienie stabilności międzynarodowego systemu walutowego", "Promowanie wolnego handlu", "Walka z ubóstwem"],
    1,
    "Misja MFW: zapewnienie stabilności międzynarodowego systemu walutowego; realizowana jest w ramach dwóch podstawowych obszarów działalności: nadzorczej i kredytowej.",
    ["Wspieranie rozwoju gospodarczego to zadanie Banku Światowego, nie MFW.", "To dokładna misja MFW z materiału źródłowego.", "Promowanie wolnego handlu to zadanie WTO, nie MFW.", "Walka z ubóstwem to zadanie Banku Światowego, nie MFW."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (MFW)",
    "W ramach jakich obszarów działalności realizowana jest misja MFW?",
    ["Tylko nadzorczej", "Nadzorczej i kredytowej", "Tylko kredytowej", "Tylko regulacyjnej"],
    1,
    "Misja MFW realizowana jest w ramach dwóch podstawowych obszarów działalności: nadzorczej i kredytowej.",
    ["To tylko jeden z obszarów, nie wszystkie.", "To dokładna informacja z materiału źródłowego o obszarach działalności MFW.", "To tylko jeden z obszarów, nie wszystkie.", "To nieprawidłowy obszar działalności MFW."]
))
question_id += 1

# ===== BANK ŚWIATOWY =====
questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (Bank Światowy)",
    "Jaka jest pełna nazwa Banku Światowego?",
    ["Międzynarodowy Bank Rozwoju", "Międzynarodowy Bank Odbudowy i Rozwoju", "Bank Międzynarodowy", "Światowy Bank Finansowy"],
    1,
    "Bank Światowy to Międzynarodowy Bank Odbudowy i Rozwoju.",
    ["To nieprawidłowa nazwa Banku Światowego.", "To dokładna pełna nazwa Banku Światowego z materiału źródłowego.", "To nieprawidłowa nazwa Banku Światowego.", "To nieprawidłowa nazwa Banku Światowego."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (Bank Światowy)",
    "Jaka jest wizja Banku Światowego od 2023 roku?",
    ["Wspieranie rozwoju gospodarczego krajów członkowskich", "Stworzenie świata wolnego od ubóstwa na nadającej się do życia planecie", "Promowanie wolnego handlu", "Stabilizacja międzynarodowego systemu walutowego"],
    1,
    "Wizja Banku Światowego od 2023 roku: stworzenie świata wolnego od ubóstwa na nadającej się do życia planecie.",
    ["To podstawowe zadanie Banku, nie wizja od 2023 roku.", "To dokładna wizja Banku Światowego od 2023 roku z materiału źródłowego.", "To cel WTO, nie wizja Banku Światowego.", "To misja MFW, nie wizja Banku Światowego."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (Bank Światowy)",
    "Jaka jest misja Banku Światowego?",
    ["Tylko wspieranie rozwoju gospodarczego", "Położenie kresu skrajnemu ubóstwu i zwiększenie dobrobytu na nadającej się do życia planecie", "Tylko walka z ubóstwem", "Tylko stabilizacja walutowa"],
    1,
    "Misja Banku Światowego: położenie kresu skrajnemu ubóstwu i zwiększenie dobrobytu na nadającej się do życia planecie.",
    ["To tylko część misji Banku Światowego.", "To dokładna misja Banku Światowego z materiału źródłowego.", "To tylko część misji Banku Światowego.", "To misja MFW, nie Banku Światowego."]
))
question_id += 1

# ===== GRUPA BANKU ŚWIATOWEGO =====
questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (Grupa Banku Światowego)",
    "Która instytucja wchodzi w skład Grupy Banku Światowego i ma skrót MBOiR?",
    ["Międzynarodowe Stowarzyszenie Rozwoju (MSR)", "Międzynarodowy Bank Odbudowy i Rozwoju (MBOiR)", "Międzynarodowa Korporacja Finansowa (MKF)", "Wielostronna Agencja Gwarancji Inwestycyjnych (MIGA)"],
    1,
    "Grupa Banku Światowego: Międzynarodowy Bank Odbudowy i Rozwoju – w skrócie MBOiR.",
    ["MSR to Międzynarodowe Stowarzyszenie Rozwoju, nie MBOiR.", "To dokładna informacja z materiału źródłowego.", "MKF to Międzynarodowa Korporacja Finansowa, nie MBOiR.", "MIGA to Wielostronna Agencja Gwarancji Inwestycyjnych, nie MBOiR."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (Grupa Banku Światowego)",
    "Która instytucja wchodzi w skład Grupy Banku Światowego i ma skrót MSR?",
    ["Międzynarodowy Bank Odbudowy i Rozwoju (MBOiR)", "Międzynarodowe Stowarzyszenie Rozwoju (MSR)", "Międzynarodowa Korporacja Finansowa (MKF)", "Wielostronna Agencja Gwarancji Inwestycyjnych (MIGA)"],
    1,
    "Grupa Banku Światowego: Międzynarodowe Stowarzyszenie Rozwoju – w skrócie MSR.",
    ["MBOiR to Międzynarodowy Bank Odbudowy i Rozwoju, nie MSR.", "To dokładna informacja z materiału źródłowego.", "MKF to Międzynarodowa Korporacja Finansowa, nie MSR.", "MIGA to Wielostronna Agencja Gwarancji Inwestycyjnych, nie MSR."]
))
question_id += 1

# ===== ŚWIATOWA ORGANIZACJA HANDLU (WTO) =====
questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (WTO)",
    "Gdzie mieści się siedziba Światowej Organizacji Handlu?",
    ["W Waszyngtonie", "W Genewie", "W Paryżu", "W Brukseli"],
    1,
    "Siedziba WTO mieści się w Genewie.",
    ["Waszyngton to siedziba MFW, nie WTO.", "To dokładna lokalizacja siedziby WTO z materiału źródłowego.", "Paryż to siedziba OECD, nie WTO.", "Bruksela to siedziba UE, nie WTO."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (WTO)",
    "Kto może zostać członkiem WTO według materiału?",
    ["Tylko państwa", "Każde państwo lub 'odrębne terytorium celne posiadające pełną autonomię w prowadzeniu swych zewnętrznych stosunków handlowych'", "Tylko kraje rozwinięte", "Tylko kraje członkowskie ONZ"],
    1,
    "Członkiem WTO może zostać każde państwo lub 'odrębne terytorium celne posiadające pełną autonomię w prowadzeniu swych zewnętrznych stosunków handlowych'.",
    ["WTO może mieć członków innych niż tylko państwa - także terytoria celne.", "To dokładna informacja o członkostwie w WTO z materiału źródłowego.", "WTO nie ogranicza członkostwa tylko do krajów rozwiniętych.", "WTO nie wymaga członkostwa w ONZ."]
))
question_id += 1

# ===== ORGANIZACJA WSPÓŁPRACY GOSPODARCZEJ I ROZWOJU (OECD) =====
questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (OECD)",
    "Który z poniższych jest celem OECD wymienionym w materiale?",
    ["Tylko osiąganie wzrostu gospodarczego", "Osiąganie możliwie najwyższego poziomu wzrostu gospodarczego, zatrudnienia i standardu życia w krajach członkowskich, przy jednoczesnym utrzymaniu stabilizacji finansowej", "Tylko promowanie handlu", "Tylko walka z ubóstwem"],
    1,
    "Cele OECD: Osiąganie możliwie najwyższego poziomu wzrostu gospodarczego, zatrudnienia i standardu życia w krajach członkowskich, przy jednoczesnym utrzymaniu stabilizacji finansowej i tym samym wniesienie wkładu do rozwoju gospodarki światowej.",
    ["To tylko część celów OECD, nie wszystkie.", "To dokładna informacja o celach OECD z materiału źródłowego.", "Promowanie handlu to tylko jeden z celów OECD.", "Walka z ubóstwem to zadanie Banku Światowego, nie główny cel OECD."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe organizacje gospodarcze (OECD)",
    "Który z poniższych jest drugim celem OECD wymienionym w materiale?",
    ["Tylko współdziałanie na rzecz rozwoju krajów członkowskich", "Współdziałanie na rzecz równomiernego rozwoju gospodarczego krajów członkowskich i krajów rozwijających się", "Tylko promowanie handlu", "Tylko stabilizacja walutowa"],
    1,
    "Cele OECD: Współdziałanie na rzecz równomiernego rozwoju gospodarczego krajów członkowskich i krajów rozwijających się.",
    ["To tylko część celu OECD, nie pełny cel.", "To dokładna informacja o drugim celu OECD z materiału źródłowego.", "Promowanie handlu to inny cel OECD.", "Stabilizacja walutowa to misja MFW, nie cel OECD."]
))
question_id += 1

# ===== ROLA HANDLU ZAGRANICZNEGO W GOSPODARCE =====
questions.append(create_question(
    question_id, "Handel zagraniczny i międzynarodowy",
    "Co to jest handel zagraniczny według materiału źródłowego?",
    ["Wymiana pomiędzy różnymi gospodarkami narodowymi analizowana z 'lotu ptaka'", "Wymiana rozpatrywana z punktu widzenia jednego kraju i jego otoczenia zagranicznego", "Tylko eksport towarów", "Tylko import towarów"],
    1,
    "HANDEL ZAGRANICZNY to wymiana rozpatrywana z punktu widzenia jednego kraju i jego otoczenia zagranicznego.",
    ["To definicja handlu międzynarodowego, nie zagranicznego.", "To dokładna definicja handlu zagranicznego z materiału źródłowego.", "Handel zagraniczny obejmuje zarówno eksport, jak i import.", "Handel zagraniczny obejmuje zarówno eksport, jak i import."]
))
question_id += 1

questions.append(create_question(
    question_id, "Handel zagraniczny i międzynarodowy",
    "Co to jest handel międzynarodowy według materiału źródłowego?",
    ["Wymiana rozpatrywana z punktu widzenia jednego kraju", "Wymiana pomiędzy różnymi gospodarkami narodowymi, kiedy strumienie handlu analizowane są z przysłowiowego 'lotu ptaka' między parą krajów", "Tylko handel w ramach ugrupowania integracyjnego", "Tylko handel między kontynentami"],
    1,
    "HANDEL MIĘDZYNARODOWY to wymiana pomiędzy różnymi gospodarkami narodowymi, kiedy strumienie handlu analizowane są z przysłowiowego 'lotu ptaka' między parą krajów, na poziomie pewnej grupy gospodarek np. w ramach ugrupowania integracyjnego, kontynentu lub pomiędzy kontynentami.",
    ["To definicja handlu zagranicznego, nie międzynarodowego.", "To dokładna definicja handlu międzynarodowego z materiału źródłowego.", "Handel międzynarodowy może być w ramach ugrupowania, ale to tylko jeden z przykładów.", "Handel międzynarodowy może być między kontynentami, ale to tylko jeden z przykładów."]
))
question_id += 1

questions.append(create_question(
    question_id, "Handel zagraniczny i międzynarodowy",
    "Co to jest eksport według materiału?",
    ["Zakup i przywóz do danego kraju dóbr i usług wytworzonych poza jego granicami", "Sprzedaż i wywóz za granicę dóbr i usług wytworzonych w danym kraju", "Tylko handel towarami", "Tylko handel usługami"],
    1,
    "Eksport to sprzedaż i wywóz za granicę dóbr i usług wytworzonych w danym kraju.",
    ["To definicja importu, nie eksportu.", "To dokładna definicja eksportu z materiału źródłowego.", "Eksport obejmuje zarówno towary, jak i usługi.", "Eksport obejmuje zarówno towary, jak i usługi."]
))
question_id += 1

questions.append(create_question(
    question_id, "Przyczyny rozwoju importu",
    "Która z poniższych jest przyczyną trwałego braku określonych towarów wymienioną w materiale?",
    ["Wahania koniunktury", "Warunki naturalne (zasoby) i warunki klimatyczne", "Nieurodzaje", "Strajki"],
    1,
    "Przyczyny trwałego braku określonych towarów: warunki naturalne (zasoby) i warunki klimatyczne. Trwały brak określonych towarów nie może być nigdy usunięty - występowanie importu niezbędnego.",
    ["Wahania koniunktury to przyczyna przejściowego braku, nie trwałego.", "To dokładna informacja o przyczynach trwałego braku towarów z materiału źródłowego.", "Nieurodzaje to przyczyna przejściowego braku, nie trwałego.", "Strajki to przyczyna przejściowego braku, nie trwałego."]
))
question_id += 1

# ===== TEORIA WYMIANY MIĘDZYNARODOWEJ =====
questions.append(create_question(
    question_id, "Teoria wymiany międzynarodowej",
    "Która z poniższych jest przyczyną importu wymienioną w materiale?",
    ["Tylko brak określonych towarów", "Brak określonych towarów, usług, surowców, przyczyny kosztowe, technologiczne, kooperacja zaopatrzeniowa, przyczyny jakościowe, obowiązywanie określonych umów handlowych", "Tylko przyczyny kosztowe", "Tylko przyczyny technologiczne"],
    1,
    "Dlaczego kraje importują: Brak określonych towarów, usług, surowców, Przyczyny kosztowe, Przyczyny technologiczne, Kooperacja zaopatrzeniowa, Przyczyny jakościowe, Obowiązywanie określonych umów handlowych.",
    ["To tylko jedna z przyczyn, nie wszystkie.", "To kompletna lista przyczyn importu z materiału źródłowego.", "To tylko jedna z przyczyn, nie wszystkie.", "To tylko jedna z przyczyn, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teoria wymiany międzynarodowej",
    "Która z poniższych jest przyczyną eksportu wymienioną w materiale?",
    ["Tylko zbyt duże nadwyżki produkcyjne", "Zbyt duże nadwyżki produkcyjne, chęć uzyskania dewiz, kreacja nowych miejsc pracy, kooperacja zaopatrzeniowa, obowiązywanie określonych umów handlowych", "Tylko chęć uzyskania dewiz", "Tylko kreacja nowych miejsc pracy"],
    1,
    "Dlaczego kraje eksportują: Zbyt duże nadwyżki produkcyjne, Chęć uzyskania dewiz, Kreacja nowych miejsc pracy, Kooperacja zaopatrzeniowa, Obowiązywanie określonych umów handlowych.",
    ["To tylko jedna z przyczyn, nie wszystkie.", "To kompletna lista przyczyn eksportu z materiału źródłowego.", "To tylko jedna z przyczyn, nie wszystkie.", "To tylko jedna z przyczyn, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - przedklasyczne",
    "Które starożytne cywilizacje są wymienione w materiale w kontekście teorii przedklasycznej?",
    ["Tylko Starożytny Egipt", "Starożytny Egipt, Fenicja, Grecja, Rzym", "Tylko Grecja i Rzym", "Tylko Fenicja"],
    1,
    "Teoria przedklasyczna: Starożytny Egipt, Fenicja, Grecja, Rzym.",
    ["To niekompletna lista z materiału.", "To dokładna lista cywilizacji z materiału źródłowego.", "To niekompletna lista z materiału.", "To niekompletna lista z materiału."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - przedklasyczne",
    "Kto i kiedy najpełniej ujął zasady dogmatu słusznej ceny?",
    ["Arystoteles w IV w. p.n.e.", "Św. Tomasz z Akwinu w XIII w.", "Adam Smith w XVIII w.", "David Ricardo w XIX w."],
    1,
    "Zasady dogmatu słusznej ceny w XIII w. najpełniej ujął św. Tomasz z Akwinu.",
    ["Arystoteles nie formułował dogmatu słusznej ceny w takim kształcie.", "To dokładna informacja z materiału źródłowego.", "Adam Smith żył później i nie formułował dogmatu słusznej ceny.", "David Ricardo żył później i nie formułował dogmatu słusznej ceny."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - klasyczne",
    "Ile krajów i ile produktów zakłada teoria kosztów absolutnych?",
    ["Jeden kraj, jeden produkt", "Dwa kraje, jeden produkt", "Dwa kraje, dwa produkty", "Trzy kraje, dwa produkty"],
    2,
    "Teoria kosztów absolutnych: Dwa kraje, dwa produkty!",
    ["To nieprawidłowe założenia teorii kosztów absolutnych.", "To nieprawidłowe założenia teorii kosztów absolutnych.", "To dokładna informacja z materiału źródłowego.", "To nieprawidłowe założenia teorii kosztów absolutnych."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - klasyczne",
    "Ile czynników produkcji zakłada teoria kosztów absolutnych?",
    ["Jeden czynnik - praca", "Dwa czynniki - kapitał i praca", "Trzy czynniki", "Cztery czynniki"],
    0,
    "Teoria kosztów absolutnych: Tylko jeden czynnik produkcji – praca.",
    ["To dokładna informacja z materiału źródłowego.", "Teoria kosztów absolutnych zakłada tylko jeden czynnik - pracę, nie dwa.", "Teoria kosztów absolutnych zakłada tylko jeden czynnik - pracę.", "Teoria kosztów absolutnych zakłada tylko jeden czynnik - pracę."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - neoklasyczne (H-O)",
    "Ile czynników produkcji zakłada teoria Heckschera-Ohlina (H-O)?",
    ["Jeden czynnik - praca", "Dwa czynniki - kapitał i praca", "Trzy czynniki - kapitał, praca, ziemia", "Cztery czynniki - kapitał, praca, ziemia, technologia"],
    1,
    "Teoria obfitości zasobów - teoria Heckschera-Ohlina (H-O): dwa kraje, dwa towary, dwa jednolite czynniki produkcji: kapitał i praca.",
    ["To założenie teorii klasycznej, nie H-O.", "To dokładna informacja z materiału źródłowego.", "To więcej czynników niż zakłada teoria H-O.", "To więcej czynników niż zakłada teoria H-O."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - neoklasyczne",
    "Kto stworzył teoremat wyrównania się cen czynników produkcji?",
    ["V. Posner", "P. Samuelson", "P. Ghemawat", "Grubiel i Lloyd"],
    1,
    "Teoremat wyrównania się cen czynników produkcji został stworzony przez P. Samuelsona.",
    ["V. Posner stworzył teorię luki technologicznej, nie ten teoremat.", "To dokładna informacja z materiału źródłowego.", "P. Ghemawat wypowiadał się o semiglobalizacji, nie stworzył tego teorematu.", "Grubiel i Lloyd stworzyli teorię handlu wewnątrzgałęziowego, nie ten teoremat."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - paradoks Leontiefa",
    "Co odkrył W. Leontief w towarach eksportowych przez USA?",
    ["Więcej kapitału niż pracy", "Więcej pracy a mniej kapitału, niż w towarach stanowiących substytuty dóbr importowanych przez ten kraj", "Równą ilość kapitału i pracy", "Tylko kapitał"],
    1,
    "W towarach eksportowych przez USA W. Leontief odkrył więcej pracy a mniej kapitału, niż w towarach stanowiących substytuty dóbr importowanych przez ten kraj.",
    ["To odwrotne odkrycie niż w materiale.", "To dokładna informacja o paradoksie Leontiefa z materiału źródłowego.", "To nieprawidłowa informacja - Leontief odkrył więcej pracy, nie równą ilość.", "To nieprawidłowa informacja - Leontief odkrył więcej pracy, nie tylko kapitał."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - neotechnologiczne",
    "Kto stworzył teorię luki technologicznej?",
    ["P. Samuelson", "V. Posner", "P. Ghemawat", "Grubiel i Lloyd"],
    1,
    "M.V. Posner jako pierwszy uchylił założenie mówiące o dysponowaniu przez wszystkie kraje jednakową technologią, tworząc koncepcję OPÓŹNIENIA NAŚLADOWCZEGO – TEORIĘ LUKI TECHNOLOGICZNEJ.",
    ["P. Samuelson stworzył teoremat wyrównania się cen, nie teorię luki technologicznej.", "To dokładna informacja z materiału źródłowego.", "P. Ghemawat wypowiadał się o semiglobalizacji, nie stworzył teorii luki technologicznej.", "Grubiel i Lloyd stworzyli teorię handlu wewnątrzgałęziowego, nie teorię luki technologicznej."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - neotechnologiczne",
    "Ile faz przechodzi produkt-innowacja według teorii cyklu życia produktu?",
    ["Dwie fazy", "Trzy fazy", "Cztery fazy", "Pięć faz"],
    1,
    "Teoria cyklu życia produktu: handel międzynarodowy jest pochodną przechodzenia danego produktu-innowacji kolejno przez trzy fazy: Fazę innowacyjną - wprowadzenia, Fazę dojrzewania – wzrostu, Fazę standaryzacji.",
    ["To nieprawidłowa liczba faz w teorii cyklu życia produktu.", "To dokładna informacja z materiału źródłowego - trzy fazy.", "To nieprawidłowa liczba faz w teorii cyklu życia produktu.", "To nieprawidłowa liczba faz w teorii cyklu życia produktu."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - korzyści skali",
    "Które korzyści skali polegają na spadku kosztów przeciętnych nie w wyniku zwiększenia skali produkcji w danym przedsiębiorstwie, ale wielkości produkcji danej branży?",
    ["Wewnętrzne korzyści skali", "Zewnętrzne korzyści skali", "Korzyści techniczne", "Korzyści organizacyjne"],
    1,
    "Zewnętrzne korzyści skali polegają na spadku kosztów przeciętnych nie w wyniku zwiększenia skali produkcji w danym przedsiębiorstwie, ale wielkości produkcji danej branży.",
    ["Wewnętrzne korzyści skali mają miejsce, gdy wzrost rozmiarów produkcji wewnątrz przedsiębiorstwa pozwala na obniżenie kosztów przeciętnych.", "To dokładna definicja zewnętrznych korzyści skali z materiału źródłowego.", "To nieprawidłowa kategoria korzyści skali.", "To nieprawidłowa kategoria korzyści skali."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - wewnątrzgałęziowy",
    "Kto stworzył teorię handlu wewnątrzgałęziowego?",
    ["V. Posner", "P. Samuelson", "Grubiel i Lloyd", "P. Ghemawat"],
    2,
    "Teoria wewnątrzgałęziowego handlu została stworzona przez Grubiel i Lloyd.",
    ["V. Posner stworzył teorię luki technologicznej, nie handlu wewnątrzgałęziowego.", "P. Samuelson stworzył teoremat wyrównania się cen, nie teorię handlu wewnątrzgałęziowego.", "To dokładna informacja z materiału źródłowego.", "P. Ghemawat wypowiadał się o semiglobalizacji, nie stworzył teorii handlu wewnątrzgałęziowego."]
))
question_id += 1

questions.append(create_question(
    question_id, "Teorie handlu - wewnątrzgałęziowy",
    "Co to jest handel wewnątrzgałęziowy według materiału źródłowego?",
    ["Wymiana produktów pochodzących z różnych gałęzi przemysłu", "Wymiana produktów pochodzących z jednej gałęzi przemysłu", "Tylko handel surowcami", "Tylko handel usługami"],
    1,
    "Handel wewnątrzgałęziowy to wymiana produktów pochodzących z jednej gałęzi przemysłu. Gałąź to dobra będące bliskimi substytutami w produkcji lub konsumpcji.",
    ["To definicja handlu międzygałęziowego, nie wewnątrzgałęziowego.", "To dokładna definicja handlu wewnątrzgałęziowego z materiału źródłowego.", "Handel wewnątrzgałęziowy może dotyczyć różnych produktów, nie tylko surowców.", "Handel wewnątrzgałęziowy może dotyczyć różnych produktów, nie tylko usług."]
))
question_id += 1

questions.append(create_question(
    question_id, "Nowoczesne teorie handlu - GVC",
    "Co oznacza niski poziom w Globalnych Łańcuchach Wartości (GVC)?",
    ["R&D, projektowanie, branding, marketing", "Montaż, dostawy surowców", "Tylko montaż", "Tylko dostawy surowców"],
    1,
    "Globalne łańcuchy wartości (GVC): niski poziom -> montaż, dostawy surowców; wysoki poziom -> R&D, projektowanie, branding, marketing.",
    ["To wysoki poziom w GVC, nie niski.", "To dokładna informacja z materiału źródłowego o niskim poziomie w GVC.", "To niekompletna definicja niskiego poziomu.", "To niekompletna definicja niskiego poziomu."]
))
question_id += 1

questions.append(create_question(
    question_id, "Nowoczesne teorie handlu - servicification",
    "Który z poniższych jest przykładem servicification of trade wymienionym w materiale?",
    ["Handel ropą naftową", "Smartfon: oprócz urządzenia ogromna część wartości to system operacyjny, aplikacje, usługi w chmurze", "Handel surowcami mineralnymi", "Handel produktami rolnymi"],
    1,
    "Przykład servicification: smartfon - oprócz samego urządzenia ogromna część wartości to system operacyjny, aplikacje, usługi w chmurze.",
    ["Handel ropą to tradycyjny handel towarami, nie przykład servicification.", "To dokładny przykład z materiału źródłowego pokazujący servicification of trade.", "Handel surowcami to tradycyjny handel towarami, nie przykład servicification.", "Handel produktami rolnymi to tradycyjny handel towarami, nie przykład servicification."]
))
question_id += 1

questions.append(create_question(
    question_id, "Nowoczesne teorie handlu - Porter's Diamond",
    "Ile czynników tworzy 'diament' w teorii przewag konkurencyjnych Portera?",
    ["Dwa czynniki", "Trzy czynniki", "Cztery czynniki", "Pięć czynników"],
    2,
    "Teoria przewag konkurencyjnych Portera (Diamond Model): przewaga kraju wynika z czterech powiązanych czynników: czynniki produkcji, warunki popytu, branże pokrewne i wspierające, strategia, struktura i rywalizacja firm.",
    ["To za mało czynników w teorii Portera.", "To za mało czynników w teorii Portera.", "To dokładna informacja z materiału źródłowego - cztery czynniki tworzące 'diament'.", "To za dużo czynników w teorii Portera."]
))
question_id += 1

# ===== KURS WALUTOWY =====
questions.append(create_question(
    question_id, "Kurs walutowy",
    "Co to jest kurs walutowy według materiału?",
    ["Tylko wartość waluty danego kraju wyrażona w walucie obcej", "Wartość waluty danego kraju wyrażona w walucie obcej; cena waluty obcej wyrażona w walucie krajowej; stosunek, w jakim dokonuje się wymiany określonej ilości danej waluty na jednostkę innej waluty", "Tylko cena waluty obcej", "Tylko stosunek wymiany"],
    1,
    "KURS WALUTOWY to wartość waluty danego kraju wyrażona w walucie obcej; cena waluty obcej wyrażona w walucie krajowej; stosunek, w jakim dokonuje się wymiany określonej ilości danej waluty na jednostkę innej waluty.",
    ["To tylko jedna z definicji, nie wszystkie.", "To kompletna definicja kursu walutowego z materiału źródłowego.", "To tylko jedna z definicji, nie wszystkie.", "To tylko jedna z definicji, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Kurs walutowy",
    "Które z poniższych są funkcjami kursu walutowego wymienionymi w materiale?",
    ["Tylko cenotwórcza", "Cenotwórcza, informacyjna, alokacyjna", "Tylko informacyjna i alokacyjna", "Tylko cenotwórcza i informacyjna"],
    1,
    "Funkcje kursu walutowego: Cenotwórcza, Informacja, Alokacyjna.",
    ["To tylko jedna z funkcji, nie wszystkie.", "To kompletna lista funkcji kursu walutowego z materiału źródłowego.", "To niekompletna lista funkcji.", "To niekompletna lista funkcji."]
))
question_id += 1

questions.append(create_question(
    question_id, "Kurs walutowy - aprecjacja",
    "Który przykład aprecjacji jest podany w materiale?",
    ["Zmiana kursu z 1 euro = 4,30 PLN na 1 euro = 4,60 PLN", "Zmiana kursu z 1 euro = 4,60 PLN na 1 euro = 4,30 PLN", "Zmiana kursu z 1 euro = 4,50 PLN na 1 euro = 4,70 PLN", "Zmiana kursu z 1 euro = 4,70 PLN na 1 euro = 4,50 PLN"],
    1,
    "Aprecjacja: wzrost wartości waluty krajowej w stosunku do waluty obcej. Przykład: Zmiana kursu z 1 euro = 4,60 PLN na 1 euro = 4,30 PLN.",
    ["To przykład deprecjacji, nie aprecjacji.", "To dokładny przykład aprecjacji z materiału źródłowego.", "To przykład deprecjacji, nie aprecjacji.", "To przykład aprecjacji, ale nie ten z materiału."]
))
question_id += 1

questions.append(create_question(
    question_id, "Kurs walutowy - deprecjacja",
    "Który przykład deprecjacji jest podany w materiale?",
    ["Zmiana kursu z 1 euro = 4,30 PLN na 1 euro = 4,60 PLN", "Zmiana kursu z 1 euro = 4,60 PLN na 1 euro = 4,30 PLN", "Zmiana kursu z 1 euro = 4,50 PLN na 1 euro = 4,70 PLN", "Zmiana kursu z 1 euro = 4,70 PLN na 1 euro = 4,50 PLN"],
    2,
    "Deprecjacja: obniżenie siły nabywczej pieniądza krajowego. Przykład: Zmiana kursu z 1 euro = 4,50 PLN na 1 euro = 4,70 PLN.",
    ["To przykład aprecjacji, nie deprecjacji.", "To przykład aprecjacji, nie deprecjacji.", "To dokładny przykład deprecjacji z materiału źródłowego.", "To przykład deprecjacji, ale nie ten z materiału."]
))
question_id += 1

# ===== RYNEK WALUTOWY =====
questions.append(create_question(
    question_id, "Rynek walutowy",
    "Która z poniższych jest cechą rynku walutowego wymienioną w materiale?",
    ["Jest umiejscowiony geograficznie w jednym miejscu", "Nie jest umiejscowiony geograficznie", "Funkcjonuje tylko w godzinach pracy", "Należy do najdroższych rynków"],
    1,
    "Cechy rynku walutowego: Nie jest umiejscowiony geograficznie, Funkcjonuje całą dobę, Należy do najtańszych, ze względu na niskie koszty transakcji i do najlepiej zintegrowanych w skali międzynarodowej.",
    ["Rynek walutowy nie jest umiejscowiony geograficznie, nie w jednym miejscu.", "To dokładna informacja z materiału źródłowego.", "Rynek walutowy funkcjonuje całą dobę, nie tylko w godzinach pracy.", "Rynek walutowy należy do najtańszych, nie najdroższych rynków."]
))
question_id += 1

questions.append(create_question(
    question_id, "Rynek walutowy",
    "Który rodzaj rynku walutowego dokonuje transakcji z dostawą walut natychmiast lub najdalej w ciągu 2 dni roboczych?",
    ["Rynek terminowy", "Rynek bieżący", "Rynek forward", "Rynek futures"],
    1,
    "Rodzaje rynku walutowego: Bieżący --> dokonywanie transakcji z dostawą walut natychmiast lub najdalej w ciągu 2 dni roboczych.",
    ["Rynek terminowy to inny rodzaj - kurs ustalony teraz, dostawa w przyszłości.", "To dokładna informacja z materiału źródłowego o rynku bieżącym.", "Rynek forward to rodzaj rynku terminowego, nie bieżącego.", "Rynek futures to rodzaj rynku terminowego, nie bieżącego."]
))
question_id += 1

# ===== MIĘDZYNARODOWY SYSTEM WALUTOWY =====
questions.append(create_question(
    question_id, "Międzynarodowy system walutowy",
    "Jaki system walutowy funkcjonuje obecnie według materiału?",
    ["System jednodywizowy", "System dwudywizowy", "System wielodywizowy", "System bez walut"],
    2,
    "Dziś system wielodywizowy! Charakterystyczna cecha - występowanie wielu walut, które odgrywają rolę pieniądza międzynarodowego, obok dolara i euro, są to waluty wielu krajów, w których znajdują się międzynarodowe centra finansowe (UK, Szwajcaria, Japonia).",
    ["To nieprawidłowy system - obecnie jest wielodywizowy.", "To nieprawidłowy system - obecnie jest wielodywizowy.", "To dokładna informacja z materiału źródłowego - system wielodywizowy.", "To nieprawidłowy system - istnieją waluty."]
))
question_id += 1

# ===== BILANS PŁATNICZY =====
questions.append(create_question(
    question_id, "Bilans płatniczy",
    "Co to jest bilans płatniczy według materiału źródłowego?",
    ["Tylko bilans handlowy (eksport minus import)", "Zestawienie wszystkich transakcji dokonywanych między rezydentami a resztą świata w danym okresie", "Tylko przepływy kapitałowe", "Tylko rezerwy walutowe"],
    1,
    "Bilans płatniczy to zestawienie wszystkich transakcji dokonywanych między rezydentami a resztą świata w danym okresie.",
    ["Bilans handlowy to tylko część bilansu płatniczego.", "To dokładna definicja bilansu płatniczego z materiału źródłowego.", "Przepływy kapitałowe to tylko część bilansu płatniczego.", "Rezerwy walutowe to tylko jeden z elementów bilansu płatniczego."]
))
question_id += 1

# ===== MIĘDZYNARODOWE PRZEPŁYWY KAPITAŁU =====
questions.append(create_question(
    question_id, "Międzynarodowe przepływy kapitału",
    "Co to są międzynarodowe przepływy kapitału według materiału?",
    ["Tylko inwestycje bezpośrednie", "Wszelkie ruchy kapitału, które swoje odzwierciedlenie znajdują w bilansie obrotów gospodarczych z zagranicą i są ujmowane w rachunku bilansu płatniczego danego kraju", "Tylko inwestycje portfelowe", "Tylko kredyty"],
    1,
    "Międzynarodowe przepływy kapitału to wszelkie ruchy kapitału, które swoje odzwierciedlenie znajdują w bilansie obrotów gospodarczych z zagranicą i są ujmowane w rachunku bilansu płatniczego danego kraju.",
    ["To tylko jedna z form przepływów kapitału, nie wszystkie.", "To dokładna definicja międzynarodowych przepływów kapitału z materiału źródłowego.", "To tylko jedna z form przepływów kapitału, nie wszystkie.", "To tylko jedna z form przepływów kapitału, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe przepływy kapitału - BIZ",
    "Według OECD i MFW, jaki minimalny udział inwestora w spółce jest wymagany, aby inwestycja mogła być uznana za bezpośrednią?",
    ["5%", "10%", "15%", "20%"],
    1,
    "Według OECD i MFW inwestycja może być uznana za bezpośrednią, jeśli w jej wyniku udział inwestora w spółce jest nie mniejszy niż 10% (zakup 10% pakietu akcji lub udziałów).",
    ["To za niski próg dla uznania inwestycji za bezpośrednią.", "To dokładna informacja z materiału źródłowego.", "To za wysoki próg dla uznania inwestycji za bezpośrednią.", "To za wysoki próg dla uznania inwestycji za bezpośrednią."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe przepływy kapitału - BIZ",
    "Co oznacza GREENFIELD INVESTMENT?",
    ["Przejęcie istniejącego przedsiębiorstwa za granicą", "Utworzenie nowego przedsiębiorstwa za granicą", "Kupno akcji bez kontroli", "Krótkoterminowa lokata kapitałowa"],
    1,
    "Formy BIZ: Utworzenie nowego przedsiębiorstwa za granicą - GREENFIELD INVESTMENT oraz Aktywizacja - przejęcie istniejącego przedsiębiorstwa za granicą - BROWNFIELD INVESTMENT.",
    ["To definicja BROWNFIELD INVESTMENT, nie GREENFIELD.", "To dokładna definicja GREENFIELD INVESTMENT z materiału źródłowego.", "To inwestycje portfelowe, nie BIZ.", "To nie forma BIZ."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe przepływy kapitału - BIZ",
    "Które z poniższych są motywami BIZ wymienionymi w materiale?",
    ["Tylko zaopatrzeniowe i rynkowe", "Zaopatrzeniowe, rynkowe, kosztowe, polityczne, strategiczne", "Tylko kosztowe i polityczne", "Tylko strategiczne"],
    1,
    "Motywy BIZ: Zaopatrzeniowe, Rynkowe, Kosztowe, Polityczne, Strategiczne.",
    ["To niekompletna lista motywów BIZ.", "To kompletna lista motywów BIZ z materiału źródłowego.", "To niekompletna lista motywów BIZ.", "To niekompletna lista motywów BIZ."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe przepływy kapitału - portfelowe",
    "Co to są portfelowe inwestycje zagraniczne według materiału?",
    ["Inwestycje z kontrolą nad przedsiębiorstwem", "Zakup papierów wartościowych emitowanych przez państwo, instytucje i przedsiębiorstwa mające siedzibę za granicą w celu osiągnięcia zysku bez angażowania się w kontrolę działalności emitenta", "Tylko zakup akcji", "Tylko zakup obligacji"],
    1,
    "Portfelowe inwestycje zagraniczne to zakup papierów wartościowych emitowanych przez państwo, instytucje i przedsiębiorstwa mające siedzibę za granicą w celu osiągnięcia zysku bez angażowania się w kontrolę działalności emitenta.",
    ["To inwestycje bezpośrednie, nie portfelowe - portfelowe nie dają kontroli.", "To dokładna definicja portfelowych inwestycji zagranicznych z materiału źródłowego.", "To tylko jedna z form inwestycji portfelowych, nie wszystkie.", "To tylko jedna z form inwestycji portfelowych, nie wszystkie."]
))
question_id += 1

# ===== MIĘDZYNARODOWE PRZEPŁYWY SIŁY ROBOCZEJ =====
questions.append(create_question(
    question_id, "Międzynarodowe przepływy siły roboczej",
    "Jaki jest minimalny okres zmiany miejsca pobytu i zamieszkania, aby była to migracja według materiału?",
    ["Nie krótszy niż 6 miesięcy", "Nie krótszy niż jeden rok", "Nie krótszy niż 2 lata", "Nie krótszy niż 3 lata"],
    1,
    "Przepływ siły roboczej (migracja) to zmiana miejsca pobytu i zamieszkania na okres nie krótszy niż jeden rok.",
    ["To za krótki okres dla uznania migracji.", "To dokładna informacja z materiału źródłowego.", "To dłuższy okres niż wymagany minimum.", "To dłuższy okres niż wymagany minimum."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe przepływy siły roboczej",
    "Które z poniższych sprzyjają procesom migracyjnym według materiału?",
    ["Tylko postęp w transporcie", "Postęp w transporcie, nowoczesne systemy mediów, środki przekazu, łączności i technologie informacyjne", "Tylko technologie informacyjne", "Tylko środki przekazu"],
    1,
    "Procesom migracyjnym sprzyjają: Postęp w transporcie, Nowoczesne systemy mediów, Środki przekazu, Łączności i technologie informacyjne.",
    ["To tylko jeden z czynników, nie wszystkie.", "To kompletna lista czynników sprzyjających migracji z materiału źródłowego.", "To tylko jeden z czynników, nie wszystkie.", "To tylko jeden z czynników, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe przepływy siły roboczej - migracje zarobkowe",
    "Co to są migracje zarobkowe według materiału?",
    ["Tylko migracje trwałe", "Przemieszczanie się osoby lub grupy osób przez granicę międzynarodową lub w obrębie państwa motywowane wyłącznie lub przede wszystkim możliwościami ekonomicznymi", "Tylko migracje czasowe", "Tylko migracje wewnętrzne"],
    1,
    "Migracje zarobkowe to 'przemieszczanie się osoby lub grupy osób przez granicę międzynarodową lub w obrębie państwa motywowane wyłącznie lub przede wszystkim możliwościami ekonomicznymi'.",
    ["Migracje zarobkowe mogą być zarówno trwałe, jak i czasowe.", "To dokładna definicja migracji zarobkowych z materiału źródłowego.", "Migracje zarobkowe mogą być zarówno trwałe, jak i czasowe.", "Migracje zarobkowe mogą być zarówno międzynarodowe, jak i wewnętrzne."]
))
question_id += 1

# ===== MIĘDZYNARODOWE PRZEPŁYWY TECHNOLOGII =====
questions.append(create_question(
    question_id, "Międzynarodowe przepływy technologii",
    "Kto zdefiniował technologię jako 'wiedzę niezbędną do wytwarzania dóbr i usług'?",
    ["W. Orlikowski", "T. Schlie", "L. Steele", "L. Balcerowicz"],
    2,
    "L. Steele zdefiniował technologię jako 'wiedzę niezbędną do wytwarzania dóbr i usług'.",
    ["W. Orlikowski zdefiniował technologię jako obiekty fizyczne, nie wiedzę.", "T. Schlie zdefiniował technologię jako procesy, nie wiedzę.", "To dokładna informacja z materiału źródłowego.", "L. Balcerowicz zdefiniował międzynarodowy transfer wiedzy technicznej, nie technologię w ten sposób."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowe przepływy technologii",
    "Co to jest międzynarodowy transfer wiedzy technicznej według materiału?",
    ["Tylko sprzedaż technologii", "Przemieszczanie się wiedzy technicznej, które prowadzi do zmian jakościowych zachodzących zarówno w poszczególnych krajach, jak i w gospodarce światowej", "Tylko zakup technologii", "Tylko licencjonowanie"],
    1,
    "Transfer technologii to przemieszczanie się wiedzy technicznej, które prowadzi do zmian jakościowych zachodzących zarówno w poszczególnych krajach, jak i w gospodarce światowej.",
    ["Transfer technologii to więcej niż tylko sprzedaż - to przemieszczanie się wiedzy.", "To dokładna definicja transferu technologii z materiału źródłowego.", "Transfer technologii to więcej niż tylko zakup - to przemieszczanie się wiedzy.", "Transfer technologii może odbywać się na różne sposoby, nie tylko licencjonowanie."]
))
question_id += 1

# ===== POLITYKA WALUTOWA =====
questions.append(create_question(
    question_id, "Polityka walutowa",
    "Co to jest polityka walutowa według materiału?",
    ["Tylko zarządzanie rezerwami walutowymi", "Zarządzanie kursem danej waluty, czyli oddziaływanie albo celowa decyzja o zaniechaniu oddziaływania na kurs walutowy", "Tylko ustalanie kursu stałego", "Tylko ustalanie kursu płynnego"],
    1,
    "Polityka walutowa to zarządzanie kursem danej waluty, czyli oddziaływanie albo celowa decyzja o zaniechaniu oddziaływania na kurs walutowy.",
    ["Polityka walutowa to szersze pojęcie niż tylko zarządzanie rezerwami.", "To dokładna definicja polityki walutowej z materiału źródłowego.", "Polityka walutowa może obejmować różne reżimy kursowe, nie tylko stały.", "Polityka walutowa może obejmować różne reżimy kursowe, nie tylko płynny."]
))
question_id += 1

questions.append(create_question(
    question_id, "Polityka walutowa",
    "Które z poniższych są celami polityki walutowej wymienionymi w materiale?",
    ["Tylko stworzenie korzystnych warunków wymiany", "Stworzenie korzystnych warunków wymiany w handlu międzynarodowym dla krajowych przedsiębiorców, zapobieganie wzrostowi deficytu w bilansie płatniczym oraz gwałtownym i znacznym zmianom kursu waluty krajowej, osiągnięcie optymalnego poziomu kursu walutowego", "Tylko zapobieganie wzrostowi deficytu", "Tylko osiągnięcie optymalnego poziomu kursu"],
    1,
    "Cele polityki walutowej: Stworzenie korzystnych warunków wymiany w handlu międzynarodowym dla krajowych przedsiębiorców; Zapobieganie wzrostowi deficytu w bilansie płatniczym oraz gwałtownym i znacznym zmianom kursu waluty krajowej; Osiągnięcie optymalnego poziomu kursu walutowego z punktu widzenia potrzeb gospodarki krajowej i balansu płatniczego.",
    ["To tylko jeden z celów, nie wszystkie.", "To kompletna lista celów polityki walutowej z materiału źródłowego.", "To tylko jeden z celów, nie wszystkie.", "To tylko jeden z celów, nie wszystkie."]
))
question_id += 1

# ===== RYNEK WALUTOWY - FUNKCJE =====
questions.append(create_question(
    question_id, "Rynek walutowy",
    "Która z poniższych jest funkcją rynku walutowego wymienioną w materiale?",
    ["Tylko umożliwienie wymiany walut", "Umożliwia dokonywanie wymiany pieniądza jednego kraju na pieniądz innego kraju, umożliwia zabezpieczenie uczestników obrotu gospodarczego przed negatywnymi konsekwencjami wahań kursów walut, umożliwienie uczestnikom gry na zniżkę lub zwyżkę wartości walut", "Tylko zabezpieczenie przed wahaniami", "Tylko umożliwienie gry na walutach"],
    1,
    "Funkcje rynku walutowego: Umożliwia dokonywanie wymiany pieniądza jednego kraju na pieniądz innego kraju; Umożliwia zabezpieczenie uczestników obrotu gospodarczego przed negatywnymi konsekwencjami wahań kursów walut; Umożliwienie uczestnikom gry na zniżkę lub zwyżkę wartości walut.",
    ["To tylko jedna z funkcji, nie wszystkie.", "To kompletna lista funkcji rynku walutowego z materiału źródłowego.", "To tylko jedna z funkcji, nie wszystkie.", "To tylko jedna z funkcji, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Rynek walutowy",
    "Który rodzaj rynku walutowego ma kurs ustalony w momencie zawarcia transakcji, ale dostawa waluty następuje w przyszłości?",
    ["Rynek bieżący", "Rynek terminowy", "Rynek spot", "Rynek natychmiastowy"],
    1,
    "Rodzaje rynku walutowego: Terminowy --> kurs jest ustalony w momencie zawarcia transakcji, ale dostawa waluty i płatność następują w określonym momencie w przyszłości, np. za miesiąc.",
    ["Rynek bieżący to inny rodzaj - dostawa natychmiast lub w ciągu 2 dni.", "To dokładna informacja z materiału źródłowego o rynku terminowym.", "Rynek spot to rodzaj rynku bieżącego, nie terminowego.", "Rynek natychmiastowy to rodzaj rynku bieżącego, nie terminowego."]
))
question_id += 1

# ===== KURS WALUTOWY - RODZAJE =====
questions.append(create_question(
    question_id, "Kurs walutowy",
    "Co to jest kurs płynny według materiału?",
    ["Kurs ustalony przez państwo", "Kurs nie jest ustalony przez państwo, ceny walut kształtują się swobodnie na rynku walutowym pod wpływem podaży i popytu", "Kurs waha się w określonych granicach", "Kurs stały"],
    1,
    "Kurs płynny to kurs, który nie jest ustalony przez państwo, ceny walut kształtują się swobodnie na rynku walutowym pod wpływem podaży i popytu.",
    ["Kurs płynny nie jest ustalony przez państwo, kształtuje się swobodnie na rynku.", "To dokładna definicja kursu płynnego z materiału źródłowego.", "To definicja kursu stałego, nie płynnego.", "Kurs stały to inny rodzaj kursu, nie płynny."]
))
question_id += 1

questions.append(create_question(
    question_id, "Kurs walutowy",
    "Co to jest kurs stały według materiału?",
    ["Kurs nieustalony przez państwo", "Kurs waha się w określonych granicach w stosunku do jednej waluty lub koszyka walut", "Kurs kształtujący się swobodnie", "Kurs bez żadnych granic"],
    1,
    "Kurs stały to kurs, który waha się w określonych granicach w stosunku do jednej waluty lub koszyka walut.",
    ["Kurs stały jest kontrolowany przez państwo w określonych granicach.", "To dokładna definicja kursu stałego z materiału źródłowego.", "To definicja kursu płynnego, nie stałego.", "Kurs stały ma określone granice, nie jest bez granic."]
))
question_id += 1

questions.append(create_question(
    question_id, "Kurs walutowy",
    "Co to jest rewaluacja według materiału?",
    ["Urzędowe obniżenie waluty krajowej względem walut obcych", "Urzędowe podniesienie waluty krajowej, względem walut obcych", "Spadek wartości waluty na rynku", "Wzrost wartości waluty na rynku"],
    1,
    "Rewaluacja to urzędowe podniesienie waluty krajowej, względem walut obcych.",
    ["To definicja dewaluacji, nie rewaluacji.", "To dokładna definicja rewaluacji z materiału źródłowego.", "Rewaluacja to decyzja władz, nie tylko spadek na rynku.", "Rewaluacja to decyzja władz, nie tylko wzrost na rynku."]
))
question_id += 1

questions.append(create_question(
    question_id, "Kurs walutowy",
    "Co to jest dewaluacja według materiału?",
    ["Urzędowe podniesienie waluty krajowej względem walut obcych", "Urzędowe obniżenie waluty krajowej względem walut obcych", "Wzrost wartości waluty na rynku", "Spadek wartości waluty na rynku"],
    1,
    "Dewaluacja to urzędowe obniżenie waluty krajowej względem walut obcych.",
    ["To definicja rewaluacji, nie dewaluacji.", "To dokładna definicja dewaluacji z materiału źródłowego.", "Dewaluacja to decyzja władz, nie tylko wzrost na rynku.", "Dewaluacja to decyzja władz, nie tylko spadek na rynku."]
))
question_id += 1

# ===== MIĘDZYNARODOWY SYSTEM WALUTOWY - DODATKOWE =====
questions.append(create_question(
    question_id, "Międzynarodowy system walutowy",
    "Co to jest międzynarodowy system walutowy według materiału?",
    ["Tylko sposób ustalania kursów walutowych", "Zespół układów, instytucji, w ramach których dokonywane są płatności związane z transakcjami dotyczącymi różnych krajów, w szczególności określające sposób ustalania kursów walutowych i rolę rządów w tym zakresie", "Tylko instytucje walutowe", "Tylko rządy"],
    1,
    "Międzynarodowy system walutowy to zespół układów, instytucji, w ramach których dokonywane są płatności związane z transakcjami dotyczącymi różnych krajów, w szczególności określające sposób ustalania kursów walutowych i rolę rządów w tym zakresie.",
    ["To tylko jeden z elementów, nie wszystkie.", "To dokładna definicja międzynarodowego systemu walutowego z materiału źródłowego.", "To tylko jeden z elementów, nie wszystkie.", "To tylko jeden z elementów, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowy system walutowy",
    "Które kraje są wymienione w materiale jako mające waluty odgrywające rolę pieniądza międzynarodowego w systemie wielodywizowym?",
    ["Tylko USA i UE", "Obok dolara i euro, waluty wielu krajów, w których znajdują się międzynarodowe centra finansowe (UK, Szwajcaria, Japonia)", "Tylko UK", "Tylko Szwajcaria i Japonia"],
    1,
    "Charakterystyczna cecha systemu wielodywizowego - występowanie wielu walut, które odgrywają rolę pieniądza międzynarodowego, obok dolara i euro, są to waluty wielu krajów, w których znajdują się międzynarodowe centra finansowe (UK, Szwajcaria, Japonia).",
    ["To niekompletna lista - są też inne kraje.", "To dokładna informacja z materiału źródłowego o krajach z walutami międzynarodowymi.", "To tylko jeden z krajów, nie wszystkie.", "To tylko część krajów, nie wszystkie."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowy system walutowy",
    "Co to jest optymalny obszar walutowy według materiału?",
    ["Obszar z różnymi walutami", "Obszar, w którym przyjęcie jednej waluty lub stosowanie kursów sztywnych zwiększa dobrobyt ponad poziom, jaki istniałby wówczas, gdyby każde z państw pozostało przy swojej walucie funkcjonującej w systemie płynnych kursów", "Obszar z płynnymi kursami", "Obszar bez waluty"],
    1,
    "Teoria tzw. Optymalnego obszaru walutowego to obszar, w którym przyjęcie jednej waluty lub stosowanie kursów sztywnych zwiększa dobrobyt ponad poziom, jaki istniałby wówczas, gdyby każde z państw pozostało przy swojej walucie funkcjonującej w systemie płynnych kursów.",
    ["Optymalny obszar walutowy to obszar z jedną walutą lub sztywnymi kursami, nie różnymi walutami.", "To dokładna definicja optymalnego obszaru walutowego z materiału źródłowego.", "Optymalny obszar walutowy to obszar z jedną walutą lub sztywnymi kursami, nie płynnymi.", "Optymalny obszar walutowy ma walutę, nie jest bez waluty."]
))
question_id += 1

questions.append(create_question(
    question_id, "Międzynarodowy system walutowy",
    "Co to jest unia walutowa według materiału?",
    ["Obszar z różnymi walutami", "System, w którym kraje tworzące optymalny obszar walutowy rezygnują z e swoich walut narodowych na rzecz wspólnej waluty i nie prowadzą niezależnych polityk pieniężnych względem siebie", "Obszar z płynnymi kursami", "Obszar bez banku centralnego"],
    1,
    "Unia walutowa to system, w którym kraje tworzące optymalny obszar walutowy rezygnują z e swoich walut narodowych na rzecz wspólnej waluty i nie prowadzą niezależnych polityk pieniężnych względem siebie. Powoływany jest w tym celu wspólny bank centralny.",
    ["Unia walutowa to obszar z jedną wspólną walutą, nie różnymi walutami.", "To dokładna definicja unii walutowej z materiału źródłowego.", "Unia walutowa to obszar z jedną wspólną walutą, nie płynnymi kursami.", "Unia walutowa ma wspólny bank centralny, nie jest bez banku centralnego."]
))
question_id += 1

print(f"Generated {len(questions)} questions so far")

# Now balance the answer distribution
answer_counts = [0, 0, 0, 0]
for q in questions:
    answer_counts[q['correctAnswerIndex']] += 1

print(f"Current distribution: A={answer_counts[0]}, B={answer_counts[1]}, C={answer_counts[2]}, D={answer_counts[3]}")

# Target: approximately equal distribution
target_per_answer = len(questions) // 4
print(f"Target: approximately {target_per_answer} questions per answer")

# Reorder options and adjust correctAnswerIndex to balance distribution
random.seed(42)  # For reproducibility

balanced_questions = []
answer_targets = [target_per_answer] * 4
current_counts = [0, 0, 0, 0]

for i, q in enumerate(questions):
    # Determine which answer index we need more of
    needed_indices = [idx for idx in range(4) if current_counts[idx] < answer_targets[idx]]
    
    if needed_indices and q['correctAnswerIndex'] not in needed_indices:
        # Swap the correct answer to a needed position
        old_correct_idx = q['correctAnswerIndex']
        new_correct_idx = needed_indices[0]
        
        # Swap options and rationales
        options = q['options'].copy()
        rationales = q['rationales'].copy()
        
        # Swap positions
        options[old_correct_idx], options[new_correct_idx] = options[new_correct_idx], options[old_correct_idx]
        rationales[old_correct_idx], rationales[new_correct_idx] = rationales[new_correct_idx], rationales[old_correct_idx]
        
        q['options'] = options
        q['rationales'] = rationales
        q['correctAnswerIndex'] = new_correct_idx
    
    current_counts[q['correctAnswerIndex']] += 1
    balanced_questions.append(q)

questions = balanced_questions

# Final distribution check
final_counts = [0, 0, 0, 0]
for q in questions:
    final_counts[q['correctAnswerIndex']] += 1

print(f"Final distribution: A={final_counts[0]}, B={final_counts[1]}, C={final_counts[2]}, D={final_counts[3]}")

# Save the complete set
with open('web/src/data/questions-pl.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved {len(questions)} questions to file with balanced answer distribution")
