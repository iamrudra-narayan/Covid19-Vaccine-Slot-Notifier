import requests
import time
import json
import schedule

data = []
def cowin_extract(): 
    base_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=457&date=25-09-2021'
    r = requests.get(base_url)
    json_object = json.loads(r.text)
    count = json_object['sessions']
    if len(count)>0:
       for session in count:
           min_age_limit = session['min_age_limit']
           name = session['name']
           pincode = session['pincode']
           available_capacity = session['available_capacity']
           available_capacity_dose1= session['available_capacity_dose1']
           available_capacity_dose2= session['available_capacity_dose2']
           fee_type= session['fee_type']
           fee= session['fee']
           vaccine= session['vaccine']
           if available_capacity>0: 
             #if fee_type=='Paid': 
               #if min_age_limit =='18':
                  data.append('Age Limit- {} Above,  Hospital Name:- {},  Pincode:- {},  Available:- {},  Available Dose-1:- {},  Available Dose-2:- {},  Fee-Type:- {},  Vaccine:- {}'.format(min_age_limit,name,pincode,available_capacity,available_capacity_dose1,available_capacity_dose2,fee_type,vaccine))  
                  print(data)
                  for msg in data:
                    base_url = 'https://api.telegram.org/bot2022169366:AAH_3VcpgwpkM_HzLlQ2y_VjYcDaVUceb7g/sendMessage?chat_id=-1001512929540&text={}'.format(msg)
                    requests.get(base_url)
if __name__ == '__main__':
   cowin_extract()
#
schedule.every(1).minutes.do(cowin_extract)
#
while True:
   schedule.run_pending()
   time.sleep(1)
