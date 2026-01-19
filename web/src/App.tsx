import { useMemo, useState } from 'react'
import { questions, validateQuestions } from './quiz/questions'
import type { QuizQuestion } from './quiz/types'
import { shuffle, unique } from './quiz/utils'

type Screen = 'setup' | 'quiz' | 'results'

const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')

function clamp(n: number, min: number, max: number) {
  return Math.min(max, Math.max(min, n))
}

function shuffleQuestionOptions(
  q: QuizQuestion,
  seed: number,
): QuizQuestion {
  const items = q.options.map((option, originalIndex) => ({
    option,
    rationale: q.rationales[originalIndex] ?? '',
    originalIndex,
  }))

  const shuffled = shuffle(items, seed)
  const newCorrectAnswerIndex = shuffled.findIndex(
    (x) => x.originalIndex === q.correctAnswerIndex,
  )

  return {
    ...q,
    options: shuffled.map((x) => x.option),
    rationales: shuffled.map((x) => x.rationale),
    correctAnswerIndex: newCorrectAnswerIndex,
  }
}

function App() {
  const issues = useMemo(() => validateQuestions(questions), [])
  const categories = useMemo(() => {
    return unique(questions.map((q) => q.category)).sort((a, b) =>
      a.localeCompare(b, 'pl'),
    )
  }, [])

  const [screen, setScreen] = useState<Screen>('setup')
  const [selectedCategories, setSelectedCategories] =
    useState<string[]>(categories)
  const [questionCount, setQuestionCount] = useState<number>(
    clamp(20, 1, questions.length),
  )
  const [shouldShuffle, setShouldShuffle] = useState<boolean>(true)
  const [shouldShuffleAnswers, setShouldShuffleAnswers] =
    useState<boolean>(true)

  const [quizQuestions, setQuizQuestions] = useState<QuizQuestion[]>([])
  const [currentIndex, setCurrentIndex] = useState<number>(0)
  const [answers, setAnswers] = useState<Record<number, number>>({})

  const filteredPool = useMemo(() => {
    const set = new Set(selectedCategories)
    return questions.filter((q) => set.has(q.category))
  }, [selectedCategories])

  const currentQuestion = quizQuestions[currentIndex]
  const selectedAnswerIndex =
    currentQuestion && answers[currentQuestion.id] !== undefined
      ? answers[currentQuestion.id]
      : undefined

  const score = useMemo(() => {
    let s = 0
    for (const q of quizQuestions) {
      const a = answers[q.id]
      if (a === q.correctAnswerIndex) s++
    }
    return s
  }, [answers, quizQuestions])

  function toggleCategory(cat: string) {
    setSelectedCategories((prev) => {
      if (prev.includes(cat)) return prev.filter((c) => c !== cat)
      return [...prev, cat]
    })
  }

  function startQuiz() {
    const pool = filteredPool
    const count = clamp(questionCount, 1, pool.length)
    const seed = Date.now() & 0xffffffff
    const ordered = shouldShuffle ? shuffle(pool, seed) : [...pool]
    const picked = ordered.slice(0, count)

    const prepared = shouldShuffleAnswers
      ? picked.map((q) => shuffleQuestionOptions(q, seed ^ q.id))
      : picked

    setQuizQuestions(prepared)
    setCurrentIndex(0)
    setAnswers({})
    setScreen('quiz')
  }

  function restart() {
    setQuizQuestions([])
    setCurrentIndex(0)
    setAnswers({})
    setScreen('setup')
  }

  function answerCurrent(answerIndex: number) {
    if (!currentQuestion) return
    setAnswers((prev) => {
      if (prev[currentQuestion.id] !== undefined) return prev
      return { ...prev, [currentQuestion.id]: answerIndex }
    })
  }

  function goNext() {
    const next = currentIndex + 1
    if (next >= quizQuestions.length) {
      setScreen('results')
      return
    }
    setCurrentIndex(next)
  }

  const progress = quizQuestions.length
    ? Math.round(((currentIndex + 1) / quizQuestions.length) * 100)
    : 0

  return (
    <div className="min-h-full bg-gradient-to-br from-amber-50 via-sky-50 to-emerald-50 text-slate-900">
      <div className="mx-auto max-w-4xl px-4 py-10">
        <header className="mb-8">
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <h1 className="text-2xl font-semibold tracking-tight sm:text-3xl">
                Międzynarodowy quiz z zarządzania projektami
              </h1>
              <p className="mt-2 text-sm text-slate-600">
                Pytania są oparte na pliku z zagadnieniami do egzaminu. Po
                wybraniu odpowiedzi zobaczysz uzasadnienie: dlaczego jest
                poprawna i czemu pozostałe są błędne.
              </p>
            </div>

            <div className="rounded-xl border border-slate-200 bg-white/70 px-4 py-3 text-sm shadow-sm">
              <div className="text-slate-600">Postęp</div>
              <div className="mt-1 font-medium">
                {screen === 'quiz'
                  ? `${currentIndex + 1}/${quizQuestions.length}`
                  : '—'}
              </div>
            </div>
          </div>
        </header>

        {issues.length > 0 ? (
          <div className="mb-6 rounded-xl border border-amber-300 bg-amber-50 p-4">
            <div className="font-medium text-amber-900">
              Wykryto problemy w bazie pytań:
            </div>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-amber-900/90">
              {issues.map((i) => (
                <li key={i}>{i}</li>
              ))}
            </ul>
          </div>
        ) : null}

        {screen === 'setup' ? (
          <div className="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-lg shadow-slate-200/60">
            <div className="grid gap-6 md:grid-cols-2">
              <section>
                <h2 className="text-lg font-semibold">Ustawienia quizu</h2>

                <label className="mt-4 block text-sm font-medium text-slate-700">
                  Liczba pytań
                </label>
                <div className="mt-2 flex items-center gap-3">
                  <input
                    className="w-full accent-indigo-600"
                    type="range"
                    min={1}
                    max={Math.max(1, filteredPool.length)}
                    value={clamp(questionCount, 1, Math.max(1, filteredPool.length))}
                    onChange={(e) => setQuestionCount(Number(e.target.value))}
                    disabled={filteredPool.length === 0}
                  />
                  <div className="w-16 text-right text-sm tabular-nums text-slate-800">
                    {filteredPool.length === 0
                      ? '0'
                      : clamp(questionCount, 1, filteredPool.length)}
                  </div>
                </div>

                <div className="mt-4 flex items-center justify-between gap-3 rounded-xl border border-slate-200 bg-white/60 px-4 py-3">
                  <div>
                    <div className="text-sm font-medium">Losowa kolejność</div>
                    <div className="text-xs text-slate-600">
                      Tasuje pytania przed startem
                    </div>
                  </div>
                  <button
                    type="button"
                    onClick={() => setShouldShuffle((v) => !v)}
                    className={`relative inline-flex h-6 w-11 items-center rounded-full border transition ${
                      shouldShuffle
                        ? 'border-emerald-500/70 bg-emerald-500/30'
                        : 'border-slate-300 bg-slate-200'
                    }`}
                    aria-pressed={shouldShuffle}
                  >
                    <span
                      className={`inline-block h-5 w-5 transform rounded-full bg-white shadow-sm transition ${
                        shouldShuffle ? 'translate-x-5' : 'translate-x-0.5'
                      }`}
                    />
                  </button>
                </div>

                <div className="mt-3 flex items-center justify-between gap-3 rounded-xl border border-slate-200 bg-white/60 px-4 py-3">
                  <div>
                    <div className="text-sm font-medium">
                      Losowa kolejność odpowiedzi (A/B/C/D)
                    </div>
                    <div className="text-xs text-slate-600">
                      Dzięki temu poprawna odpowiedź nie jest „prawie zawsze A”
                    </div>
                  </div>
                  <button
                    type="button"
                    onClick={() => setShouldShuffleAnswers((v) => !v)}
                    className={`relative inline-flex h-6 w-11 items-center rounded-full border transition ${
                      shouldShuffleAnswers
                        ? 'border-emerald-500/70 bg-emerald-500/30'
                        : 'border-slate-300 bg-slate-200'
                    }`}
                    aria-pressed={shouldShuffleAnswers}
                  >
                    <span
                      className={`inline-block h-5 w-5 transform rounded-full bg-white shadow-sm transition ${
                        shouldShuffleAnswers ? 'translate-x-5' : 'translate-x-0.5'
                      }`}
                    />
                  </button>
                </div>
              </section>

              <section>
                <div className="flex items-center justify-between gap-3">
                  <h2 className="text-lg font-semibold">Kategorie</h2>
                  <div className="text-xs text-slate-600">
                    Wybrane: {selectedCategories.length}/{categories.length}
                  </div>
                </div>

                <div className="mt-3 flex flex-wrap gap-2">
                  {categories.map((cat) => {
                    const on = selectedCategories.includes(cat)
                    return (
                      <button
                        key={cat}
                        type="button"
                        onClick={() => toggleCategory(cat)}
                        className={`rounded-full border px-3 py-1 text-xs font-medium transition ${
                          on
                            ? 'border-indigo-300 bg-indigo-50 text-indigo-800'
                            : 'border-slate-300 bg-white/70 text-slate-700 hover:border-indigo-300 hover:bg-indigo-50/60'
                        }`}
                      >
                        {cat}
                      </button>
                    )
                  })}
                </div>

                <div className="mt-5 flex flex-wrap gap-2">
                  <button
                    type="button"
                    className="rounded-lg border border-slate-300 bg-white/70 px-3 py-2 text-sm text-slate-800 hover:bg-white"
                    onClick={() => setSelectedCategories(categories)}
                  >
                    Zaznacz wszystkie
                  </button>
                  <button
                    type="button"
                    className="rounded-lg border border-slate-300 bg-white/70 px-3 py-2 text-sm text-slate-800 hover:bg-white"
                    onClick={() => setSelectedCategories([])}
                  >
                    Wyczyść
                  </button>
                </div>
              </section>
            </div>

            <div className="mt-6 flex flex-wrap items-center justify-between gap-3">
              <div className="text-sm text-slate-700">
                Dostępne pytania po filtrach:{' '}
                <span className="font-semibold text-slate-900">
                  {filteredPool.length}
                </span>
              </div>
              <button
                type="button"
                onClick={startQuiz}
                disabled={filteredPool.length === 0}
                className="rounded-xl bg-gradient-to-r from-indigo-600 to-fuchsia-600 px-5 py-3 text-sm font-semibold text-white shadow shadow-indigo-600/20 transition hover:from-indigo-500 hover:to-fuchsia-500 disabled:cursor-not-allowed disabled:bg-slate-300 disabled:from-slate-400 disabled:to-slate-400"
              >
                Start
              </button>
            </div>
          </div>
        ) : null}

        {screen === 'quiz' && currentQuestion ? (
          <div className="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-lg shadow-slate-200/60">
            <div className="mb-5">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <span className="inline-flex items-center rounded-full border border-indigo-200 bg-indigo-50 px-3 py-1 text-xs font-medium text-indigo-800">
                  {currentQuestion.category}
                </span>
                <div className="text-xs text-slate-600">
                  Wynik: {score}/{quizQuestions.length}
                </div>
              </div>

              <div className="mt-3 h-2 w-full overflow-hidden rounded-full bg-slate-200">
                <div
                  className="h-full bg-gradient-to-r from-indigo-500 to-fuchsia-500 transition-all"
                  style={{ width: `${progress}%` }}
                />
              </div>
            </div>

            <h2 className="text-lg font-semibold leading-snug sm:text-xl">
              {currentQuestion.question}
            </h2>

            <div className="mt-5 grid gap-3">
              {currentQuestion.options.map((opt, i) => {
                const answered = selectedAnswerIndex !== undefined
                const isCorrect = i === currentQuestion.correctAnswerIndex
                const isSelected = i === selectedAnswerIndex

                const base =
                  'w-full rounded-xl border px-4 py-3 text-left text-sm transition focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-400'
                const idle =
                  'border-slate-200 bg-white/80 hover:border-indigo-300 hover:bg-indigo-50/30'
                const correct =
                  'border-emerald-300 bg-emerald-50'
                const wrong =
                  'border-rose-300 bg-rose-50'
                const chosenRing = isSelected ? ' ring-2 ring-indigo-400/40' : ''

                const cls = answered
                  ? `${base} ${isCorrect ? correct : isSelected ? wrong : idle}${chosenRing}`
                  : `${base} ${idle}`

                return (
                  <button
                    key={`${currentQuestion.id}-${i}`}
                    type="button"
                    className={cls}
                    onClick={() => answerCurrent(i)}
                    disabled={answered}
                  >
                    <div className="flex items-start gap-3">
                      <div className="mt-0.5 inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-md border border-slate-200 bg-slate-50 text-xs font-semibold text-slate-700">
                        {LETTERS[i] ?? String(i + 1)}
                      </div>
                      <div className="flex-1">
                        <div className="font-medium text-slate-900">{opt}</div>
                        {answered ? (
                          <div className="mt-1 text-xs text-slate-600">
                            {currentQuestion.rationales[i]}
                          </div>
                        ) : null}
                      </div>
                      {answered && isCorrect ? (
                        <div className="text-xs font-semibold text-emerald-700">
                          Poprawna
                        </div>
                      ) : null}
                      {answered && isSelected && !isCorrect ? (
                        <div className="text-xs font-semibold text-rose-700">
                          Wybrana
                        </div>
                      ) : null}
                    </div>
                  </button>
                )
              })}
            </div>

            {selectedAnswerIndex !== undefined ? (
              <div className="mt-6 rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="text-sm font-semibold">
                  {selectedAnswerIndex === currentQuestion.correctAnswerIndex ? (
                    <span className="text-emerald-700">Dobrze!</span>
                  ) : (
                    <span className="text-rose-700">Nie tym razem.</span>
                  )}
                </div>
                <p className="mt-2 text-sm text-slate-800">
                  {currentQuestion.explanation}
                </p>
                <p className="mt-2 text-xs text-slate-600">
                  Poprawna odpowiedź:{' '}
                  <span className="font-semibold text-slate-900">
                    {LETTERS[currentQuestion.correctAnswerIndex]} —{' '}
                    {currentQuestion.options[currentQuestion.correctAnswerIndex]}
                  </span>
                </p>
              </div>
            ) : null}

            <div className="mt-6 flex flex-wrap items-center justify-between gap-3">
              <button
                type="button"
                onClick={restart}
                className="rounded-xl border border-slate-300 bg-white/70 px-4 py-2 text-sm text-slate-800 hover:bg-white"
              >
                Zmień ustawienia
              </button>

              <button
                type="button"
                onClick={goNext}
                disabled={selectedAnswerIndex === undefined}
                className="rounded-xl bg-gradient-to-r from-indigo-600 to-fuchsia-600 px-5 py-2.5 text-sm font-semibold text-white shadow shadow-indigo-600/20 transition hover:from-indigo-500 hover:to-fuchsia-500 disabled:cursor-not-allowed disabled:bg-slate-300 disabled:from-slate-400 disabled:to-slate-400"
              >
                {currentIndex + 1 >= quizQuestions.length ? 'Zakończ' : 'Dalej'}
              </button>
            </div>
          </div>
        ) : null}

        {screen === 'results' ? (
          <div className="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-lg shadow-slate-200/60">
            <h2 className="text-xl font-semibold">Podsumowanie</h2>
            <p className="mt-2 text-sm text-slate-700">
              Wynik:{' '}
              <span className="font-semibold text-slate-900">
                {score}/{quizQuestions.length}
              </span>{' '}
              ({quizQuestions.length ? Math.round((score / quizQuestions.length) * 100) : 0}%)
            </p>

            <div className="mt-6">
              <h3 className="text-sm font-semibold text-slate-800">
                Pytania, w których była pomyłka
              </h3>
              <div className="mt-3 space-y-3">
                {quizQuestions
                  .filter((q) => answers[q.id] !== q.correctAnswerIndex)
                  .map((q) => (
                    <div
                      key={`wrong-${q.id}`}
                      className="rounded-xl border border-slate-200 bg-white/80 p-4"
                    >
                      <div className="text-xs text-slate-600">{q.category}</div>
                      <div className="mt-1 text-sm font-medium">{q.question}</div>
                      <div className="mt-2 text-xs text-slate-700">
                        Twoja odpowiedź:{' '}
                        <span className="font-semibold text-rose-700">
                          {answers[q.id] === undefined
                            ? '—'
                            : `${LETTERS[answers[q.id]]} — ${q.options[answers[q.id]]}`}
                        </span>
                      </div>
                      <div className="mt-1 text-xs text-slate-700">
                        Poprawna odpowiedź:{' '}
                        <span className="font-semibold text-emerald-700">
                          {LETTERS[q.correctAnswerIndex]} —{' '}
                          {q.options[q.correctAnswerIndex]}
                        </span>
                      </div>
                    </div>
                  ))}
                {quizQuestions.every((q) => answers[q.id] === q.correctAnswerIndex) ? (
                  <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-4 text-sm text-emerald-900">
                    Wszystko poprawnie — świetna robota.
                  </div>
                ) : null}
              </div>
            </div>

            <div className="mt-6 flex flex-wrap gap-3">
              <button
                type="button"
                onClick={restart}
                className="rounded-xl bg-gradient-to-r from-indigo-600 to-fuchsia-600 px-5 py-2.5 text-sm font-semibold text-white shadow shadow-indigo-600/20 transition hover:from-indigo-500 hover:to-fuchsia-500"
              >
                Zagraj ponownie
              </button>
              <button
                type="button"
                onClick={() => {
                  // szybki restart z tymi samymi ustawieniami
                  setScreen('setup')
                }}
                className="rounded-xl border border-slate-300 bg-white/70 px-4 py-2 text-sm text-slate-800 hover:bg-white"
              >
                Wróć do ustawień
              </button>
            </div>
          </div>
        ) : null}

        <footer className="mt-10 text-center text-xs text-slate-500">
          Źródło pytań: plik z zagadnieniami do egzaminu (PMI/PMBOK, PCM, KE,
          prakseologia, projekty UE, Agile).
        </footer>
      </div>
    </div>
  )
}

export default App
