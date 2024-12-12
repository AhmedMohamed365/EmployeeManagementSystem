import { JWTTokens } from '@/types/auth.types';

const TOKEN_KEY = 'auth_tokens';

export const TokenService = {
  getTokens(): JWTTokens | null {
    const tokens = localStorage.getItem(TOKEN_KEY);
    console.log('Tokens from localStorage:', tokens);
    return tokens ? JSON.parse(tokens) : null;
  },

  saveTokens(tokens: JWTTokens): void {
    console.log('Saving tokens:', tokens);
    localStorage.setItem(TOKEN_KEY, JSON.stringify(tokens));
  },

  removeTokens(): void {
    console.log('Removing tokens');
    localStorage.removeItem(TOKEN_KEY);
  },

  getAccessToken(): string | null {
    const tokens = this.getTokens();
    console.log('Access Token:', tokens?.access);
    return tokens?.access || null;
  },

  getRefreshToken(): string | null {
    const tokens = this.getTokens();
    console.log('Refresh Token:', tokens?.refresh);
    return tokens?.refresh || null;
  }
};
