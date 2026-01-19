export type QuizQuestion = {
  id: number
  category: string
  question: string
  options: string[]
  correctAnswerIndex: number
  /**
   * Krótkie wyjaśnienie: dlaczego odpowiedź poprawna jest poprawna.
   */
  explanation: string
  /**
   * Uzasadnienia dla każdej opcji (w tej samej kolejności co `options`).
   * Dla opcji poprawnej powinno tłumaczyć „dlaczego to jest dobre”.
   * Dla opcji błędnych powinno tłumaczyć „dlaczego to jest błędne”.
   */
  rationales: string[]
}

