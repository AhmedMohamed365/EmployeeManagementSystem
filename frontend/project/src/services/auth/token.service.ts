import { JWTTokens } from '@/types/auth.types';

const TOKEN_KEY = 'auth_tokens';

export const TokenService = {
  getTokens(): JWTTokens | null {
    const tokens = localStorage.getItem(TOKEN_KEY);
    return tokens ? JSON.parse(tokens) : null;
  },

  saveTokens(tokens: JWTTokens): void {
    localStorage.setItem(TOKEN_KEY, JSON.stringify(tokens));
  },

  removeTokens(): void {
    localStorage.removeItem(TOKEN_KEY);
  },

  getAccessToken(): string | null {
    const tokens = this.getTokens();
    return tokens?.access || null;
  },

  getRefreshToken(): string | null {
    const tokens = this.getTokens();
    return tokens?.refresh || null;
  }
};