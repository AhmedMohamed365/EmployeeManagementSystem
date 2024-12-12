export const API_BASE_URL = 'http://your-django-api-url';
export const AUTH_BASE_URL = `${API_BASE_URL}/auth`;

export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/jwt/create/',
    REFRESH: '/jwt/refresh/',
    VERIFY: '/jwt/verify/',
    CURRENT_USER: '/users/me/',
    LOGOUT: '/token/logout/'
  },
  COMPANIES: '/api/companies',
  DEPARTMENTS: '/api/departments',
  EMPLOYEES: '/api/employees'
} as const;