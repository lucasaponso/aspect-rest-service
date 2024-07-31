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
