from datetime import datetime, timezone                                           
now = datetime.now()

date_time  = now.strftime('%Y%m%d%H%m%s')
timestamp  = date_time[slice(0, 14,1)]
print(timestamp)

# {
#   "content": {
#     "amount": "10",
#     "phone_number": '257400000232'
#   }, 
#   "message": "Success", 
#   "status_code": 200
# }