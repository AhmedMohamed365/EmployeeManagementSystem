// Authentication related types
export interface LoginCredentials {
  email: string;
  password: string;
}

export interface JWTTokens {
  access: string;
  refresh: string;
}

export interface User {
  id: number;
  email: string;
  username: string;
  role: 'admin' | 'manager' | 'employee';
}