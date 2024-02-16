import sys

class ProgressBar:
    def __init__(self):
        self._bar_length = 50

    def show_progress_bar(self, number_of_completed_rows: int, total_rows: int):
        if self._should_delay(number_of_completed_rows=number_of_completed_rows, total_rows=total_rows):
            return
        
        percent = round(number_of_completed_rows / total_rows * 100)
        filled_length = int(self._bar_length * percent / 100)
        bar = self._get_bar(filled_length=filled_length)

        sys.stdout.write(f"\r[{bar}] {percent:.0f}%")
        sys.stdout.flush()

    def _get_bar(self, filled_length: int):
        bar = '=' * filled_length + '-' * (self._bar_length - filled_length)

        return bar
    
    def _should_delay(self, number_of_completed_rows: int, total_rows: int):
        return number_of_completed_rows % 10 != 0 and number_of_completed_rows != total_rows
