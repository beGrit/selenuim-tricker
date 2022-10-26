import csv
import datetime

def demo():
    a_date = datetime.datetime.strptime('20221001', '%Y%m%d')
    b_date = datetime.datetime.strptime('20221002', '%Y%m%d')
    print(a_date > b_date)

def run():
    vps_eta_dt = {}
    vps_etd_dt = {}
    with open('config/ex_rate_20220929.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print(csv_reader)
        for row in csv_reader:
            vps_eta_dt_date = datetime.datetime.strptime(row['VPS_ETA_DT'], '%Y%m%d')
            vps_etd_dt_date = datetime.datetime.strptime(row['VPS_ETD_DT'], '%Y%m%d')
            if 'min' not in vps_etd_dt:
                vps_eta_dt['min'] = datetime.datetime.fromtimestamp(vps_eta_dt_date.timestamp())
            else:
                if vps_eta_dt['min'] >= vps_eta_dt_date:
                    vps_eta_dt['min'] = datetime.datetime.fromtimestamp(vps_eta_dt_date.timestamp())

            if 'min' not in vps_etd_dt:
                vps_etd_dt['min'] = datetime.datetime.fromtimestamp(vps_etd_dt_date.timestamp())
            else:
                if vps_etd_dt['min'] >= vps_etd_dt_date:
                    vps_etd_dt['min'] = datetime.datetime.fromtimestamp(vps_etd_dt_date.timestamp())

            if 'max' not in vps_eta_dt:
                vps_eta_dt['max'] = datetime.datetime.fromtimestamp(vps_eta_dt_date.timestamp())
            else:
                if vps_eta_dt['max'] <= vps_eta_dt_date:
                    vps_eta_dt['max'] = datetime.datetime.fromtimestamp(vps_eta_dt_date.timestamp())

            if 'max' not in vps_etd_dt:
                vps_etd_dt['max'] = datetime.datetime.fromtimestamp(vps_etd_dt_date.timestamp())
            else:
                if vps_etd_dt['max'] <= vps_etd_dt_date:
                    vps_etd_dt['max'] = datetime.datetime.fromtimestamp(vps_etd_dt_date.timestamp())
    trans_dict = [
        vps_etd_dt,
        vps_eta_dt,
    ]
    for target_dict in trans_dict:
        for key, value in target_dict.items():
            value = value.strftime('%Y%m%d')
            target_dict[key] = value
    print("VPS ETA DT: " + str(vps_eta_dt))
    print("VPS ETD DT: " + str(vps_etd_dt))

run()
