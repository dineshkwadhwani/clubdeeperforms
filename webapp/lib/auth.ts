export function getTodayPassword(prefix: string): string {
  const now = new Date();
  const dd = String(now.getDate()).padStart(2, "0");
  const mm = String(now.getMonth() + 1).padStart(2, "0");
  const yyyy = String(now.getFullYear());
  return `${prefix}${dd}${mm}${yyyy}`;
}

export function checkUserPassword(password: string): boolean {
  return password === getTodayPassword("clubdeeper");
}

export function checkAdminPassword(password: string): boolean {
  return password === getTodayPassword("dinesh");
}
