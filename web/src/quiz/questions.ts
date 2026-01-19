import rawQuestions from '../data/questions-pl.json'
import type { QuizQuestion } from './types'

export const questions: QuizQuestion[] = rawQuestions as QuizQuestion[]

export function validateQuestions(qs: readonly QuizQuestion[]): string[] {
  const issues: string[] = []
  const ids = new Set<number>()

  for (const q of qs) {
    if (ids.has(q.id)) issues.push(`Duplikat id: ${q.id}`)
    ids.add(q.id)

    if (!q.category?.trim()) issues.push(`Puste category (id=${q.id})`)
    if (!q.question?.trim()) issues.push(`Puste question (id=${q.id})`)
    if (!Array.isArray(q.options) || q.options.length < 2)
      issues.push(`Za mało opcji (id=${q.id})`)
    if (q.correctAnswerIndex < 0 || q.correctAnswerIndex >= q.options.length)
      issues.push(`Błędny correctAnswerIndex (id=${q.id})`)
    if (!Array.isArray(q.rationales) || q.rationales.length !== q.options.length)
      issues.push(`rationales != options (id=${q.id})`)
  }

  return issues
}

