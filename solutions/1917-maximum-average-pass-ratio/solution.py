import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Создаем max-heap с использованием min-heap через отрицательные значения
        heap = []
        
        # Инициализация: вычисляем изменение коэффициента для каждого класса
        for pass_i, total_i in classes:
            # Вычисляем delta = (pass+1)/(total+1) - pass/total
            delta = (pass_i + 1) / (total_i + 1) - pass_i / total_i
            # Добавляем в кучу с отрицательным delta для имитации max-heap
            heapq.heappush(heap, (-delta, pass_i, total_i))
        
        # Распределяем всех дополнительных студентов
        for _ in range(extraStudents):
            # Извлекаем класс с максимальным увеличением коэффициента
            neg_delta, pass_i, total_i = heapq.heappop(heap)
            # Добавляем студента в этот класс
            pass_i += 1
            total_i += 1
            # Пересчитываем delta для обновленного класса
            new_delta = (pass_i + 1) / (total_i + 1) - pass_i / total_i
            heapq.heappush(heap, (-new_delta, pass_i, total_i))
        
        # Вычисляем итоговый средний коэффициент
        total_ratio = 0.0
        for _, pass_i, total_i in heap:
            total_ratio += pass_i / total_i
        
        return total_ratio / len(classes)

