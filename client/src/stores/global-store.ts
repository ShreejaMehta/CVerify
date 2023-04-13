import { defineStore } from 'pinia'

export const useGlobalStore = defineStore('global', {
	state: () => {
		return {
			isSidebarMinimized: false,
			userName: 'admin',
			isLoggedIn: false,
		}

	},

	actions: {
		toggleSidebar() {
			this.isSidebarMinimized = !this.isSidebarMinimized
		},

		changeUserName(userName: string) {
			this.userName = userName
		},
		updateLoggedInStatus(isLoggedIn: boolean) {
			this.isLoggedIn = isLoggedIn
		}
	},
})
