import { useGlobalStore } from '../stores/global-store'

export function isLoggedIn() {
  return useGlobalStore().isLoggedIn
}
