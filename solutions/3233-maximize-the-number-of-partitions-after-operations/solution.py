class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dp(i: int, mask: int, changed: bool) -> int:
            """
            Возвращает макс. кол-во партиций для s[i:] с учетом текущего состояния.
            i: текущий индекс
            mask: битовая маска символов в текущей партиции
            changed: флаг, была ли уже произведена замена
            """
            
            # Базовый случай: дошли до конца строки.
            # Последняя партиция, которую мы формировали, заканчивается здесь.
            if i == n:
                return 1

            # --- Вариант 1: Не меняем символ s[i] ---
            
            char_bit = 1 << (ord(s[i]) - ord('a'))
            new_mask_no_change = mask | char_bit
            
            res_no_change = 0
            # Если добавление s[i] превышает лимит k
            if new_mask_no_change.bit_count() > k:
                # Начинаем новую партицию. +1 к счету.
                # Новая партиция содержит только s[i].
                res_no_change = 1 + dp(i + 1, char_bit, changed)
            else:
                # Продолжаем текущую партицию.
                res_no_change = dp(i + 1, new_mask_no_change, changed)

            # --- Вариант 2: Меняем символ s[i] (если еще можно) ---
            
            res_change = 0
            if not changed:
                # Перебираем все 26 возможных символов для замены
                for j in range(26):
                    new_char_bit = 1 << j
                    new_mask_with_change = mask | new_char_bit
                    
                    current_res = 0
                    if new_mask_with_change.bit_count() > k:
                        # Начинаем новую партицию с измененным символом
                        current_res = 1 + dp(i + 1, new_char_bit, True)
                    else:
                        # Продолжаем текущую партицию с измененным символом
                        current_res = dp(i + 1, new_mask_with_change, True)
                    
                    res_change = max(res_change, current_res)

            return max(res_no_change, res_change)

        # Начальный вызов: начинаем с индекса 0, пустой маской и без изменений.
        return dp(0, 0, False)
