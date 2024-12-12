export interface User {
  id: number;
  username: string;
  email: string;
  role: 'admin' | 'manager' | 'employee';
}

export interface Company {
  id: number;
  name: string;
  number_of_departments: number;
  number_of_employees: number;
}

export interface Department {
  id: number;
  name: string;
  company: number;
  company_name: string;
  number_of_employees: number;
}

export interface Employee {
  id: number;
  status: 'Onboarding' | 'Hired' | 'Terminated';
  name: string;
  email: string;
  mobile_number: string;
  address: string;
  designation: string;
  hired_on: string | null;
  company: number;
  department: number;
}

export interface TokenPair {
  access: string;
  refresh: string;
}