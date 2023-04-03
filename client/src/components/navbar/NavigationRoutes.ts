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
      name: 'Resume',
      displayName: 'Resume ',
      meta: {
        icon: 'vuestic-iconset-forms',
      },
      disabled: true,
      children: [
        {
          name: 'user-info',
          displayName: 'User Dashboard',
        },
        {
          name: 'user-upload',
          displayName: 'Resume upload',
        },
        /* { */
        /*   name: 'file-upload', */
        /*   displayName: 'File Upload', */
        /* }, */
      ],
    },
  ] as INavigationRoute[],
}
