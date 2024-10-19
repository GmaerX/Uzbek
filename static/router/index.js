import { createRouter, createWebHashHistory } from 'vue-router'
import AboutUs from "@/pages/AboutUs/AboutUs.vue";
import FullPage from "@/components/FullPage.vue";
import MemberAssociation from "@/components/MemberAssociation.vue";
import MainPage from "@/pages/MainPage/MainPage.vue";
import FamousPersonsPage from "@/pages/FamousPersonsPage/FamousPersonsPage.vue";
import FamousPersonDetailed from "@/pages/FamousPersonsPage/FamousPersonDetailed.vue";
import RegionsPage from "@/pages/Regions/RegionsPage.vue";
import Guide from "@/pages/Regions/guide.vue";
import Information from "@/pages/Regions/Information.vue";
import Contacts from "@/pages/Regions/Contacts.vue";
import ContactsPage from "@/pages/Contacts'/ContactsPage.vue";
import Republic from "@/pages/Contacts'/Republic.vue";
import Regions from "@/pages/Contacts'/Regions.vue";
import PressCenter from "@/pages/PressCenter/PressCenter.vue";
import Newsdetail from "@/pages/PressCenter/Newsdetail.vue";
import Donats from "@/pages/Donats/Donats.vue";
import ViaCard from "@/pages/Donats/ViaCard.vue";
import ViaQR from "@/pages/Donats/ViaQR.vue";
import Documents from "@/pages/Documents/Documents.vue";
import OrganizationDetails from "@/pages/AboutUs/OrganizationDetails.vue";
import Sport from "@/pages/AboutUs/Sport.vue";
import Education from "@/pages/AboutUs/Education.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: FullPage,
    children: [
      {
        path: '',
        name: 'MainPage',
        component: MainPage
      },
      {
        path: '/about-us',
        name: 'AboutUs',
        component: AboutUs
      },
      {
        path: '/famous-persons',
        name: 'FamPersons',
        component: FamousPersonsPage,
      },
      {
        path: '/regions',
        name: 'regions',
        component: RegionsPage,
        redirect: '/regions/guide',
        children: [
          {
            path: 'guide',
            name: 'guide',
            component: Guide,
            props: true
          },
          {
            path: 'information',
            name: 'information',
            component: Information,
          },
          {
            path: 'contacts-info',
            name: 'contacts',
            component: Contacts,
          }
        ]
      },
      {
        path: '/documents',
        name: 'documents',
        component: Documents,
      },
      {
        path: '/press-center',
        name: 'press-center',
        component: PressCenter,
      },
      {
        path: '/news',
        name: 'news-detail',
        component: Newsdetail,
        props: true,
      },
      {
        path: '/contacts',
        name: 'contacts',
        component: ContactsPage,
        redirect: '/contacts/republic-contacts',
        children: [
          {
            path: 'republic-contacts',
            name: 'republic-contacts',
            component: Republic,
            props: true
          },
          {
            path: 'regions-contacts',
            name: 'regions-contacts',
            component: Regions,
            props: true
          }
        ]
      },
      {
        path: '/donates',
        name: 'donate ',
        component: Donats,
        redirect: '/donates/1',
        children: [
          {
            path: '1',
            name: 'viacard ',
            component: ViaCard,
          },
          {
            path: '2',
            name: 'viaqr',
            component: ViaQR,
          },
        ]
      },
      {
        path: '/organization-details',
        name:'organization-details',
        component: OrganizationDetails
      },
      {
        path: '/sport',
        name:'sport',
        component: Sport
      },
      {
        path: '/education',
        name:'education',
        component: Education
      }
    ]
  },
  {
    path: '/member-association',
    name: 'member-association',
    component: MemberAssociation
  },
  {
    path: '/person-detail',
    name: 'person-detail',
    component: FamousPersonDetailed
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
