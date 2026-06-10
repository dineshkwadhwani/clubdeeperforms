// In-memory override store — only stores explicit admin changes
// Keys not present here = use the default from projects.ts (p.active)
const overrides: Map<number, boolean> = new Map();

export function getOverride(index: number): boolean | null {
  return overrides.has(index) ? overrides.get(index)! : null;
}

export function setOverride(index: number, enabled: boolean): void {
  overrides.set(index, enabled);
}

export function deleteOverride(index: number): void {
  overrides.delete(index);
}

// Returns only explicitly set overrides — null means "use default"
export function getAllOverrides(): Record<number, boolean | null> {
  const result: Record<number, boolean | null> = {};
  for (let i = 1; i <= 20; i++) {
    result[i] = overrides.has(i) ? overrides.get(i)! : null;
  }
  return result;
}

export function setAllOverrides(config: Record<number, boolean>): void {
  overrides.clear();
  for (const [key, val] of Object.entries(config)) {
    overrides.set(Number(key), val);
  }
}

export function clearAllOverrides(): void {
  overrides.clear();
}
