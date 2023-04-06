export interface INavigationRoute {
  name: string
  displayName: string
  meta: { icon: string }
  children?: INavigationRoute[]
}

export default {
  root: {
    name: '/',
    displayName: 'navigationRoutes.home',
  },
  routes: [
    {
      name: 'dashboard',
      displayName: 'menu.dashboard',
      meta: {
        icon: 'vuestic-iconset-dashboard',
      },
    },
    {
      name: 'user-upload',
      displayName: 'Resume upload',
      meta: {
        icon: 'vuestic-iconset-forms',
      },
      disabled: true,
    },
  ] as INavigationRoute[],
}
