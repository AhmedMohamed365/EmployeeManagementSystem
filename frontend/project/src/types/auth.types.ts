export interface LoginCredentials {
  email: string;
  password: string;
}

export interface JWTTokens {
  access: string;
  refresh: string;
}

export interface User {
  id: string;
  email: string;
  role: string;
  // Add other user-specific fields as needed
}

export interface RegisterUser {
  email: string;
  password: string;
  role: string; // Include any required fields for registration
}
