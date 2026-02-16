import { useEffect, useState } from 'react';
import { apiBaseUrl } from '/utils/supabase/info';

export function useSeedData() {
  const [seeded, setSeeded] = useState(false);

  useEffect(() => {
    const pingHealth = async () => {
      try {
        await fetch(`${apiBaseUrl}/health`);
      } catch {
        // Local API may not be running yet.
      } finally {
        // Seeding is handled by local_api.py (SQLite), not frontend.
        setSeeded(true);
      }
    };

    pingHealth();
  }, []);

  return seeded;
}
