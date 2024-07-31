from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from db.init import get_db
from typing import Annotated, List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/core")

db_dependency = Annotated[Session, Depends(get_db)]

# Define a Pydantic model for the response
class DeviceInfo(BaseModel):
    linked_key: str = Query(max_length=32)
    unit_serial_no: str = Query(max_length=32)
    unit_name: str = Query(max_length=100)
    product_type: str = Query(max_length=50)
    product_code: str = Query(max_length=50)
    hw_version: str = Query(max_length=50)
    fpga_version: str = Query(max_length=50)
    boot_loader: str = Query(max_length=50)
    active_sw_version: str = Query(max_length=50)
    backup_sw_version: str = Query(max_length=50)
    asset_no: str = Query(max_length=50)
    ip_address: str = Query(max_length=15)  ##perhaps change this to a ip address type
    slot_id: int ##set max and min here
    location: str = Query(max_length=100)
    config_signature : str = Query(max_length=50)
    companyname : str = Query(max_length=50)
    mac_address: str = Query(max_length=17)
    imei: str = Query(max_length=50)
    imsi: str = Query(max_length=50)
    iccid: str = Query(max_length=50)
    phone_no : str = Query(max_length=50)
    phone_no_2 : str = Query(max_length=50)
    imsi_2: str = Query(max_length=50)
    iccid_2: str = Query(max_length=50)
    config_name: str = Query(max_length=100)
    nav_submap_id: str = Query(max_length=50)

    # unit_password: str = Query(max_length=100)

    # child_node: str = Query(max_length=5)
    # xtab_mode: str = Query(max_length=15)
    # config_signature: str = Query(max_length=50)
    # node_state: str = Query(max_length=10)
    # region_id: int ##set max and min here
    # region_name : str = Query(max_length=50)
    # rack_id : int ##set max and min here
    # rack_name : str = Query(max_length=50)
    # shelf_id : int ##set max and min here
    # custom_field1 : str = Query(max_length=50)
    # snmask : str = Query(max_length=15) ##perhaps change this to a ip address type
    # gwaddr : str = Query(max_length=15) ##perhaps change this to a ip address type
    # csaddr : str = Query(max_length=50)
    # community_name : str = Query(max_length=50)
    # discovered_node : str = Query(max_length=5)
    # user_name : str = Query(max_length=50)
    # connection_method : str = Query(max_length=50)
    # q1_device : str = Query(max_length=5)
    # q1_bus : str = Query(max_length=50)
    # q1_ne_address : str = Query(max_length=50)
    # q1_fe_number : str = Query(max_length=50)
    # enable_telent : str = Query(max_length=5)
    # enable_ssh : str = Query(max_length=5)
    # enable_web : str = Query(max_length=5)
    # enable_lct : str = Query(max_length=5)
    # enable_mste : str = Query(max_length=5)
    # default_app : str = Query(max_length=20)
    # bp_mode : str = Query(max_length=20)
    # backplain_bus : int ##set max and min here
    # subnet_id : int ##set max and min here
    # phone_no: str = Query(max_length=50)
    # phone_no_2: str = Query(max_length=50)
    # use_same_ip: str = Query(max_length=5)
    # enable_config_save: str = Query(max_length=5)
    # template_1: str = Query(max_length=200)
    # template_2: str = Query(max_length=200)
    # template_3: str = Query(max_length=200)
    # device_specific_config: str = Query(max_length=5000)
    # snmpv3_eng_id_type: str = Query(max_length=20)
    # snmpv3_eng_id: str = Query(max_length=50)
    # snmpv3_user: str = Query(max_length=15)
    # maintenance_mode: str = Query(max_length=5)
    # sim_1_ip: str = Query(max_length=15)
    # sim_2_ip: str = Query(max_length=15)
    # masking_template: str = Query(max_length=200)




@router.get('/inventory', response_model=List[DeviceInfo], tags=["data"], summary='Retrieves all data associated with the device_info_tab table')
async def get_inventory(db: db_dependency):
    # Execute raw SQL
    query = """SELECT
            serial_no,
            unit_serial_no,
            unit_name,
            product_type,
            product_code,
            hw_version,
            fpga_version,
            boot_loader,
            active_sw_version,
            backup_sw_version,
            asset_no,
            ip_address,
            slot_id,
            location,
            config_signature,
            companyname,
            mac_address,
            imei,
            imsi,
            iccid,
            phone_no,
            phone_no_2,
            imsi_2,
            iccid_2,
            config_name,
            nav_submap_id
            FROM device_info_tab """

    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()


    device_info_list = []
    for row in rows:
        device_info = DeviceInfo(
            linked_key=row[0],
            unit_serial_no=row[1],
            unit_name=row[2],
            product_type=row[3],
            product_code=row[4],
            hw_version=row[5],
            fpga_version=row[6],
            boot_loader=row[7],
            active_sw_version=row[8],
            backup_sw_version=row[9],
            asset_no=row[10],
            ip_address=row[11],
            slot_id=row[12],
            location=row[13],
            config_signature=row[14],
            companyname=row[15],
            mac_address=row[16],
            imei=row[17],
            imsi=row[18],
            iccid=row[19],
            phone_no=row[20],
            phone_no_2=row[21],
            imsi_2=row[22],
            iccid_2=row[23],
            config_name=row[24],
            nav_submap_id=row[25]
            )
        device_info_list.append(device_info)

    return device_info_list
