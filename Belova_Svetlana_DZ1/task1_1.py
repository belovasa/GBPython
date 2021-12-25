"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
* до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""
def convert_time(duration: int) -> str:
   result = ''
   while duration >= 60:
      if duration >= 86400:
         dur_day = duration//86400
         result = str(dur_day)+' дн '
         duration = duration % 86400
      elif duration < 86400 and duration >= 3600:
         dur_hour = duration//3600
         result = result+str(dur_hour) + ' час '
         duration = duration % 3600
      elif duration < 3600:
         dur_min = duration//60
         result = result + str(dur_min) + ' мин '
         duration = duration % 60
      else:
         dur_sec = duration
         result = result+str(dur_sec) + ' сек'
   return result

# duration = 53
# duration = 153
# duration = 4153
duration = 400153
result = convert_time(duration)
print(result)