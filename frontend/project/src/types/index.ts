export interface User {
  id: number;
  username: string;
  email: string;
  token?: string;
}

export interface Company {
  id: number;
  name: string;
  description?: string;
  created_at: string;
}

export interface Department {
  id: number;
  name: string;
  company: number;
  description?: string;
}

export interface Employee {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  department: number;
  position: string;
  hire_date: string;
}