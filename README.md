# Quiz z ekonomii międzynarodowej

To repozytorium zawiera prostą aplikację webową z quizem (w 100% po polsku), przygotowaną na podstawie materiału:
`Ekonomia międzynarodowa.txt`.

## Jak uruchomić

Wszystko jest w katalogu `web/`.

```bash
cd web
npm install
npm run dev
```

## Jak zbudować (build)

```bash
cd web
npm run build
npm run preview
```

## Baza pytań

- Plik z pytaniami: `web/src/data/questions-pl.json`
- Każde pytanie ma:
  - odpowiedzi wielokrotnego wyboru,
  - wskazaną poprawną odpowiedź,
  - **wyjaśnienie dlaczego poprawna jest poprawna** i **dlaczego błędne są błędne** (dla każdej opcji osobno).

