import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import Login from '../views/Login.vue';
import Dashboard from '../views/Dashboard.vue';
import CompanyList from '../views/companies/CompanyList.vue';
import CompanyDetail from '../views/companies/CompanyDetail.vue';
import DepartmentList from '../views/departments/DepartmentList.vue';
import DepartmentDetail from '../views/departments/DepartmentDetail.vue';
import EmployeeList from '../views/employees/EmployeeList.vue';
import EmployeeDetail from '../views/employees/EmployeeDetail.vue';
import EmployeeForm from '../views/employees/EmployeeForm.vue';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { public: true }
  },
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/companies',
    name: 'Companies',
    component: CompanyList,
  },
  {
    path: '/companies/:id',
    name: 'CompanyDetail',
    component: CompanyDetail,
  },
  {
    path: '/departments',
    name: 'Departments',
    component: DepartmentList,
  },
  {
    path: '/departments/:id',
    name: 'DepartmentDetail',
    component: DepartmentDetail,
  },
  {
    path: '/employees',
    name: 'Employees',
    component: EmployeeList,
  },
  {
    path: '/employees/new',
    name: 'NewEmployee',
    component: EmployeeForm,
  },
  {
    path: '/employees/:id',
    name: 'EmployeeDetail',
    component: EmployeeDetail,
  },
  {
    path: '/employees/:id/edit',
    name: 'EditEmployee',
    component: EmployeeForm,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (!to.meta.public && !authStore.isAuthenticated()) {
    next('/login');
  } else {
    next();
  }
});

export default router;