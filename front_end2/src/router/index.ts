import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/components/LandingView/LandingView.vue'),
      meta: {
        title: 'Home',
        showBreadCrumb: true
      }
    },
    {
      path: '/datalist',
      name: 'Datalist',
      component: () => import('@/components/DataList/DataList.vue'),
      meta: {
        title: 'Data List',
        showBreadCrumb: true
      }
    },
    {
      path: '/celltype/:id',
      name: 'CellType',
      component: () => import('@/components/CellType/CellType.vue'),
      meta: {
        title: 'Cell Type',
        showBreadCrumb: true
      }
    },
    // {
    //   path: '/search',
    //   name: 'Search',
    //   component: () => import('@/components/search/search.vue')
    // },
    {
      path: '/genome-browser',
      name: 'genome-browser',
      component: () => import('@/components/Browser/index.vue'),
      meta: {
        title: 'Genome Browser',
        showBreadCrumb: true
      }
    },
    {
      path: '/cancer-cre',
      name: 'CancerCRE',
      component: () => import('@/components/CancerCRE/index.vue'),
      meta: {
        title: 'Cancer 3D genome',
        showBreadCrumb: true
      }
      // component: Analysis,
      // children: [
      //   {
      //     path: 'annotations',
      //     name: 'LoopSetsAnnotation',
      //     component: () => import('@/components/LoopSetsAnnotation/index.vue')
      //   }//,
      // {
      //   path: 'differential-loops-analysis',
      //   name: 'DifferentialLoopsAnalysis',
      //   component: DifferentialLoopsAnalysis
      // },
      // {
      //   path: 'transcription-factor-analysis',
      //   name: 'TranscriptionFactorAnalysis',
      //   component: TranscriptionFactorAnalysis
      // },
      // {
      //   path: '4c-virtual-plot',
      //   name: 'Virtual4CPlot',
      //   component: Virtual4CPlot
      // }
      // ]
    },
    {
      path: '/cancer-cre/:id',
      name: 'CancerCREDetail',
      component: () => import('@/components/CancerCRE/CancerCREDetail.vue'),
      meta: {
        title: 'Cancer 3D Detail',
        showBreadCrumb: false
      }
    },
    {
      path: '/annotation',
      name: 'Annotation',
      redirect: { name: 'Uploads' },
      component: () => import('@/components/Annotation/index.vue'),
      meta: {
        title: 'Loop annotation',
        showBreadCrumb: true
      },
      children: [
        {
          path: 'uploads',
          name: 'Uploads',
          component: () => import('@/components/Annotation/Uploads.vue'),
          meta: {
            title: 'Loop annotation details',
            showBreadCrumb: false
          }
        },
        {
          path: 'task-info/:taskId',
          name: 'AnnotationDetail',
          component: () => import('@/components/Annotation/AnnotationDetail.vue'),
          meta: {
            title: 'Loop annotation details',
            showBreadCrumb: false
          }
        }
      ]
    },
    // {
    //   path: '/status/task-info/:id',
    //   name: 'Annotation',
    //   component: () => import('@/components/Annotation/AnnotationDetail.vue'),
    //   meta: {
    //     title: 'Loop annotation details'
    //   }
    // },
    {
      path: '/download',
      name: 'Download',
      component: () => import('@/components/Download/index.vue'),
      meta: {
        title: 'Download'
      }
    },
    {
      path: '/documentation',
      name: 'Documentation',
      component: () => import('@/components/Documentation/index.vue'),
      meta: {
        title: 'Documentation'
      }
    },
  ],
})
router.afterEach((to, from, next) => {
  console.log('router.beforeEach')
  const { meta } = to;
  console.log(meta)
  Object.keys(meta).forEach((key) => {
    if (typeof meta[key] === 'function') {
      meta[key] = meta[key](to);
      console.log(meta[key])
    }
  });
  // next();
});
export default router
