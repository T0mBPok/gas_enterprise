from fastapi import Response
from openpyxl import Workbook
from fastapi.responses import StreamingResponse
from src.order.schemas import GetOrder
import io

def export_orders_xlsx(orders: list[GetOrder]):
    wb = Workbook()
    ws = wb.active

    ws.append([
        "ID", "Газ объем", "Стоимость",
        "Статус", "Клиент", "Телефон", "Дата"
    ])

    for o in orders:
        ws.append([
            o.id,
            o.gas_volume,
            o.cost,
            o.status.name,
            o.customer.name,
            o.customer.phone_num,
            o.created_at.strftime("%Y-%m-%d"),
        ])

    buf = io.BytesIO()
    wb.save(buf)

    return Response(
        content=buf.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=orders.xlsx"
        }
    )
