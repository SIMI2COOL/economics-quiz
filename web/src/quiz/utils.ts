export function shuffle<T>(items: readonly T[], seed?: number): T[] {
  // Prosty, deterministyczny shuffle gdy podany seed (ułatwia testy/powtarzalność).
  // Jeśli seed niepodany, używamy Math.random().
  const arr = [...items]
  let s = typeof seed === 'number' ? seed >>> 0 : undefined

  const rand = () => {
    if (s === undefined) return Math.random()
    // LCG: https://en.wikipedia.org/wiki/Linear_congruential_generator (proste i wystarczające)
    s = (1664525 * s + 1013904223) >>> 0
    return s / 2 ** 32
  }

  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1))
    ;[arr[i], arr[j]] = [arr[j], arr[i]]
  }
  return arr
}

export function unique<T>(items: readonly T[]): T[] {
  return [...new Set(items)]
}

